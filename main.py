import os
import sys
import uuid
import zipfile

from openai import OpenAI
import json
import requests

# NVAI endpoint for the ocdrnet NIM
nvai_url="https://ai.api.nvidia.com/v1/cv/nvidia/ocdrnet"


API_KEY="nvapi-KEY_HERe"

header_auth = f"Bearer {API_KEY}"


def _respond(content):
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=API_KEY
    )

    for item in content['metadata']:
        del item["polygon"]

    prompt = f"As a financial advisor, analyse the OCR output below and tell me what the document contains.\n{content['metadata']}"

    completion = client.chat.completions.create(
        model="meta/llama-3.1-405b-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=True
    )

    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="")


def _upload_asset(input, description):
    """
    Uploads an asset to the NVCF API.
    :param input: The binary asset to upload
    :param description: A description of the asset

    """
    assets_url = "https://api.nvcf.nvidia.com/v2/nvcf/assets"

    headers = {
        "Authorization": header_auth,
        "Content-Type": "application/json",
        "accept": "application/json",
    }

    s3_headers = {
        "x-amz-meta-nvcf-asset-description": description,
        "content-type": "image/jpeg",
    }

    payload = {"contentType": "image/jpeg", "description": description}

    response = requests.post(assets_url, headers=headers, json=payload, timeout=30)

    response.raise_for_status()

    asset_url = response.json()["uploadUrl"]
    asset_id = response.json()["assetId"]

    response = requests.put(
        asset_url,
        data=input,
        headers=s3_headers,
        timeout=300,
    )

    response.raise_for_status()
    return uuid.UUID(asset_id)


if __name__ == "__main__":
    """Uploads an image of your choosing to the NVCF API and sends a
    request to the Optical character detection and recognition model.
    The response is saved to a local directory.

    Note: You must set up an environment variable, NGC_PERSONAL_API_KEY.
    """

    if len(sys.argv) != 3:
        print("Usage: python test.py <image> <output_dir>")
        sys.exit(1)

    asset_id = _upload_asset(open(sys.argv[1], "rb"), "Input Image")

    inputs = {"image": f"{asset_id}", "render_label": True}

    asset_list = f"{asset_id}"

    headers = {
        "Content-Type": "application/json",
        "NVCF-INPUT-ASSET-REFERENCES": asset_list,
        "NVCF-FUNCTION-ASSET-IDS": asset_list,
        "Authorization": header_auth,
    }

    response = requests.post(nvai_url, headers=headers, json=inputs)

    with open(f"TEMP/{asset_id}.zip", "wb") as out:
        out.write(response.content)

    with zipfile.ZipFile(f'TEMP/{asset_id}.zip', "r") as z:
        z.extractall(f'{sys.argv[2]}/{asset_id}')

    print(f"Output saved to {sys.argv[2]}/{asset_id}")
    print(os.listdir(sys.argv[2]))


    # Find the .response file in the asset output/asset_id directory
    response_files = [f for f in os.listdir(f'{sys.argv[2]}/{asset_id}') if f.endswith('.response')]
    response_file = response_files[0]
    response_file_path = f'{sys.argv[2]}/{asset_id}/{response_file}'

    # Open the unzipped file and send it to the LLM
    with open(response_file_path) as f:
        d = json.load(f)
        print(_respond(d))

    # Clean up
    os.remove(f"TEMP/{asset_id}.zip")

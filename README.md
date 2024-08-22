Example Script which implements NVidia NIM using OCR and LLM

# Usage

`
python main.py ./data/1.jpg output
`

Where ./data/1.jpg refers to the example image in this repo and output is the desired directory for the files to land in. It currently does not clean up the files as the generated images are useful for testingg.

# Example response from the input image

```
Based on the OCR output, the document appears to be a bank check. Here's a breakdown of the information it contains:

1. **Payee Information:**
   - Name: Mary Johnson
   - Address: 395 B5 Apt, Brooklyn, NY
   - Date: 2019

2. **Bank Details:**
   - Bank: USA Bank (with multiple branches)
   - Account Number: 001234567
   - Check Number: 0007

3. **Check Details:**
   - Type: Rent (monthly)
   - Amount: $100 and seventy-five dollars (likely a typo, should be $175)
   - Memo: J. Smith
   - Order/Payee: Mary Johnson
   - Check Number: 715

4. **Security Features:**
   - The check contains a watermark, microprinting, and colored security threads, as stated in the fine print at the bottom.

5. **Signature and Authorization:**
   - The check is signed and authorized.

6. **Potential Errors or Inconsistencies:**
   - The amount mentioned in the OCR output seems to have a mistake. It mentions "seven lifteen" which should likely be "seventy-five".
   - Some words like "lorem", "amet", "sit", "dolor" appear to be placeholders or random words that might have been misinterpreted by the OCR.

Here's a cleaned-up version of the check details:

- Pay to the order of: Mary Johnson
- Amount: $100.75
- For: Rent (monthly)
- Memo: J. Smith
- Date: 2019
- Check Number: 715
- Bank: USA Bank
- Account Number: 001234567
- Check Number: 0007None


```

# Running the Script on Windows

## Prerequisites 

* Install Python 3.X on the host machine -> https://www.python.org/downloads/
* Python PIP (this should be installed automatically with python but in case you have issues) -> https://packaging.python.org/en/latest/tutorials/installing-packages/#ensure-you-can-run-pip-from-the-command-line
* An NVidia NIM api key from the console -> https://build.nvidia.com/nvidia/

# Commands

Install the required libraries using `pip` by typing the following commands:

```
# Ensure latest versions of tools
py -m pip install --upgrade pip setuptools wheel
pip install openai
pip install requests
```

Navigate to the dirctory where the python file is stored then type the following command

```
python main.py ./data/1.jpg output
```

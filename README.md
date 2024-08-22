Example Script which implements NVidia NIM using OCR and LLM

# Usage

`
python main.py ./data/1.jpg output
`

Where ./data/1.jpg refers to the example image in this repo and output is the desired directory for the files to land in. It currently does not clean up the files as the generated images are useful for testingg.

# Example response form the input image

```
After analyzing the output, I can tell you that the document appears to be a **check** (also known as a cheque). Here's why:

1. **Check-related keywords**: The output contains keywords like "check", "cheque", "payable", "order", "pay", and "dollars", which are all related to a financial transaction.
2. **Banking information**: The output includes labels like "bank", "account", "no", "usa", and "branches", suggesting that the document is related to a banking transaction.
3. **Signature and authorization**: The presence of labels like "signature" and "authorized" implies that the document requires a signature to authorize the transaction.
4. **Date and address**: The output includes labels like "date", "2019", "brooklyn", "ny", and "apt", which suggest that the document contains a date and address.
5. **Security features**: The output mentions "watermark", "microprinting", and "colored paper", which are common security features used to prevent check counterfeiting.
6. **Payee information**: The output includes labels like "mary", "gohnson", and "12345", which appear to be the payee's name and address.

Based on these observations, I conclude that the document is a check, likely a personal check or a business check, containing the usual information such as the date, payee's name and address, payment amount, and authorization signature.

```

# 🔳 QR Code Studio

A small Streamlit app that makes clean, print-ready QR codes – one at a time or hundreds at once from a CSV file.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-app-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

## What it makes

| Type | Scanning it… |
|---|---|
| **Link** | opens the website |
| **UPI payment** | opens GPay / PhonePe / Paytm / BHIM with the payee, amount and note filled in |
| **WhatsApp chat** | opens a chat with the number, with a ready message |
| **Wi-Fi** | joins the network without typing the password |
| **Contact card** | saves name, phone, e-mail, company and website to the phone |
| **E-mail** | opens a new mail with address and subject filled in |
| **Plain text** | shows the text |

- Colours, size, quiet zone and error-correction level you choose; an optional logo in the centre.
- Download as **PNG**, or **SVG** for sharp printing at any size.
- **Bulk:** upload a CSV with `name,data` columns and get a ZIP with one PNG per row – handy for shop counters, asset labels or event badges.

## Run it

```bash
pip install -r requirements.txt
streamlit run Qr_Code.py
```

Or open the repository in **GitHub Codespaces** – the dev container installs everything and starts the app by itself.

## Tests

```bash
pip install pytest
pytest -q
```

The code that builds what goes inside each QR code lives in `qr_payloads.py`, separate from the screens, so it is tested on its own.

## Project layout

```
Qr_Code.py        the Streamlit app (screens, styling, PNG / SVG / ZIP downloads)
qr_payloads.py    builds the QR content for each type (UPI, Wi-Fi, vCard, …)
tests/            unit tests for qr_payloads.py
.devcontainer/    one-click GitHub Codespaces setup
```

---
Made by **Satyam Singh** · MIT licence

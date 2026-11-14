"""QR Code Studio - a small Streamlit app that makes clean, print-ready QR codes.

Run:  streamlit run Qr_Code.py
"""
from __future__ import annotations

import csv
import io
import re
import zipfile

import qrcode
import qrcode.image.svg
import streamlit as st
from PIL import Image
from qrcode.constants import ERROR_CORRECT_H, ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q

from qr_payloads import (email_payload, text_payload, upi_payload, url_payload, vcard_payload,
                         whatsapp_payload, wifi_payload)

st.set_page_config(page_title="QR Code Studio", page_icon="🔳", layout="wide")

LEVELS = {"Low (7 %)": ERROR_CORRECT_L, "Medium (15 %)": ERROR_CORRECT_M, "Quartile (25 %)": ERROR_CORRECT_Q, "High (30 %, best with a logo)": ERROR_CORRECT_H}


def make_qr(data: str, level: int, box: int, border: int, fill: str, back: str, logo: Image.Image | None = None) -> Image.Image:
    qr = qrcode.QRCode(error_correction=level, box_size=box, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color=back).convert("RGB")
    if logo is not None:
        side = img.size[0] // 4                       # the logo covers at most a quarter of the width
        mark = logo.convert("RGBA")
        mark.thumbnail((side, side))
        pad = Image.new("RGB", (mark.size[0] + 12, mark.size[1] + 12), back)
        pad.paste(mark, (6, 6), mark)
        img.paste(pad, ((img.size[0] - pad.size[0]) // 2, (img.size[1] - pad.size[1]) // 2))
    return img


def make_svg(data: str, level: int, border: int) -> bytes:
    qr = qrcode.QRCode(error_correction=level, border=border, image_factory=qrcode.image.svg.SvgPathImage)
    qr.add_data(data)
    qr.make(fit=True)
    buf = io.BytesIO()
    qr.make_image().save(buf)
    return buf.getvalue()


def png_bytes(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


def safe_name(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("_")[:60] or "qr"


st.title("🔳 QR Code Studio")
st.caption("Links, UPI payments, WhatsApp chats, Wi-Fi, contact cards and e-mails - as print-ready PNG or SVG. One at a time or in bulk from a CSV file.")

with st.sidebar:
    st.header("Style")
    level_name = st.selectbox("Error correction", list(LEVELS), index=1)
    box = st.slider("Module size (px)", 4, 20, 10)
    border = st.slider("Quiet zone (modules)", 1, 8, 4)
    fill = st.color_picker("QR colour", "#111111")
    back = st.color_picker("Background", "#FFFFFF")
    logo_file = st.file_uploader("Logo in the centre (optional)", type=["png", "jpg", "jpeg"])
    if logo_file is not None and level_name.startswith(("Low", "Medium")):
        st.info("With a logo, choose 'High' error correction so the code still scans.")

level = LEVELS[level_name]
logo = Image.open(logo_file) if logo_file is not None else None

single, bulk = st.tabs(["Single QR code", "Bulk from CSV"])

with single:
    kind = st.radio("What should the QR code do?", ["Link", "UPI payment", "WhatsApp chat", "Wi-Fi", "Contact card", "E-mail", "Plain text"], horizontal=True)
    left, right = st.columns([3, 2])
    with left:
        try:
            if kind == "Link":
                payload = url_payload(st.text_input("Link", placeholder="https://example.com"))
            elif kind == "UPI payment":
                c1, c2 = st.columns(2)
                payload = upi_payload(c1.text_input("UPI ID", placeholder="name@okbank"), c2.text_input("Payee name"),
                                      c1.text_input("Amount in ₹ (optional)"), c2.text_input("Note (optional)"))
            elif kind == "WhatsApp chat":
                payload = whatsapp_payload(st.text_input("Mobile number with country code", placeholder="91 98765 43210"),
                                           st.text_area("Message (optional)", height=80))
            elif kind == "Wi-Fi":
                c1, c2 = st.columns(2)
                sec = c2.selectbox("Security", ["WPA", "WEP", "nopass"], format_func=lambda s: "No password" if s == "nopass" else s)
                payload = wifi_payload(c1.text_input("Wi-Fi name (SSID)"), c1.text_input("Password", type="password"), sec, c2.checkbox("Hidden network"))
            elif kind == "Contact card":
                c1, c2 = st.columns(2)
                payload = vcard_payload(c1.text_input("Full name"), c2.text_input("Phone"), c1.text_input("E-mail"),
                                        c2.text_input("Company"), c1.text_input("Job title"), c2.text_input("Website"))
            elif kind == "E-mail":
                payload = email_payload(st.text_input("To"), st.text_input("Subject"), st.text_area("Message", height=80))
            else:
                payload = text_payload(st.text_area("Text", height=120))
            error = ""
        except ValueError as exc:
            payload, error = "", str(exc)
        if error:
            st.caption("ℹ️ " + error)
        if payload:
            with st.expander("What the QR code contains"):
                st.code(payload)

    with right:
        if payload:
            img = make_qr(payload, level, box, border, fill, back, logo)
            st.image(img, caption=f"{img.size[0]} × {img.size[1]} px")
            name = safe_name(kind.lower())
            st.download_button("⬇ Download PNG", png_bytes(img), f"{name}.png", "image/png", use_container_width=True)
            if logo is None:
                st.download_button("⬇ Download SVG (for print)", make_svg(payload, level, border), f"{name}.svg", "image/svg+xml", use_container_width=True)
        else:
            st.info("Fill in the details on the left - the QR code appears here.")

with bulk:
    st.write("Upload a CSV file with a **name** column and a **data** column (a link, UPI link or any text). You get one ZIP with a PNG per row.")
    st.download_button("Sample CSV", "name,data\nShop front,https://example.com\nCounter UPI,upi://pay?pa=name@okbank&pn=Shop&cu=INR\n", "sample.csv", "text/csv")
    up = st.file_uploader("CSV file", type=["csv"], key="bulk")
    if up is not None:
        rows = list(csv.DictReader(io.StringIO(up.getvalue().decode("utf-8-sig"))))
        rows = [r for r in rows if (r.get("data") or "").strip()]
        if not rows:
            st.error("No rows with a 'data' value were found. The first line must be: name,data")
        else:
            st.write(f"{len(rows)} QR codes will be made.")
            if st.button("Make the ZIP", type="primary"):
                buf, used = io.BytesIO(), {}
                with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
                    progress = st.progress(0.0)
                    for i, row in enumerate(rows, 1):
                        base = safe_name(row.get("name") or f"qr_{i}")
                        used[base] = used.get(base, 0) + 1
                        fname = base if used[base] == 1 else f"{base}_{used[base]}"
                        zf.writestr(f"{fname}.png", png_bytes(make_qr(row["data"].strip(), level, box, border, fill, back, logo)))
                        progress.progress(i / len(rows))
                st.download_button("⬇ Download ZIP", buf.getvalue(), "qr_codes.zip", "application/zip", type="primary")

st.divider()
st.caption("Made by Satyam Singh · Python · Streamlit · qrcode")

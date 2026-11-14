"""Builds the text that goes inside a QR code for each supported type.

Kept free of Streamlit and image code so it can be tested on its own.
"""
from __future__ import annotations

from urllib.parse import quote, urlencode


def _clean(value: str | None) -> str:
    return (value or "").strip()


def url_payload(url: str) -> str:
    url = _clean(url)
    if not url:
        raise ValueError("Enter a link.")
    if "://" not in url:
        url = "https://" + url
    return url


def text_payload(text: str) -> str:
    text = _clean(text)
    if not text:
        raise ValueError("Enter some text.")
    return text


def upi_payload(vpa: str, name: str, amount: str = "", note: str = "") -> str:
    """UPI payment link (NPCI format) - opens GPay / PhonePe / Paytm / BHIM with the payee filled in."""
    vpa, name, amount, note = _clean(vpa), _clean(name), _clean(amount), _clean(note)
    if "@" not in vpa:
        raise ValueError("Enter a valid UPI ID, for example name@okbank.")
    if not name:
        raise ValueError("Enter the payee name.")
    params = {"pa": vpa, "pn": name, "cu": "INR"}
    if amount:
        try:
            value = float(amount)
        except ValueError as exc:
            raise ValueError("Amount must be a number.") from exc
        if value <= 0:
            raise ValueError("Amount must be more than zero.")
        params["am"] = f"{value:.2f}"
    if note:
        params["tn"] = note[:80]
    return "upi://pay?" + urlencode(params, quote_via=quote)


def whatsapp_payload(phone: str, message: str = "") -> str:
    digits = "".join(ch for ch in _clean(phone) if ch.isdigit())
    if len(digits) == 10:
        digits = "91" + digits          # Indian mobile number without the country code
    if len(digits) < 11:
        raise ValueError("Enter the mobile number with country code, for example 91 98765 43210.")
    link = f"https://wa.me/{digits}"
    message = _clean(message)
    return link + (f"?text={quote(message)}" if message else "")


def _wifi_escape(value: str) -> str:
    for ch in ("\\", ";", ",", ":", '"'):
        value = value.replace(ch, "\\" + ch)
    return value


def wifi_payload(ssid: str, password: str = "", security: str = "WPA", hidden: bool = False) -> str:
    ssid = _clean(ssid)
    if not ssid:
        raise ValueError("Enter the Wi-Fi name.")
    security = security if security in ("WPA", "WEP", "nopass") else "WPA"
    if security != "nopass" and not password:
        raise ValueError("Enter the Wi-Fi password (or choose 'No password').")
    parts = [f"T:{security}", f"S:{_wifi_escape(ssid)}"]
    if security != "nopass":
        parts.append(f"P:{_wifi_escape(password)}")
    if hidden:
        parts.append("H:true")
    return "WIFI:" + ";".join(parts) + ";;"


def vcard_payload(name: str, phone: str = "", email: str = "", company: str = "", title: str = "", website: str = "") -> str:
    name = _clean(name)
    if not name:
        raise ValueError("Enter the name.")
    lines = ["BEGIN:VCARD", "VERSION:3.0", f"FN:{name}", f"N:{';'.join(reversed(name.split(' ', 1)))};;;"]
    if _clean(company):
        lines.append(f"ORG:{_clean(company)}")
    if _clean(title):
        lines.append(f"TITLE:{_clean(title)}")
    if _clean(phone):
        lines.append(f"TEL;TYPE=CELL:{_clean(phone)}")
    if _clean(email):
        lines.append(f"EMAIL:{_clean(email)}")
    if _clean(website):
        lines.append(f"URL:{url_payload(website)}")
    lines.append("END:VCARD")
    return "\n".join(lines)


def email_payload(to: str, subject: str = "", body: str = "") -> str:
    to = _clean(to)
    if "@" not in to:
        raise ValueError("Enter a valid e-mail address.")
    query = {k: v for k, v in (("subject", _clean(subject)), ("body", _clean(body))) if v}
    return f"mailto:{to}" + ("?" + urlencode(query, quote_via=quote) if query else "")

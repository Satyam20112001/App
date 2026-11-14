import pytest

from qr_payloads import email_payload, upi_payload, url_payload, vcard_payload, whatsapp_payload, wifi_payload


def test_url_adds_https():
    assert url_payload("example.com") == "https://example.com"


def test_upi_link():
    assert upi_payload("shop@okbank", "My Shop", "250", "Order 12") == "upi://pay?pa=shop%40okbank&pn=My%20Shop&cu=INR&am=250.00&tn=Order%2012"


def test_upi_rejects_bad_id_and_amount():
    with pytest.raises(ValueError):
        upi_payload("shop", "My Shop")
    with pytest.raises(ValueError):
        upi_payload("shop@okbank", "My Shop", "-5")


def test_whatsapp_adds_india_code():
    assert whatsapp_payload("98765 43210", "Hi there") == "https://wa.me/919876543210?text=Hi%20there"


def test_wifi_escapes_special_characters():
    assert wifi_payload("Office;5G", "pa:ss") == "WIFI:T:WPA;S:Office\;5G;P:pa\\:ss;;"
    assert wifi_payload("Guest", security="nopass") == "WIFI:T:nopass;S:Guest;;"


def test_vcard_and_email():
    card = vcard_payload("Satyam Singh", "+91 90000 00000", "me@example.com", "Example Ltd", "Developer", "example.com")
    assert card.startswith("BEGIN:VCARD") and "FN:Satyam Singh" in card and "URL:https://example.com" in card
    assert email_payload("me@example.com", "Hello there") == "mailto:me@example.com?subject=Hello%20there"

import requests
import os

BREVO_API_KEY = os.getenv("BREVO_API_KEY")

def send_email(to_email, message, user):
    url = "https://api.brevo.com/v3/smtp/email"

    payload = {
        "sender": {"email": user.smtp_email, "name": "rech.ai"},
        "to": [{"email": to_email}],
        "subject": "Quick introduction",
        "htmlContent": message.replace("\n", "<br>")
    }

    headers = {
        "accept": "application/json",
        "api-key": BREVO_API_KEY,
        "content-type": "application/json"
    }

    r = requests.post(url, json=payload, headers=headers)

    if r.status_code >= 300:
        raise Exception(r.text)

# app/ai_email.py

import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL_NAME = "gemma:2b"

def generate_email(name, company, industry):
    prompt = f"""
You are writing a genuine one-to-one cold email.

The goal is to start a real conversation, not to sell anything.

Recipient:
Name: {name}
Company: {company}
Industry: {industry}

Instructions:
- Use their name and company naturally
- Sound curious and thoughtful
- Briefly mention why you are reaching out
- Mention their industry in a relevant way
- Ask for a short call at the end
- No hype, no marketing language
- No phrases like "we help", "platform", "solution"
- 90–130 words
- Write like a real founder emailing another founder
"""

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "stream": False
    }

    try:
        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=120
        )
        response.raise_for_status()
        data = response.json()

        email = data["message"]["content"].strip()

        if len(email) < 50:
            raise ValueError("AI response too short")

        return email

    except Exception as e:
        print("⚠️ Ollama error:", e)
        return (
            f"Hi {name},\n\n"
            f"I came across {company} and noticed the work you're doing in the {industry} space.\n"
            f"I'd love to learn a bit more about how you're currently handling growth and outreach.\n\n"
            f"Would you be open to a quick 10–15 minute call sometime this week?\n\n"
            f"Best,\nManideep"
        )

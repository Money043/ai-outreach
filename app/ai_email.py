import os
import requests

GROQ_KEY = os.getenv("GROQ_API_KEY")

def generate_email(name, company, industry):
    prompt = f"""
Write a professional cold email.

Recipient name: {name}
Company: {company}
Industry: {industry}

The email should:
- Be personalized
- Explain how rech.ai helps
- Be 120–180 words
- End with a call to action
"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        },
        timeout=30
    )

    data = response.json()
    return data["choices"][0]["message"]["content"]

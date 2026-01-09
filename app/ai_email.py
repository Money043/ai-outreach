import os
import requests

GROQ_KEY = os.getenv("GROQ_API_KEY")

def generate_email(name, company, industry):
    prompt = f"""
Write a personalized cold email.

Recipient: {name}
Company: {company}
Industry: {industry}

Explain how rech.ai helps automate outreach.
Make it 120–180 words and end with a call to action.
"""

    try:
        r = requests.post(
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

        data = r.json()

        if "choices" not in data:
            print("Groq error:", data)
            return "Hi, we help businesses automate outreach. Let me know if you'd like to chat."

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("Groq crash:", e)
        return "Hi, we help businesses automate outreach. Let me know if you'd like to chat."

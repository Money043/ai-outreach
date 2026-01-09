import pandas as pd
from app.ai_email import generate_email
from app.send_email import send_email

def run_campaign(user):
    print(f"🚀 Campaign started for {user}")

    path = f"data/{user}/leads.csv"

    try:
        df = pd.read_csv(path)
    except:
        print("❌ No leads file found for", user)
        return

    for _, row in df.iterrows():
        name = row["name"]
        email = row["email"]
        company = row.get("company", "their company")
        industry = row.get("industry", "their industry")

        print(f"✉️ Generating email for {email}")

        message = generate_email(name, company, industry)

        print("📨 Sending email...")
        send_email(email, message, user)

        print(f"✅ Email sent to {email}")

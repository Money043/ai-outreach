import pandas as pd
from app.ai_email import generate_email
from app.send_email import send_email
from app.logger import log

def run_campaign(user):
    log(user, "Campaign started")

    path = f"data/{user}/leads.csv"
    try:
        df = pd.read_csv(path)
    except:
        log(user, "No leads file found")
        return

    for _, row in df.iterrows():
        name = row["name"]
        email = row["email"]
        company = row.get("company", "their company")
        industry = row.get("industry", "their industry")

        log(user, f"Generating email for {email}")

        message = generate_email(name, company, industry)

        log(user, f"Sending to {email}")
        send_email(email, message, user)

        log(user, f"Sent to {email}")

    log(user, "Campaign finished")

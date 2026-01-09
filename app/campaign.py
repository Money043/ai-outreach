from app.database import SessionLocal
from app.models import User
from app.ai_email import generate_email
from app.send_email import send_email

def run_campaign(leads, logged_in_user_email):
    db = SessionLocal()

    # Load full user from DB
    user = db.query(User).filter(User.email == logged_in_user_email).first()

    if not user:
        raise Exception("User not found")

    for lead in leads:
        email = lead["email"]
        name = lead["name"]
        company = lead["company"]
        industry = lead["industry"]

        print("✉️ Generating email for", email)

        message = generate_email(name, company, industry)

        print("📨 Sending email...")
        send_email(email, message, user)

    db.close()

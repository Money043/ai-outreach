import smtplib
from email.message import EmailMessage
from database import SessionLocal
from app.models import User

def send_email(to, content, user):
    db = SessionLocal()
    u = db.query(User).filter(User.email == user).first()

    if not u.smtp_email or not u.smtp_password:
        raise Exception("No email connected")

    msg = EmailMessage()
    msg["From"] = u.smtp_email
    msg["To"] = to
    msg["Subject"] = "Quick question"
    msg.set_content(content)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(u.smtp_email, u.smtp_password)
        server.send_message(msg)

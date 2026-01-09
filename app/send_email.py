import smtplib
from email.message import EmailMessage
from database import SessionLocal
from app.models import User

def send_email(to, content, user):
    db = SessionLocal()
    u = db.query(User).filter(User.email == user).first()

    msg = EmailMessage()
    msg["From"] = u.sender_email
    msg["To"] = to
    msg["Subject"] = "Quick question"
    msg.set_content(content)

    with smtplib.SMTP("smtp-relay.brevo.com", 587) as server:
        server.starttls()
        server.login(u.brevo_login, u.brevo_password)
        server.send_message(msg)

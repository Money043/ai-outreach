from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Depends
from fastapi.responses import FileResponse
import shutil
import os

from fastapi.staticfiles import StaticFiles
from app.campaign import run_campaign
from app.models import User
from app.auth import hash_password, verify_password, create_token, get_current_user
from database import SessionLocal, Base, engine

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Create DB tables
Base.metadata.create_all(bind=engine)

# ---------------- DASHBOARD ----------------

@app.get("/")
def dashboard():
    return FileResponse("frontend/login.html")

# ---------------- AUTH ----------------

@app.post("/signup")
def signup(email: str, password: str):
    db = SessionLocal()
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        return {"error": "User already exists"}

    user = User(email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    return {"message": "User created"}

@app.post("/login")
def login(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password):
        return {"error": "Invalid credentials"}

    token = create_token(user.email)
    return {"access_token": token}

# ---------------- FILE UPLOAD (PER USER) ----------------

@app.post("/upload")
async def upload(file: UploadFile = File(...), user=Depends(get_current_user)):
    user_dir = f"data/{user}"
    os.makedirs(user_dir, exist_ok=True)

    with open(f"{user_dir}/leads.csv", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": "Leads uploaded for " + user}

# ---------------- START CAMPAIGN (PER USER) ----------------

@app.post("/start-campaign")
def start_campaign(background_tasks: BackgroundTasks, user=Depends(get_current_user)):
    background_tasks.add_task(run_campaign, user)
    return {"message": "Campaign started for " + user}

@app.post("/connect-email")
def connect_email(sender_email: str, brevo_login: str, brevo_password: str, user=Depends(get_current_user)):
    db = SessionLocal()
    u = db.query(User).filter(User.email == user).first()

    u.sender_email = sender_email
    u.brevo_login = brevo_login
    u.brevo_password = brevo_password
    db.commit()

    return {"message": "Email connected"}



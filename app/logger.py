import os
from datetime import datetime

def log(user, msg):
    os.makedirs(f"logs/{user}", exist_ok=True)
    with open(f"logs/{user}/campaign.log", "a") as f:
        f.write(f"{datetime.now()} — {msg}\n")

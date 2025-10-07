# app/utils.py
from datetime import datetime

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("booking_log.txt", "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(message)

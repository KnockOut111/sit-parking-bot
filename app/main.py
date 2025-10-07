
# app/main.py
import schedule
import time
from booking import run_booking
from dotenv import load_dotenv
import os

load_dotenv()
BOOK_TIME = os.getenv("BOOK_TIME", "07:55")

print(f"⏰ Scheduler active — booking will run every day at {BOOK_TIME}")

schedule.every().day.at(BOOK_TIME).do(run_booking)

while True:
    schedule.run_pending()
    time.sleep(60)

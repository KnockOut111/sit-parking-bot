# app/booking.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os, time

load_dotenv()

USERNAME = os.getenv("SIT_USERNAME")
PASSWORD = os.getenv("SIT_PASSWORD")

def init_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    return webdriver.Chrome(options=options)

def login(driver):
    driver.get("https://bolig.sit.no/")
    # TODO: Add login logic here (Feide / Sit credentials)
    print("Login simulated — replace with actual logic")

def run_booking():
    driver = init_driver()
    try:
        login(driver)
        # TODO: Navigate to parking booking page
        # TODO: Fill out form fields and submit
        print("Booking simulated — replace with actual navigation & form selectors")
    finally:
        driver.quit()

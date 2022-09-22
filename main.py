import os
import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

CHROME_DRIVER_PATH = "/Users/godma/Documents/1. Coding Projects/ChromeDriver/chromedriver"
SERVICE = Service(executable_path=CHROME_DRIVER_PATH)
USERNAME = "godmantan@gmail.com"
PASSWORD = os.environ.get("PASSWORD")
CAMP_LOCATION = input("What is the URL of the campground (https://www.recreation.gov/camping/campgrounds/#####)?")
SITE_LOCATION = input("What is the URL of the exact SITE within the campground (https://www.recreation.gov/camping/campsites/#####)?")
SITE_ID = SITE_LOCATION.strip("https://www.recreation.gov/camping/campsites/")
# print(SITE_ID)

CHECK_IN = input("What is the check-in date (MM/DD/YYYY)?")
check_in_converted = datetime.strptime(CHECK_IN, '%m/%d/%Y').strftime('%b %d %Y')
# print(check_in_converted)

CHECK_OUT = input("What is the check-out date (MM/DD/YYYY)?")
check_out_converted = datetime.strptime(CHECK_OUT, '%m/%d/%Y').strftime('%b %d %Y')
# print(check_out_converted)

driver = webdriver.Chrome(service=SERVICE)
driver.get(f"{CAMP_LOCATION}")

check_in = driver.find_element(By.ID, "campground-start-date-calendar")
check_in.send_keys(CHECK_IN)

check_out = driver.find_element(By.ID, "campground-end-date-calendar")
check_out.send_keys(CHECK_OUT)

driver.get(f"{SITE_LOCATION}")
time.sleep(3)

cart_button = driver.find_element(By.ID, "add-cart-campsite")

keep_trying = True
while keep_trying:
    try:
        cart_text = driver.find_element(By.XPATH, "//span[text()='Add to Cart']").text
        if cart_text == "Add to Cart":
            cart_button.click()

            time.sleep(2)

            email_input = driver.find_element(By.ID, "email")
            email_input.send_keys(USERNAME)
            password_input = driver.find_element(By.ID, "rec-acct-sign-in-password")
            password_input.send_keys(PASSWORD)
            driver.find_element(By.CLASS_NAME, "rec-acct-sign-in-btn").click()
            keep_trying = False
    except NoSuchElementException:
        driver.refresh()
        time.sleep(3)






import undetected_chromedriver as uc
import random
import json
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('shoppy_mail')
PASSWORD = os.getenv('shoppy_password')

# Log in if required
def login_if_required(driver, wait, username, password):
    try:
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "loginKey")))
        print("Logging in now...")
        password_field = driver.find_element(By.NAME, "password")
        username_field.send_keys(username)
        time.sleep(random.uniform(1, 3))
        password_field.send_keys(password)
        time.sleep(random.uniform(1, 2))
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
    except Exception:
        print("Already logged in or login form not present.")

# Simulate human-like behavior
def simulate_human_behavior(driver, num_actions=10):
    print("Simulating human-like behavior...")
    actions = ActionChains(driver)
    for _ in range(num_actions):
        scroll_y = random.randint(100, 800)
        driver.execute_script(f"window.scrollBy(0, {scroll_y});")
        time.sleep(random.uniform(0.5, 2))

    elements = driver.find_elements(By.CSS_SELECTOR, "div")
    for _ in range(num_actions):
        if elements:
            element = random.choice(elements)
            try:
                actions.move_to_element(element).pause(random.uniform(0.5, 2)).perform()
            except:
                pass
    print("Human-like actions completed.")

# Load cookies from file
with open("shopee_seller.json", "r") as file:
    cookies = json.load(file)

# Setup undetected Chrome options
options = uc.ChromeOptions()

options.add_argument(r"--user-data-dir=~/.config/google-chrome/Profile 3")
options.add_argument("--profile-directory=Profile 3")

options.add_argument("--disable-blink-features=AutomationControlled")

# Initialize undetected Chrome driver
driver = uc.Chrome(options=options)

driver.get("https://shopee.sg")
time.sleep(2)

# Set cookies via CDP
for cookie in cookies:
    cookie_payload = {
        "name": cookie['name'],
        "value": cookie['value'],
        "domain": cookie['domain'],
        "path": cookie.get('path', '/'),
        "secure": cookie.get('secure', False),
        "httpOnly": cookie.get('httpOnly', False),
    }
    if 'expirationDate' in cookie:
        cookie_payload['expires'] = int(cookie['expirationDate'])
    try:
        driver.execute_cdp_cmd("Network.setCookie", cookie_payload)
    except Exception as e:
        print(f"Failed to set cookie {cookie['name']}: {e}")

driver.refresh()
time.sleep(5)

wait = WebDriverWait(driver, 20)

# Login if needed
login_if_required(driver, wait, USERNAME, PASSWORD)

time.sleep(random.randint(3, 5))
simulate_human_behavior(driver, num_actions=random.randint(5, 12))
driver.get("http://shopee.sg")
simulate_human_behavior(driver, num_actions=random.randint(5, 12))
time.sleep(random.randint(2, 5))
from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from urllib.parse import urlparse
import random
import json
import time
import csv
import os


from behavior_function import simulate_human_behavior
load_dotenv()
email = os.getenv('shoppy_mail')
password = os.getenv('shoppy_password')

options = uc.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

driver = uc.Chrome(version_main=141,options=options)

site_url = "https://shopee.sg"
driver.get(site_url)
driver.maximize_window()

# wait for page to load
WebDriverWait(driver, 15).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

with open("shopee_seller.json", "r", encoding="utf-8") as f:
    cookies = json.load(f)

# helper to normalize expiry keys
def get_expiry(cookie):
    for key in ("expiry", "expirationDate", "expires", "expire", "expiration"):
        if key in cookie and cookie[key]:
            try:
                return int(float(cookie[key]))
            except Exception:
                pass
    return None

current_host = urlparse(driver.current_url).hostname  # e.g. 'shopee.sg'

added = 0
for cookie in cookies:
    # minimal cookie payload required by Selenium
    cookie_payload = {
        "name": cookie.get("name"),
        "value": cookie.get("value", ""),
    }

    # optional fields
    if cookie.get("path"):
        cookie_payload["path"] = cookie["path"]
    if "secure" in cookie:
        cookie_payload["secure"] = bool(cookie["secure"])
    if "httpOnly" in cookie:
        # Selenium expects 'httpOnly' or 'httponly' depending on driver - include it
        cookie_payload["httpOnly"] = bool(cookie["httpOnly"])

    expiry = get_expiry(cookie)
    if expiry:
        cookie_payload["expiry"] = expiry

    # Only include domain if it matches current host; otherwise omit it.
    domain = cookie.get("domain")
    if domain:
        normalized_domain = domain.lstrip(".")
        if normalized_domain == current_host:
            cookie_payload["domain"] = domain
        else:
            # skip setting domain to avoid InvalidCookieDomainException
            pass

    try:
        driver.add_cookie(cookie_payload)
        added += 1
    except Exception as e:
        print(f"Failed to add cookie {cookie.get('name')!r}: {e}. Payload: {cookie_payload}")

print(f"Attempted to add {len(cookies)} cookies, successfully added {added} (approx).")
# A short wait then refresh so the site picks up cookies
time.sleep(1)
driver.refresh()
time.sleep(5)



try:
    close_popUP = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="HomePagePopupBannerSection"]/div[2]/div'))
    )
    delay = random.uniform(0.5,0.9)
    actions = ActionChains(driver)
    actions.move_to_element(close_popUP).pause(delay).click().perform()
except:
    print("dint got the popup")



simulate_human_behavior(driver, 3)


# got to mobile accories page
driver.get('https://shopee.sg/Mobile-Gadgets-cat.11013350?page=0&sortBy=sales')

WebDriverWait(driver, 15).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

simulate_human_behavior(driver, 4)

WebDriverWait(driver, 20).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.col-xs-2-4.shopee-search-item-result__item'))
)


products_data = []

PageProducts = driver.find_elements(By.CSS_SELECTOR, '.col-xs-2-4.shopee-search-item-result__item')

for product in PageProducts:
    try:
        detils_link = product.find_element(By.CSS_SELECTOR, '.contents').get_attribute('href')
        image_link = product.find_element(By.XPATH, ".//a/div/div[1]/img").get_attribute('src')
        Name = product.find_element(By.XPATH, './/a[1]/div/div[2]/div[1]/div[1]').text
        
        products_data.append({
            "name": Name,
            "image": image_link,
            "details_link": detils_link
        })
        simulate_human_behavior(driver, 1)
        
    except Exception as e:
        print("Error:", e)

with open('shopee_products.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "image", "details_link"])
    writer.writeheader()
    writer.writerows(products_data)

print("✅ Saved to shopee_products.csv")


driver.quit()
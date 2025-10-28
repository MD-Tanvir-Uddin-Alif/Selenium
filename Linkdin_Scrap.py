from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time



options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)
driver.get('https://www.linkedin.com/')
driver.maximize_window()

time.sleep(2)

signIn_Button = driver.find_element(By.XPATH, '/html/body/nav/div/a[1]').click()

time.sleep(3)

email = ''
password = ''

# ---- LOGIN ----
send_email = driver.find_element(By.XPATH, '//*[@id="username"]')
send_email.send_keys(email)
time.sleep(1.5)
send_email.send_keys(Keys.ENTER)
time.sleep(2)

send_password = driver.find_element(By.XPATH, '//*[@id="password"]')
send_password.send_keys(password)
time.sleep(1.5)
send_password.send_keys(Keys.ENTER)
time.sleep(2)

# ---- CAPTCHA HANDLING ----
try:
    WebDriverWait(driver, 5).until(
        EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe"))
    )
    print("⚠ CAPTCHA detected — please solve it manually in the browser...")

    # WAIT until CAPTCHA is solved (watch URL change)
    while True:
        if "feed" in driver.current_url or "checkpoint" not in driver.current_url:
            print("✅ CAPTCHA cleared — continuing automation")
            driver.switch_to.default_content()
            break
        time.sleep(2)

except Exception:
    print("✅ No CAPTCHA — continuing")





WebDriverWait(driver, 20).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)



hashtag = "google" 
url = f"https://www.linkedin.com/search/results/content/?keywords=%23{hashtag}&origin=FACETED_SEARCH&sortBy=%22date_posted%22"
driver.get(url)
time.sleep(7)
# WebDriverWait(driver, 20).until(
#     lambda d: d.execute_script("return document.readyState") == "complete"
# )


WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.artdeco-card.mb2'))
        )



for _ in range(3):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

content_list = driver.find_elements(By.CSS_SELECTOR, ".artdeco-card.mb2")

for index, content in enumerate(content_list, 1):
    try:
        # Scroll the post into the center of the viewport
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", content)
        time.sleep(1)
        
        
        time.sleep(1)  # Pause so you can see which post is highlighted
        
        # Try to click the comment button
        comment_button = content.find_element(
            By.CSS_SELECTOR,
            '.social-actions-button.comment-button'
        )
        comment_button.click()
        time.sleep(2)

        # If comment box appears -> type comment
        comment_box = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ql-editor'))
        )
        
        comment_box = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.ql-editor'))
        )
        
        comment_box.click()
        time.sleep(0.5)
        
        
        comment_box.send_keys("something")
        time.sleep(2)
        
        print(f" Comment posted on post #{index}")

    except Exception as e:
        try:
            driver.find_element(By.CSS_SELECTOR, ".comments-disabled-comments-block")
            print(f"Comments disabled on post #{index} — skipping")
            continue
        except:
            print(f"⚠️ No active comment box on post #{index} — skipping")
            continue

print(f"Total posts: {len(content_list)}")
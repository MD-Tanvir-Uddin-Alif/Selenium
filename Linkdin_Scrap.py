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

time.sleep(2)

signIn_Button = driver.find_element(By.XPATH, '/html/body/nav/div/a[1]').click()

time.sleep(3)

email = 'mdtanviruddinalif@gmail.com'
password = 'dummy2345'

send_emil = driver.find_element(By.XPATH, '//*[@id="username"]')
time.sleep(1.1)
send_emil.send_keys(email)
time.sleep(1.8)
send_emil.send_keys(Keys.ENTER)
time.sleep(2.7)

send_password = driver.find_element(By.XPATH, '//*[@id="password"]')
time.sleep(1.3)
send_password.send_keys(password)
time.sleep(2.3)
send_password.send_keys(Keys.ENTER)
time.sleep(2.8)


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


content_list = driver.find_elements(By.CSS_SELECTOR, ".artdeco-card.mb2")

for content in content_list:
    try:
        # Try to click the comment button
        comment_button = content.find_element(
            By.CSS_SELECTOR,
            '.social-actions-button.comment-button'
        )
        comment_button.click()
        time.sleep(1)

        # If comment box appears -> type comment
        comment_box = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ql-editor'))
        )
        comment_box.send_keys("something")
        time.sleep(2)
        print("Comment posted")

    except Exception as e:
        try:
            # Comment button exists, but comments are disabled
            driver.find_element(By.CSS_SELECTOR, ".comments-disabled-comments-block")
            print("Comments disabled — skipping this post")
            continue
        except:
            print("⚠️ No active comment box — skipping")
            continue


# time.sleep(10)

print(len(content_list))
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
driver.get("https://www.flipkart.com/")

try:
    # Input search
    input_search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="q"]'))
    )
    input_search.send_keys("laptops")
    input_search.send_keys(Keys.ENTER)

    # Wait for product cards
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '._75nlfW'))
    )
    time.sleep(3)  # Wait for all nested content (images, scripts) to load

    # Get all product cards
    product_cards = driver.find_elements(By.CSS_SELECTOR, '._75nlfW')
    print(f"Found {len(product_cards)} products")

    # Prepare HTML
    all_cards_html = '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Flipkart Laptops</title>\n</head>\n<body>\n'

    for idx, card in enumerate(product_cards, 1):
        driver.execute_script("arguments[0].scrollIntoView(true);", card)
        time.sleep(0.5)

        # This will include all nested content!
        card_html = card.get_attribute('outerHTML')
        all_cards_html += f"<!-- Product {idx} -->\n{card_html}\n\n"

    all_cards_html += '</body>\n</html>'

    # Save to HTML file
    with open("flipkart_laptops_full_cards.html", "w", encoding="utf-8") as f:
        f.write(all_cards_html)

    print("All product cards saved successfully!")

finally:
    driver.quit()

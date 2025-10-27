from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#-----------------
# Set up
#-----------------
driver = webdriver.Edge()
driver.get("https://www.flipkart.com/")

try:
    #-----------------
    # Giving input
    #-----------------
    input_search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="q"]'))
    )
    input_search.send_keys("laptops")
    input_search.send_keys(Keys.ENTER)

    #-----------------------------------------------------
    # Wait for product cards to load
    #-----------------------------------------------------
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '._75nlfW'))
    )
    
    # Additional wait for images to load
    time.sleep(3)

    #---------------------------------
    # Taking all the product cards
    #---------------------------------
    Products_Cards = driver.find_elements(By.CSS_SELECTOR, '._75nlfW')
    
    print(f"Found {len(Products_Cards)} products")

    for index, card in enumerate(Products_Cards, 1):
        try:
            # Scroll the card into view
            driver.execute_script("arguments[0].scrollIntoView(true);", card)
            time.sleep(0.5)
            
            product_images = card.find_elements(By.TAG_NAME, 'img')
            image_src = product_images[0].get_attribute('src')
            product_link = card.find_element(By.XPATH, './/a').get_attribute('href')
            product_name = (
                card.find_element(By.XPATH, './/a/div[2]/div[1]/div[1]').text.strip() 
                if card.find_element(By.XPATH, './/a/div[2]/div[1]/div[1]').text.strip() 
                else card.find_element(By.XPATH, './/a/div[2]/div[1]/div[2]').text.strip()
                )
            
            
            product_rating = (
                card.find_element(By.XPATH, './/a/div[2]/div[1]/div[3]/span[1]/div').text.strip()
                if card.find_element(By.XPATH, './/a/div[2]/div[1]/div[3]/span[1]/div').text.strip()
                else card.find_element(By.XPATH, './/a/div[2]/div[1]/div[2]/span[1]/div').text.strip()
                )

            print('---------------------------------------------------------------------------------------')
            print(f"Product Link {index}: {product_link}")
            print(f"Product Image {index}: {image_src}")
            print(f"Product Title {index}: {product_name}")
            print(f"Product Title {index}: {product_rating}")
            
        except Exception as e:
            print(f"Error getting image for product {index}: {str(e)}")
            continue

finally:
    time.sleep(2)
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.edge.options import Options
import time
import csv


#-----------------
# Set up
#-----------------

# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')

# Create CSV with headers only once
with open("flipkart_laptops.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Product Name", "Price", "Image", "Link"])


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
    for i in range(1,6):
        print(f'-------------page{i}------------------')
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
                
                product_price = card.find_element(By.XPATH, './/a/div[2]/div[2]/div[1]/div/div[1]').text
                
                
                # product_rating = (
                #     card.find_element(By.XPATH, './/a/div[2]/div[1]/div[2]/span[1]/div').text.strip()
                #     if card.find_element(By.XPATH, './/a/div[2]/div[1]/div[2]/span[1]/div').text.strip()
                #     else card.find_element(By.XPATH, './/a/div[2]/div[1]/div[3]/span[1]/div').text.strip()
                #     )

                print('---------------------------------------------------------------------------------------')
                # print(f"all images: {product_images}")
                print(f"Product Link {index}: {product_link}")
                print(f"Product Image {index}: {image_src}")
                print(f"Product Title {index}: {product_name}")
                print(f"Product Title {index}: {product_price}")
                with open("flipkart_laptops.csv", "a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([product_name, product_price, image_src, product_link])

                
            except Exception as e:
                print(f"Error getting image for product {index}: {str(e)}")
                continue
            
        try:
            next_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//span[text()="Next"]'))
            )
            next_btn.click()
            time.sleep(1)  # wait for next page to load
        except:
            print("No more pages. Scraping finished.")
            break

finally:
    time.sleep(2)
    driver.quit()
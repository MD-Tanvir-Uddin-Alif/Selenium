from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv


all_products = []


driver = webdriver.Edge()

driver.get('https://www.flipkart.com/')

input_search = driver.find_element(By.XPATH, '//input[@name="q"]')
input_search.send_keys("smart watches")
input_search.send_keys(Keys.ENTER)

time.sleep(5)  

product_card = driver.find_elements(By.XPATH, '//div[@class="_1sdMkc LFEi7Z"]')
print(len(product_card))

for index, product in enumerate(product_card, 1):
    try:
        link = product.find_element(By.XPATH, './/a').get_attribute('href')
        print(f'Opening product {index}: {link}')

        driver.execute_script("window.open(arguments[0], '_blank');", link)
        driver.switch_to.window(driver.window_handles[1])
        
        time.sleep(13)

        watch_name = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span').text
        watch_price = driver.find_element(By.XPATH , '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]').text
        watch_image = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/img').get_attribute('src')
        # watch_ratting = driver.find_element(By.XPATH , '//*[@id="productRating_LSTSMWGEH7VGYMGCP3VXIJHDY_SMWGEH7VGYMGCP3V_"]/div').text
        # watch_warrenty = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[5]/div/div[2]/div').text
        
        print(f'---------------------------------------------------------{index}-------------------------------------------')
        print(f'Opening product {index}: {link}')
        print(watch_name)
        print(watch_image)
        print(watch_price)
        # print(watch_ratting)
        # print(watch_warrenty)
        
        all_products.append({
            'Name':watch_name,
            'Image_link': watch_image,
            'Price': watch_price,
            'Link':link
        })

        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
    except Exception as e:
        print(f"Skipping product {index} due to error: {e}")



csv_file = 'flipkart_smartwatches.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['Name', 'Price', 'Image_link', 'Link'])
    writer.writeheader()
    writer.writerows(all_products)
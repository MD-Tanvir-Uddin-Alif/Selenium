from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge()

driver.get('https://www.flipkart.com/')

search = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/header/div[1]/div[2]/form/div/div/input')
search.send_keys("smart watches")
search.send_keys(Keys.ENTER)
watches = driver.find_elements(By.XPATH, '//img[contains(@src, "http")]')


# print(len(watches))

for i in range(1,len(watches)+1):
    try:
        watch_link = driver.find_element(By.XPATH, f'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[{i}]/div/a/div[1]/div/div/div/img').get_attribute('src')
        watch_name = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[{i}]/div/div/a[1]').get_attribute('title')
        watch_price = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[{i}]/div/div/a[2]/div/div[1]').text
        watch_discount_price = driver.find_element(By.XPATH, f'/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div[{i}]/div/div/a[2]/div/div[3]/span').text

        print("------------------------------------------------------------")
        print(watch_link)
        print(watch_name)
        print(watch_price)
        print(watch_discount_price)
        print("-------------------------------------------------------------")
    except:
        print("-------------------------------------------------------------")
        print(f"item is messing: {i}")
        print("-------------------------------------------------------------")





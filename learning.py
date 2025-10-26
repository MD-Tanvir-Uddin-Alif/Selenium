from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge()

driver.get('https://cse.wub.edu.bd/main/faculty_member_details/79')

data = driver.find_element(By.XPATH ,'//*[@id="overview"]/div/div/div/div[2]/div[1]/div/div[2]').text

print(data)

driver.quit()

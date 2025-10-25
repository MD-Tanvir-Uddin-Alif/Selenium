from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

driver = webdriver.Edge()
driver.get('https://www.scrapethissite.com/pages/ajax-javascript/')

file = open("films.csv", mode="w", newline="", encoding="utf-8")
writer = csv.writer(file)

writer.writerow(["Year", "Film Name", "Nominations", "Awards", "Winner"])

for year in range(2010, 2016):
    driver.find_element(By.ID, str(year)).click()
    time.sleep(2)

    films = driver.find_elements(By.CLASS_NAME, 'film')
    
    for film in films:
        film_name = film.find_element(By.CLASS_NAME, 'film-title').text
        film_nominations = film.find_element(By.CLASS_NAME, 'film-nominations').text
        film_awards = film.find_element(By.CLASS_NAME, 'film-awards').text
        
        try:
            film.find_element(By.CLASS_NAME, "film-best-picture").find_element(By.TAG_NAME, "i")
            is_winner = "YES"
        except:
            is_winner = "NO"
        
        writer.writerow([year, film_name, film_nominations, film_awards, is_winner])

file.close()
print("Data saved successfully to films.csv")
driver.quit()

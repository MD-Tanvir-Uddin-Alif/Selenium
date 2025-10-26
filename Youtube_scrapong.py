import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Making driver
driver = webdriver.Edge()
driver.get('https://www.youtube.com/')

# Searching by input
search_by_input = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
search_by_input.send_keys("movies")
search_by_input.send_keys(Keys.ENTER)

# Wait until the page loaded
WebDriverWait(driver, 20).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

# Wait for video elements
try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-rich-item-renderer"))
    )
    video_container = driver.find_elements(By.CSS_SELECTOR, "ytd-rich-item-renderer")
except:
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-video-renderer"))
    )
    video_container = driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer")

# Open CSV file
with open("youtube_videos.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Video Link", "Views", "Channel Link"])

    # Extract data 
    for video in video_container:
        try:
            video_link = video.find_element(By.CSS_SELECTOR, '#thumbnail').get_attribute('href')
        except:
            video_link = "N/A"
        try:
            video_title = video.find_element(By.CSS_SELECTOR, '#video-title').get_attribute('title')
        except:
            video_title = "N/A"
        try:
            video_views = video.find_element(By.CSS_SELECTOR, '.inline-metadata-item.style-scope.ytd-video-meta-block').text
        except:
            video_views = "N/A"
        try:
            video_channel_link = video.find_element(By.CSS_SELECTOR, 'a.yt-simple-endpoint.style-scope.yt-formatted-string').get_attribute('href')
        except:
            video_channel_link = "N/A"

        writer.writerow([video_title, video_link, video_views, video_channel_link])

driver.quit()
print("Scraping complete! Data saved to youtube_videos.csv")

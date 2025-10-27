import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options

# --------------------------
# Setup
# --------------------------

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')


driver = webdriver.Edge(options=options)
driver.get('https://www.youtube.com/')

# Search input
search_input = driver.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
search_input.send_keys("best phone under 40000 in bangladesh 2025")
search_input.send_keys(Keys.ENTER)

# Wait until search results load
WebDriverWait(driver, 20).until(
    lambda d: d.execute_script("return document.readyState") == "complete"
)

# --------------------------
# Scroll to load more videos
# --------------------------
scroll_pause_time = 2
last_height = driver.execute_script("return document.documentElement.scrollHeight")

for _ in range(10):  # scroll 10 times, adjust as needed
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break  # no more videos loaded
    last_height = new_height

# --------------------------
# Get all video containers
# --------------------------
try:
    video_container = driver.find_elements(By.CSS_SELECTOR, "ytd-rich-item-renderer")
    if not video_container:
        video_container = driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer")
except:
    video_container = driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer")

print(f"Found {len(video_container)} videos.")

# --------------------------
# Save data to CSV
# --------------------------
with open("youtube_videos_2.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Video Link", "Views", "Channel Link"])  # header

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

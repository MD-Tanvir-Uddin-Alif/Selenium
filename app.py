from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests


url = requests.get("https://www.scrapethissite.com/pages/ajax-javascript/#2015").json()

html_template = BeautifulSoup(url, 'lxml')

print(html_template)
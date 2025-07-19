from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

s = Service("C:/Users/tirth/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://quotes.toscrape.com/scroll')

# Wait for initial load
time.sleep(3)

# Scroll to the bottom to load all products
# Below Code Is Needed When Entire Page is not loading in one shot.
#Start

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # wait for new content to load

    # Check if more content loaded
    new_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
    print(new_height)
    if new_height == last_height:
        break  # No more content
    last_height = new_height

#End

# Now grab full HTML
html = driver.page_source
# soup = BeautifulSoup(html, 'lxml')

with open('quotes.html','w',encoding='utf-8') as f:
    f.write(html)

input("Press Enter to close browser...")
driver.quit()

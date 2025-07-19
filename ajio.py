from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

s = Service("C:/Users/tirth/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('https://www.ajio.com/men-belts/c/830201007')

time.sleep(3)

prev_count = 0
same_count_repeats = 0

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for products to load

    # Count how many products have loaded so far
    products = driver.find_elements(By.CLASS_NAME, 'item')  # or use a better selector
    current_count = len(products)
    print(f"Loaded products: {current_count}")

    if current_count == prev_count:
        same_count_repeats += 1
    else:
        same_count_repeats = 0

    if same_count_repeats >= 3:
        print("No more products loaded. Exiting scroll.")
        break

    prev_count = current_count

html = driver.page_source
with open('belts.html', 'w', encoding='utf-8') as f:
    f.write(html)

input("Press Enter to close browser...")
driver.quit()

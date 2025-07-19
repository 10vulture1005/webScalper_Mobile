from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("C:/Users/tirth/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com")
time.sleep(2)

u_i = driver.find_element(by=By.XPATH,value='//*[@id="APjFqb"]')

u_i.send_keys('CampusX')
time.sleep(2)

u_i.send_keys(Keys.ENTER)
time.sleep(20)

link = driver.find_element(by=By.XPATH,value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')
link.click()
time(50)

# link = driver.find_element(by=By.XPATH,value='//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
# link.click()
# time(10)

driver.quit()


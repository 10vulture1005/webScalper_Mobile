from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time

# Setup Chrome driver path (UPDATE THIS PATH)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 ...")  # your UA

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Create driver


# Bypass detection
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
    """
})

# Open the target site
driver.get('https://www.91mobiles.com/list-of-phones/top-performance-phones')
wait = WebDriverWait(driver, 10)

all_html = []

# Keep clicking Load More until it's gone
while True:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Reduced sleep time
        
        all_html.append(driver.page_source)
        
        # Find active "Next" button
        next_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//span[@class="pagination_arrow" and contains(@onclick, "next")]')
        ))
        
        # Scroll button into view and click
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        next_button.click()
        time.sleep(3)  # Wait for content load
        
    except (TimeoutException, ElementClickInterceptedException):
        print("Reached end of pages or button not clickable")
        break
    except Exception as e:
        print(f"Stopping due to: {str(e)}")
        break

# Save combined HTML
with open('mobiles.html', 'w', encoding='utf-8') as f:
    f.write('<html><head><title>Combined Products</title></head><body>')
    f.write('\n'.join(all_html))
    f.write('</body></html>')

print("Done. Saved full page to 'mobiles.html'")
driver.quit()
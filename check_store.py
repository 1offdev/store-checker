from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from notify import pushNotify

STORE_URL = "https://www.apple.com/shop/buy-mac/macbook-air/midnight-apple-m2-chip-with-8-core-cpu-and-10-core-gpu-512gb"

MESSAGE = f"<a href='{STORE_URL}'>Buy NOW!</a>"
PAGE_SCRIPT_VARIABLE = "window.pageLevelData.CTO_BOOTSTRAP"
EXECUTE_SCRIPT = f"return {PAGE_SCRIPT_VARIABLE}"

chrome_service = Service(executable_path="/opt/homebrew/bin/chromedriver")
driver = webdriver.Chrome(service=chrome_service)
driver.get(STORE_URL)

time.sleep(5)

page_data = driver.execute_script(EXECUTE_SCRIPT)
try:
    buyable = page_data["purchaseInfo"]["isBuyable"]
    if buyable is True:
        pushNotify(MESSAGE)
finally:
    driver.quit()

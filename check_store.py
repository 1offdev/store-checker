from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from notify import pushNotify

STORE_URL = "https://www.apple.com/shop/buy-mac/macbook-air/midnight-apple-m2-chip-with-8-core-cpu-and-10-core-gpu-512gb"

USER_AGENT = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

MESSAGE = f"<a href='{STORE_URL}'>Buy NOW!</a>"
PAGE_SCRIPT_VARIABLE = "window.pageLevelData.CTO_BOOTSTRAP"
EXECUTE_SCRIPT = f"return {PAGE_SCRIPT_VARIABLE}"

chrome_service = Service(executable_path="/opt/homebrew/bin/chromedriver")
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument(USER_AGENT)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get(STORE_URL)

page_data = driver.execute_script(EXECUTE_SCRIPT)
try:
    buyable = page_data["purchaseInfo"]["isBuyable"]
    print(buyable)
    if buyable is True:
        pushNotify(MESSAGE)
finally:
    driver.quit()

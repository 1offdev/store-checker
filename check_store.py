from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pushover import push_notify
from twilio_sms import send_sms
import os
from dotenv import load_dotenv

STORE_URL = os.getenv("STORE_URL")

USER_AGENT = "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

MESSAGE_HTML = f"<a href='{STORE_URL}'>Buy NOW!</a>"
MESSAGE_TEXT = f"Buy NOW! {STORE_URL}"

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
        push_notify(MESSAGE_HTML)
        send_sms(MESSAGE_TEXT)
finally:
    driver.quit()

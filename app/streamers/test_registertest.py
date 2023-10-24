# Test for register.html page
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

# driver wait time
wait = WebDriverWait(driver, 60)

driver.get('http://127.0.0.1:8000/')

driver.quit()







from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep
from selenium.webdriver.support.ui import WebDriverWait


# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

print("testing started")
driver = webdriver.Chrome(options=options)
driver.get("https://www.saucedemo.com/")
wait = WebDriverWait(driver, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')

# Get page title
title = driver.title

# Test if title is correct
assert "Swag Labs" in title
print("TEST 0: `title` test passed")

# Close the driver
driver.quit()

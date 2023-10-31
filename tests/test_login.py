from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

def login_page_test(driver, username, password):
    # Find the element with the id "Username Input" and click it
    username_input_element = driver.find_element(By.ID, "id_username")
    username_input_element.click()
    time.sleep(0.5)

    # Send the username to the username input
    username_input_element.send_keys("linus")
    time.sleep(0.5)

    # Find the element with the id "Password Input" and click it
    password_input_element = driver.find_element(By.ID, "id_password")
    password_input_element.click()
    time.sleep(0.5)

    # Send the password to the password input
    password_input_element.send_keys("123")
    time.sleep(0.5)

    # Find the element with the id "Login Submit Button" and click it
    login_submit_button_element = driver.find_element(By.ID, "login")
    login_submit_button_element.click()
    time.sleep(0.5)

    # Wait for the URL to change to the home page URL
    wait.until(EC.url_contains('/'))
    time.sleep(0.5)
    # Check if the URL contains the expected post-login page URL
    if '/login' in driver.current_url:
        print("Login failed")
    else:
        print("Login successful")
# Create a ChromeOptions object with the log level set to 3
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

# Set the wait time for the driver
wait = WebDriverWait(driver, 60)

# Navigate to the homepage
driver.get('http://localhost:8000/login')

# Call the login page test function with appropriate input values
login_page_test(driver, 'linus', '123')  # Replace with actual credentials

# Close the webdriver
driver.quit()

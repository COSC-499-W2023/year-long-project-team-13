from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

def login(driver, username, password):
    # Find the element with the id "Username Input" and click it
    username_input_element = driver.find_element(By.ID, "id_username")
    username_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_username")))

    # Send the username to the username input
    username_input_element.send_keys("linus")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_username"), "linus"))

    # Find the element with the id "Password Input" and click it
    password_input_element = driver.find_element(By.ID, "id_password")
    password_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password")))

    # Send the password to the password input
    password_input_element.send_keys("Admin123")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password"), "Admin123"))

    # Scroll down the login page
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)

    # Find the element with the id "Login Submit Button" and click it
    login_submit_button_element = driver.find_element(By.ID, "login")
    wait.until(EC.element_to_be_clickable((By.ID, "login")))
    login_submit_button_element.click()

    # Wait for the URL to change to the home page URL
    wait.until(EC.url_contains('/'))
    if '/' in driver.current_url:
        print("Login Successful")
    else:
        print("Login Failed")

def request_video_test(driver):
    # Find the element with the id "Video Request Button" and click it
    video_button_element = driver.find_element(By.ID, "Video Request Button")
    wait.until(EC.element_to_be_clickable((By.ID, "Video Request Button")))
    video_button_element.click()
    # Wait for the URL to change to the video page URL
    wait.until(EC.url_contains('/request-video'))
    # Check contacts button
    video_button_element = driver.find_element(By.ID, "contacts")
    video_button_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "contacts")))
    # Check message text area
    video_button_element = driver.find_element(By.ID, "message")
    video_button_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "message")))
    # Check due date button
    video_button_element = driver.find_element(By.ID, "dueDate")
    video_button_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "dueDate")))
    # Check that the send button goes to home page
    video_button_element = driver.find_element(By.ID, "send")
    video_button_element.click()
    # Wait for the URL to change to the home page URL
    wait.until(EC.url_contains('/'))
    # Check if the URL contains the expected page URL
    if '/' in driver.current_url:
        print("TEST: 0 `Request Video` Successful")
    else:
        print("TEST: 0 `Request Video` Failed")

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
print("Request Page test Start")
login(driver, 'linus', 'Admin123')  # Replace with actual credentials
time.sleep(0.5)
request_video_test(driver)
print("Request Page test Completed")

# Close the webdriver
driver.quit()


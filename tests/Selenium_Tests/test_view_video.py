from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os

def login(driver, username, password):
    # Find the element with the id "Username Input" and click it
    username_input_element = driver.find_element(By.ID, "id_username")
    username_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_username")))

    # Send the username to the username input
    username_input_element.send_keys(username)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_username"), username))

    # Find the element with the id "Password Input" and click it
    password_input_element = driver.find_element(By.ID, "id_password")
    password_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password")))

    # Send the password to the password input
    password_input_element.send_keys(password)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password"), password))

    # Scroll down the login page
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)

    # Find the element with the id "Login Submit Button" and click it
    login_submit_button_element = driver.find_element(By.ID, "login")
    login_submit_button_element.click()

    # Wait for the URL to change to the home page URL
    wait.until(EC.url_contains('/'))
    print("Login Successful")

def view_video(driver):
    # click notifications button
    wait.until(EC.presence_of_element_located((By.ID, "Notification-Button")))
    notification_button = driver.find_element(By.ID, "Notification-Button")
    wait.until(EC.element_to_be_clickable((By.ID, "Notification-Button")))
    notification_button.click()
    # Click the video button
    wait.until(EC.url_contains('/notifications'))
    print("TEST: 1 `Notification-Button` Sucessful")

    wait.until(EC.presence_of_element_located((By.ID, "View Video")))
    video_button = driver.find_element(By.ID, "View Video")
    wait.until(EC.element_to_be_clickable((By.ID, "View Video")))
    video_button.click()
    wait.until(EC.url_contains('/video'))
    print("TEST: 2 `View Video From Notifications` Successful")


# Create a ChromeOptions object with the log level set to 3
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--start-maximized")
opt.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.maximize_window()

# Set the wait time for the driver
wait = WebDriverWait(driver, 60)

# Navigate to the homepage
driver.get('http://localhost:8000/login')

# Call the login page test function with appropriate input values
print("View Video Test Start")
login(driver, 'linus', 'Admin123')  # Replace with actual credentials
time.sleep(0.5)
view_video(driver)
print("View Video Test Complete")

# Close the webdriver
driver.quit()

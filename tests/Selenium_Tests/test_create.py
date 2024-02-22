from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
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
    login_submit_button_element.click()

    # Wait for the URL to change to the home page URL
    wait.until(EC.url_contains('/'))
    print("Login Successful")

def create_video_test(driver):
    # Find the element with the id "videos hover" and hover over it
    wait.until(EC.presence_of_element_located((By.ID, "Videos Hover")))
    topbar_element = driver.find_element(By.ID, "Videos Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "Videos Hover")))
    print("TEST: 0 `Videos hover` successful")

    # Find the element with the id "New Video Button" and click it
    video_button_element = driver.find_element(By.ID, "New Video Button")
    wait.until(EC.presence_of_element_located((By.ID, "New Video Button")))
    hover = ActionChains(driver).move_to_element(video_button_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "New Video Button")))
    ActionChains(driver).click(video_button_element).perform()
    # Wait for the URL to change to the video page URL
    wait.until(EC.url_contains('/new/'))
    # Check if the URL contains the expected page URL
    if '/new' in driver.current_url:
        print("TEST: 1 `Create Video` Successful")
    else:
        print("TEST 1: `Create Video` Failed")
        
    # Find the element with the id "start-camera" and click it
    start_camera_element = driver.find_element(By.ID, "start-camera")
    wait.until(EC.element_to_be_clickable((By.ID, "start-camera")))
    start_camera_element.click()
    print("TEST: 2 `Start Camera` Successful")
    
    # Find the element with the id "start-record" and click it
    start_record_element = driver.find_element(By.ID, "start-record")
    wait.until(EC.element_to_be_clickable((By.ID, "start-record")))
    start_record_element.click()
    print("TEST: 3 `Start Record` Successful")
    
    # Find the element with the id "stop-record" and click it
    stop_record_element = driver.find_element(By.ID, "stop-record")
    wait.until(EC.element_to_be_clickable((By.ID, "stop-record")))
    stop_record_element.click()
    print("TEST: 4 `Stop Record` Successful")
    
    # Find the element with the id "next" and click it
    next_element = driver.find_element(By.ID, "next")
    wait.until(EC.element_to_be_clickable((By.ID, "next")))
    next_element.click()
    print("TEST: 5 `Next` Successful")
    
    # Find the element with the id "preview" and click it
    preview_element = driver.find_element(By.ID, "preview")
    wait.until(EC.element_to_be_clickable((By.ID, "preview")))
    preview_element.click()
    print("TEST: 6 `Preview` Successful")
    
    # Find the element with the id "back-details" and click it
    back_details_element = driver.find_element(By.ID, "back-details")
    wait.until(EC.element_to_be_clickable((By.ID, "back-details")))
    back_details_element.click()
    print("TEST: 7 `Back Details` Successful")
    
    # Find the element with the id "back-record" and click it
    back_record_element = driver.find_element(By.ID, "back-record")
    wait.until(EC.element_to_be_clickable((By.ID, "back-record")))
    back_record_element.click()
    print("TEST: 8 `Back Record` Successful")
    
    # Find the element with the id "start-record" and click it
    start_record_element = driver.find_element(By.ID, "start-record")
    wait.until(EC.element_to_be_clickable((By.ID, "start-record")))
    start_record_element.click()
    print("TEST: 9 `Start Record 2` Successful")
    
    # Find the element with the id "stop-record" and click it
    stop_record_element = driver.find_element(By.ID, "stop-record")
    wait.until(EC.element_to_be_clickable((By.ID, "stop-record")))
    stop_record_element.click()
    print("TEST: 10 `Stop Record 2` Successful")
    
    # Find the element with the id "download-video" and click it
    download_video_element = driver.find_element(By.ID, "download-video")
    wait.until(EC.element_to_be_clickable((By.ID, "download-video")))
    download_video_element.click()
    print("TEST: 11 `Download Video` Successful")
    
    # Find the element with the id "next" and click it
    next_element = driver.find_element(By.ID, "next")
    wait.until(EC.element_to_be_clickable((By.ID, "next")))
    next_element.click()
    
    # Find the element with th

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
print("Create Video Test Start")
login(driver, 'linus', 'Admin123')  # Replace with actual credentials
time.sleep(0.5)
create_video_test(driver)
print("Create Video Test Completed")

# Close the webdriver
driver.quit()


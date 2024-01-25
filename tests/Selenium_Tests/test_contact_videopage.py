# create a test for the homepage.html in ../stream/templates/stream/homepage.html using selenium

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

# video page test function
def video_page_test(driver):
    # Find the element with the id "Videos Hover" and hover over it
    wait.until(EC.presence_of_element_located((By.ID, "Videos Hover")))
    topbar_element = driver.find_element(By.ID, "Videos Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "Videos Hover")))
    print("TEST: 0 `Videos hover` successful")
    # Find the element with the id "Video Button" and click it
    video_button_element = driver.find_element(By.ID, "Video Button")
    wait.until(EC.presence_of_element_located((By.ID, "Video Button")))
    hover = ActionChains(driver).move_to_element(video_button_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Video Button")))
    ActionChains(driver).click(video_button_element).perform()

    # Wait for the URL to change to the video page URL
    wait.until(EC.url_contains('/video'))

    # Check if the URL contains the expected video page URL
    if '/video' in driver.current_url:
        print("TEST: 1 `Video page` successful")
    else:
        print("TEST 1: `Video page` failed")

# add contact page test function
def add_contact_page_test(driver):

    # Find the element with the id "Contact Button" and click it
    contact_button_element = driver.find_element(By.ID, "Add Contacts Button")
    contact_button_element.click()

    # Wait for the URL to change to the contact page URL
    wait.until(EC.url_contains('/contact'))

    # Check if the URL contains the expected contact page URL
    if '/contact' in driver.current_url:
        print("TEST 2: `Add contact` successful")
    else:
        print("TEST 2: `Add contact` failed")


# add login page test function
def login_page_test(driver):
    # Find the element with the id "Login Button" and click it
    login_button_element = driver.find_element(By.ID, "Login Button")
    login_button_element.click()

    # Wait for the URL to change to the login page URL
    wait.until(EC.url_contains('/login'))

    # Check if the URL contains the expected login page URL
    if '/login' in driver.current_url:
        print("Login successful")
    else:
        print("Login failed")



# login to the page
def login(driver):
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
    print("fully logged in")

def add_contact_page_search_test(driver):
    # Find the element with the id "Contact Button" and click it
    contact_button_element = driver.find_element(By.ID, "search button")
    contact_button_element.click()

    # Wait for the URL to change to the contact page URL
    wait.until(EC.url_contains('/video'))

    # Check if the URL contains the expected contact page URL
    if '/video' in driver.current_url:
        print("TEST 3: `Add contact search` successful")
    else:
        print("TEST 3: `Add contact search` failed")
# Create a ChromeOptions object with the log level set to 3
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

# Set the wait time for the driver
wait = WebDriverWait(driver, 60)

# Navigate to the homepage
driver.get('http://localhost:8000')

# Call the video page test function
print("Contact Video Page Test Start")
login_page_test(driver)
login(driver)
video_page_test(driver)
add_contact_page_test(driver)
add_contact_page_search_test(driver)
print("Contact Video Page Test Completed")

# close the webdriver
driver.quit()

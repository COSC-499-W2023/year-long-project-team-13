from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

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

# test hover over topbar
def topbar_videos_hover_test(driver):

    # Find the element with the id "Topbar" and hover over it
    wait.until(EC.presence_of_element_located((By.ID, "Videos Hover")))
    topbar_element = driver.find_element(By.ID, "Videos Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "Videos Hover")))
    if EC.presence_of_element_located((By.ID, "Videos Hover")):
        print("TEST: 0 `Videos hover` successful")
    viewvideos_element = driver.find_element(By.ID, "Video Button")
    wait.until(EC.presence_of_element_located((By.ID, "Video Button")))
    hover = ActionChains(driver).move_to_element(viewvideos_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Video Button")))
    ActionChains(driver).click(viewvideos_element).perform()
    if(driver.current_url == "http://localhost:8000/videos/"):
        print("TEST: 1 `Videos click` successful")

def topbar_user_hover_test(driver):
    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 2 `User hover` successful")

# Create a ChromeOptions object with the log level set to 3
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

# Set the wait time for the driver
wait = WebDriverWait(driver, 10)

# Navigate to the homepage
driver.get('http://localhost:8000/login')

print("Topbar test Start")
login(driver)
time.sleep(0.5)
topbar_videos_hover_test(driver)
time.sleep(0.5)
topbar_user_hover_test(driver)
print("Topbar test Completed")

# close the webdriver
driver.quit()

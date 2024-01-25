from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

def login_page_test(driver, username, password):
    wait.until(EC.url_contains('/login'))
    # Find the element with the id "Username Input" and click it
    username_input_element = driver.find_element(By.ID, "id_username")
    username_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_username")))


    # Send the username to the username input
    username_input_element.send_keys(username)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_username"), "linus"))

    # Find the element with the id "Password Input" and click it
    password_input_element = driver.find_element(By.ID, "id_password")
    password_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password")))

    # Send the password to the password input
    password_input_element.send_keys(password)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password"), "123"))

    # Scroll down the login page
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)

    # Find the element with the id "Login Submit Button" and click it
    login_submit_button_element = driver.find_element(By.ID, "login")
    wait.until(EC.element_to_be_clickable((By.ID, "login")))
    login_submit_button_element.click()

    # Wait for the URL to change to the home page URL
    WebDriverWait(driver, 60).until(EC.url_contains('/'))

    # Check if the URL contains the expected post-login page URL
    if '/login' in driver.current_url:
        print("Login failed")
    else:
        print("Login successful")

def admin_test(driver, username, password):
    # Call the login page test function
    login_page_test(driver, username, password)
    time.sleep(0.5)

    # Find the element with the id "Topbar" and hover over it
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 0 `User hover` successful")

    # Find the element with the id "Admin Button" and click it
    admin_element = driver.find_element(By.ID, "Admin Button")
    wait.until(EC.presence_of_element_located((By.ID, "Admin Button")))
    hover = ActionChains(driver).move_to_element(admin_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Admin Button")))
    ActionChains(driver).click(admin_element).perform()

    # Wait for the URL to change to the admin page URL
    wait.until(EC.url_contains('/admin'))

    # Check if the URL contains the expected profile page URL
    if '/admin' in driver.current_url:
        print("TEST: 1 `Admin` successful")
    else:
        print("TEST: 1 `Admin` failed")

    # Wait for the profile page to load
    # WebDriverWait(driver, 60).until(EC.url_contains('/profile'))

    # Check if the profile page elements are present and correct
    #assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[src*='user.profile.image.url']")))
    #assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "username"), username))
    #assert WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.ID, "email"), email))

# Create a ChromeOptions object with the log level set to 3
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 60)

# Call the profile page test function with appropriate input values
driver.get('http://localhost:8000/login')
print("Admin Page test Start")
admin_test(driver, 'linus', 'Admin123')
time.sleep(0.5)
print("Admin Page test Completed")

# Close the webdriver
driver.quit()

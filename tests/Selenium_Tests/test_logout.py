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

def logout_test(driver, username, password):
    # Call the login page test function
    login_page_test(driver, username, password)
    time.sleep(0.5)

    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 0 `User hover` successful")
    # Find the element with the id "Logout Button" and click it
    logout_element = driver.find_element(By.ID, "Logout Button")
    wait.until(EC.presence_of_element_located((By.ID, "Logout Button")))
    hover = ActionChains(driver).move_to_element(logout_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Logout Button")))
    ActionChains(driver).click(logout_element).perform()
    wait.until(EC.url_contains('/#'))
    # Cancel logout
    logout_confirm_element = driver.find_element(By.ID, "cancel")
    logout_confirm_element.click()

    # Wait for the URL to change to the home page URL
    wait.until(EC.url_contains('/'))
    # Find the element with the id "User Hover" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 1 `User hover` successful")
    # Find the element with the id "Logout Button" and click it
    logout_element = driver.find_element(By.ID, "Logout Button")
    wait.until(EC.presence_of_element_located((By.ID, "Logout Button")))
    hover = ActionChains(driver).move_to_element(logout_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Logout Button")))
    ActionChains(driver).click(logout_element).perform()
    wait.until(EC.url_contains('/#'))
    # Confirm logout
    logout_confirm_element = driver.find_element(By.ID, "logout")
    logout_confirm_element.click()

    # Wait for the URL to change to the logout page URL
    wait.until(EC.url_contains('/logout'))

    # Check if the URL contains the expected logout page URL
    if '/logout' in driver.current_url:
        print("TEST: 2 `Logout` successful")
    else:
        print("TEST: 2 `Logout` failed")

# Create a ChromeOptions object with the log level set to 3
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 60)

# Call the profile page test function with appropriate input values
print("Logout test Start")
driver.get('http://localhost:8000/login')
logout_test(driver, 'linus', 'Admin123')
print("Logout test Completed")

# Close the webdriver
driver.quit()

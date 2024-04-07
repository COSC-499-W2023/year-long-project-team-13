from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait



def register_page_test(driver, username, email, password, permission, security, answer):
    html = driver.find_element(By.TAG_NAME, "html")

    # Find the username, email, and password fields and fill them out
    username_element = driver.find_element(By.ID, "id_username")
    username_element.send_keys(username)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_username"), username))

    email_element = driver.find_element(By.ID, "id_email")
    email_element.send_keys(email)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_email"), email))

    password1_element = driver.find_element(By.ID, "id_password1")
    password1_element.send_keys(password)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password1"), password))

    eye_icon_elements = driver.find_elements(By.CLASS_NAME, "toggle-password")
    for eye_icon in eye_icon_elements:
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "toggle-password")))
    eye_icon.click()

    password2_element = driver.find_element(By.ID, "id_password2")
    password2_element.send_keys(password)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password2"), password))

    # Scroll down the register page
    html.send_keys(Keys.PAGE_DOWN)

    # Find the permission dropdown and select the appropriate permission
    permission_element = Select(driver.find_element(By.NAME, "permission"))
    # wait.until(EC.element_to_be_clickable((By.ID, "id_permission")))
    # permission_element.click()
    permission_element.select_by_value(permission)

    security_element = Select(driver.find_element(By.NAME, "security_question"))
    # wait.until(EC.element_to_be_clickable((By.ID, "id_permission")))
    # permission_element.click()
    security_element.select_by_value(security)

    security_answer_element = driver.find_element(By.ID, "id_security_answer")
    wait.until(EC.element_to_be_clickable((By.ID, "id_security_answer")))
    security_answer_element.click()
    security_answer_element.send_keys(answer)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_security_answer"), answer))

     # Find the checkbox and click it
    checkbox_element = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox']")))
    checkbox_element.click()
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))

    html.send_keys(Keys.END)

    # Submit the form by clicking the "Register" button
    register_button = driver.find_element(By.ID, "register")
    wait.until(EC.element_to_be_clickable((By.ID, "register")))
    register_button.click()

    # Wait for the registration to complete (you might need to adjust the wait time)
    # wait.until(EC.url_contains('/register'))
    wait.until(EC.url_contains('/login'))

    # Check if the URL contains the expected login page URL
    if '/register' in driver.current_url:
        print("TEST: 0 `Registration` failed")
    else:
        print("TEST: 0 `Registration` successful")

# Create a ChromeOptions object with the log level set to 3
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

# Set the wait time for the driver
wait = WebDriverWait(driver, 60)  # Adjust the wait time as needed

# Navigate to the registration page
driver.get('http://localhost:8000/register/')  # Update the URL if needed

# Call the register page test function with appropriate input values
print("Register Page test Start")
register_page_test(driver, 'WannaBe', 'raymond@email.com', 'herman1234', "1", "2", "canada")
print("Register Page test end for permission 1")
time.sleep(0.5)
driver.get('http://localhost:8000/register/')  # Update the URL if needed
register_page_test(driver, 'abcdef', 'abcdef@email.com', 'herman1234', "2", "1", "canada")
print("Register Page test end for permission 2")
print("Register Page test End")

# Close the webdriver
driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import time

def reset_password_page_test(driver, email, username, answer, password):
    # Scroll down the login page

    # Find the element with the id "Email Input" and click it

    wait.until(EC.url_contains('/login'))
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    forgot_password_button = driver.find_element(By.ID, "forgot-password-btn")
    wait.until(EC.visibility_of_element_located((By.ID, "forgot-password-btn")))
    forgot_password_button.click()

    wait.until(EC.url_contains('/forget-password'))
    if '/forget-password' in driver.current_url:
        print("TEST 1: `Forget Password Page` successful")
    else:
        print("TEST 1: `Forget Password Page` failed")

    # Find the element with id_username and click it
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    username_input_element = driver.find_element(By.ID, "id_username")
    wait.until(EC.element_to_be_clickable((By.ID, "id_username")))
    username_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_username")))

    # Send the username to the username input
    username_input_element.send_keys("testing")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_username"), "testing"))

    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)

    # Find the element with the id "id_email" and click it
    email_input_element = driver.find_element(By.ID, "id_email")
    email_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_email")))

    # Send the email to the email input
    email_input_element.send_keys("testing2@gmail.com")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_email"), "testing2@gmail.com"))

    submit_button = driver.find_element(By.ID, "email-username-submit")
    wait.until(EC.element_to_be_clickable((By.ID, "email-username-submit")))
    submit_button.click()

    wait.until(EC.url_contains('/forget-password'))
    if '/forget-password' in driver.current_url:
        print("TEST 2: `Bad Username/Email` successful")
    else:
        print("TEST 2: `Bad Username/Email` failed")

    # Find the element with id_username and click it
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    username_input_element = driver.find_element(By.ID, "id_username")
    username_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_username")))

    # Send the username to the username input
    username_input_element.send_keys(username)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_username"), username))

    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)

    # Find the element with the id "id_email" and click it
    email_input_element = driver.find_element(By.ID, "id_email")
    email_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_email")))

    # Send the email to the email input
    email_input_element.send_keys(email)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_email"), email))

    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)

    submit_button = driver.find_element(By.ID, "email-username-submit")
    wait.until(EC.element_to_be_clickable((By.ID, "email-username-submit")))
    submit_button.click()

    wait.until(EC.url_contains('/security-answer'))
    if '/security-answer' in driver.current_url:
        print("TEST 3: `Good Username/Email` successful")
    else:
        print("TEST 3: `Good Username/Email` failed")

    # Find the element with the id "security_answer" and click it
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    security_answer_input_element = driver.find_element(By.ID, "security_answer")
    wait.until(EC.element_to_be_clickable((By.ID, "security_answer")))
    security_answer_input_element.click()
    security_answer_input_element.send_keys("testing")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "security_answer"), "testing"))

    submit_button = driver.find_element(By.ID, "security-answer-submit")
    submit_button.click()

    wait.until(EC.url_contains('/security-answer'))
    if '/security-answer' in driver.current_url:
        print("TEST 4: `Bad Security Answer` successful")
    else:
        print("TEST 4: `Bad Security Answer` failed")

    # Find the element with the id "security_answer" and click it
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    security_answer_input_element = driver.find_element(By.ID, "security_answer")
    wait.until(EC.element_to_be_clickable((By.ID, "security_answer")))
    security_answer_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "security_answer")))
    security_answer_input_element.send_keys(answer)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "security_answer"), answer))

    submit_button = driver.find_element(By.ID, "security-answer-submit")
    submit_button.click()

    wait.until(EC.url_contains('/password_reset_done'))
    if '/password_reset_done' in driver.current_url:
        print("TEST 5: `Good Security Answer` successful")
    else:
        print("TEST 5: `Good Security Answer` failed")

    # Find the element with the id "id_password" and click it
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    password_input_element = driver.find_element(By.ID, "id_password")
    wait.until(EC.element_to_be_clickable((By.ID, "id_password")))
    password_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password")))
    password_input_element.send_keys("password")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password"), "password"))

    # Find the element with the id "id_password2" and click it
    confirm_password_input_element = driver.find_element(By.ID, "id_password2")
    wait.until(EC.element_to_be_clickable((By.ID, "id_password2")))
    confirm_password_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password2")))
    confirm_password_input_element.send_keys("2password")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password2"), "2password"))

    # Find the element with the id "password-reset-submit" and click it
    submit_button = driver.find_element(By.ID, "password-reset-submit")
    wait.until(EC.element_to_be_clickable((By.ID, "password-reset-submit")))
    submit_button.click()

    wait.until(EC.url_contains('/password_reset_done'))
    if '/password_reset_done' in driver.current_url:
        print("TEST 6: `Bad Password Reset` successful")
    else:
        print("TEST 6: `Bad Password Reset` failed")

    # Find the element with the id "id_password" and click it
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    password_input_element = driver.find_element(By.ID, "id_password")
    wait.until(EC.element_to_be_clickable((By.ID, "id_password")))
    password_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password")))
    password_input_element.send_keys(password)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password"), password))

    # Find the element with the id "id_password2" and click it
    confirm_password_input_element = driver.find_element(By.ID, "id_password2")
    wait.until(EC.element_to_be_clickable((By.ID, "id_password2")))
    confirm_password_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password2")))
    confirm_password_input_element.send_keys(password)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password2"), password))

    # Find the element with the id "password-reset-submit" and click it
    submit_button = driver.find_element(By.ID, "password-reset-submit")
    wait.until(EC.element_to_be_clickable((By.ID, "password-reset-submit")))
    submit_button.click()

    wait.until(EC.url_contains('/login'))
    if '/login' in driver.current_url:
        print("TEST 7: `Good Password Reset` successful")
    else:
        print("TEST 7: `Good Password Reset` failed")


def login_test(driver, username, password):
    # Find the element with the id "Username Input" and click it
    wait.until(EC.url_contains('/login'))
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

    # Find the eye icon and click it
    eye_icon_element = driver.find_element(By.CLASS_NAME, "toggle-password")
    eye_icon_element.click()

    # Scroll down the login page
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)

    # Find the element with the id "Login Submit Button" and click it
    login_submit_button_element = driver.find_element(By.ID, "login")
    wait.until(EC.element_to_be_clickable((By.ID, "login")))
    login_submit_button_element.click()

    # Wait for the URL to change to the home page URL
    wait.until(EC.url_contains('/'))

    # Check if the URL contains the homepage
    if '/login' in driver.current_url:
        print("TEST 8: `Login` failed Did not go home")
    else:
        print("TEST 8: `Login` successful")

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
print("Reset Password Page test Start")
# test call here
reset_password_page_test(driver, "raymond@email.com", "WannaBe", "canada", "django123")
time.sleep(0.5)
login_test(driver, "WannaBe", "django123")
print("Reset Password Page test Completed")

# Close the webdriver
driver.quit()

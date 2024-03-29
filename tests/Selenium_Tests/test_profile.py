from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
# Get absolute path from relative path image
import os
import sys


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
    login_submit_button_element.click()

    # Wait for the URL to change to the home page URL
    WebDriverWait(driver, 60).until(EC.url_contains('/'))

    # Check if the URL contains the expected post-login page URL
    if '/login' in driver.current_url:
        print("Login failed")
    else:
        print("Login successful")

def profile_page_test(driver, username, password, firstName, lastName, email, birthyear, birthdate, image, firstName_set, lastName_set, email_set, birthyear_set, birthdateset):
    # Call the login page test function
    login_page_test(driver, username, password)
    time.sleep(0.5)

    # Navigate to the profile page
    # driver.get('http://localhost:8000/profile')

    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 0 `User hover` successful")

    # Find the element with the id "Profile Button" and click it
    profile_button_element = driver.find_element(By.ID, "Profile Button")
    wait.until(EC.presence_of_element_located((By.ID, "Profile Button")))
    hover = ActionChains(driver).move_to_element(profile_button_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Profile Button")))
    ActionChains(driver).click(profile_button_element).perform()

    # Wait for the URL to change to the profile page URL
    wait.until(EC.url_contains('/profile'))
    print("TEST: 1 `Profile page found` successful")

    firstName_element = driver.find_element(By.ID, "id_first_name")
    firstName_element.clear()
    firstName_element.send_keys(firstName_set)
    firstName_value_input = firstName_element.get_attribute('value')
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_first_name"), firstName_set))
    print("TEST: 2 `First Name input` successful")

    lastName_element = driver.find_element(By.ID, "id_last_name")
    lastName_element.clear()
    lastName_element.send_keys(lastName_set)
    lastName_value_input = lastName_element.get_attribute('value')
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_last_name"), lastName_set))
    print("TEST: 3 `Last Name input` successful")

    email_element = driver.find_element(By.ID, "id_email")
    email_element.clear()
    email_element.send_keys(email_set)
    email_value_input = email_element.get_attribute('value')
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_email"), email_set))
    print("TEST: 4 `Email input` successful")

    birthdate_element = driver.find_element(By.ID, "id_birthdate")
    birthdate_element.clear()
    birthdate_element.send_keys(birthyear_set)
    time.sleep(0.5)
    birthdate_element.send_keys(Keys.TAB)
    birthdate_element.send_keys(birthdateset)
    birthdate_value_input = birthdate_element.get_attribute('value')
    time.sleep(0.5)
    print("TEST: 5 `Birthdate input` successful")

    uploadImg = driver.find_element(By.ID, "id_image")
    uploadImg.send_keys(image)
    time.sleep(0.5)

    update_button = driver.find_element(By.ID, "update")
    update_button.click()

    wait.until(EC.url_contains('/profile'))

    firstName_value_check = driver.find_element(By.ID, "id_first_name").get_attribute('value')

    lastName_value_check = driver.find_element(By.ID, "id_last_name").get_attribute('value')

    email_value_check = driver.find_element(By.ID, "id_email").get_attribute('value')

    birthdate_value_check = driver.find_element(By.ID, "id_birthdate").get_attribute('value')

    # .text.lower()

    name_display_value_check = driver.find_element(By.ID, "NameCheck").text
    print("TEST: 6 `name check` successful")

    email_display_value_check = driver.find_element(By.ID, "EmailCheck").text
    print("TEST: 7 `email check` successful")

    birthdate_display_value_check = driver.find_element(By.ID, "BirthdateCheck").text
    print("TEST: 8 `birthdate check` successful")

    img_check = driver.find_element(By.TAG_NAME, "img").get_attribute('src')
    print("TEST: 9 `image check` successful")

    firstName_element = driver.find_element(By.ID, "id_first_name")
    firstName_element.clear()
    firstName_element.send_keys(firstName)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_first_name"), firstName))

    lastName_element = driver.find_element(By.ID, "id_last_name")
    lastName_element.clear()
    lastName_element.send_keys(lastName)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_last_name"), lastName))

    email_element = driver.find_element(By.ID, "id_email")
    email_element.clear()
    email_element.send_keys(email)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_email"), email))

    birthdate_element = driver.find_element(By.ID, "id_birthdate")
    birthdate_element.clear()
    birthdate_element.send_keys(birthyear)
    birthdate_element.send_keys(Keys.TAB)
    birthdate_element.send_keys(birthdate)
    time.sleep(0.5)

    update_button = driver.find_element(By.ID, "update")
    update_button.click()

    wait.until(EC.url_contains('/profile'))

    # Check if the URL contains the expected profile page URL
    if '/profile' in driver.current_url:
        if firstName_value_check == firstName_value_input and lastName_value_check == lastName_value_input and email_value_check == email_value_input and birthdate_value_check == birthdate_value_input and 'mountain' in img_check and '.jpg' in img_check and email_display_value_check == email_value_check and name_display_value_check == (firstName_value_check + " " + lastName_value_check):
            print("TEST: 10 `Edit Profile` successful")
        else:
            print("TEST: 10 `Edit Profile` failed")
    else:
        print("TEST: 10 `Edit Profile` failed")

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

# File file = new File("src/test/resources/testData/twt_Pic.jpg")
# yourElement.sendKeys(file.getAbsolutePath())
# projectpath = System.getProperty("user.dir")

# print( os.path.abspath('..\\drivers\\chromedriver_v78.0.exe') )

# Call the profile page test function with appropriate input values
print("Profile Page test Start")
driver.get('http://localhost:8000/login')
profile_page_test(driver, 'adrian', 'cclemon0912', 'Adrian', 'Fong', 'af@student.com','2024', '0118', os.path.abspath('../../app/media/mountain.jpg'), 'Test First Name', 'Test Last Name', 'admin@xyz.com','2000', '1225')
print("Profile Page test Completed")

# Close the webdriver
driver.quit()

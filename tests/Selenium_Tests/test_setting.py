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
    login_submit_button_element.click()

    # Wait for the URL to change to the home page URL
    WebDriverWait(driver, 30).until(EC.url_contains('/'))
    # Check if the URL contains the expected post-login page URL
    if '/login' in driver.current_url:
        print("Login failed")
    else:
        print("Login successful")

def profileChangePassword(driver):
    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 0 `User hover` successful")

    # Find the element with the id "Setting Button" and click it
    profile_element = driver.find_element(By.ID, "Profile Button")
    wait.until(EC.presence_of_element_located((By.ID, "Profile Button")))
    hover = ActionChains(driver).move_to_element(profile_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Setting Button")))
    ActionChains(driver).click(profile_element).perform()

    # Find the element with the id "Login Submit Button" and click it
    change_password_button_element = driver.find_element(By.ID, "change password")
    change_password_button_element.click()

    if '/setting' in driver.current_url:
        print("TEST: 1 Change Password redirect successful")
    else:
        print("TEST: 1 Change Password redirect failed")


def setting_test(driver, username, password, newpassword):
    # Call the login page test function
    login_page_test(driver, username, password)
    time.sleep(0.5)

    profileChangePassword(driver)
    time.sleep(0.5)

    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 2 `User hover` successful")

    # Find the element with the id "Setting Button" and click it
    setting_element = driver.find_element(By.ID, "Setting Button")
    wait.until(EC.presence_of_element_located((By.ID, "Setting Button")))
    hover = ActionChains(driver).move_to_element(setting_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Setting Button")))
    ActionChains(driver).click(setting_element).perform()

    oldpassword_input_element = driver.find_element(By.ID, "id_oldpassword")
    oldpassword_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_oldpassword")))

    print("Test 1 : oldpassword successful")

    password_input_element = driver.find_element(By.ID, "id_password")
    password_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password")))

    print("Test 2 : newpassword successful")

    # Scroll down the page
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)

    time.sleep(0.5)

    password2_input_element = driver.find_element(By.ID, "id_password2")
    password2_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password2")))

    print("Test 3 : confirmpassword successful")

    wait.until(EC.visibility_of_element_located((By.ID, "Save")))
    wait.until(EC.presence_of_element_located((By.ID, "Save")))
    save_input_element = driver.find_element(By.ID, "Save")
    wait.until(EC.element_to_be_clickable((By.ID, "Save")))
    save_input_element.click()

    print("Test 4 : Save successful")

    wait.until(EC.visibility_of_element_located((By.ID, "Update")))
    wait.until(EC.presence_of_element_located((By.ID, "Update")))
    update_input_element = driver.find_element(By.ID, "Update")
    wait.until(EC.element_to_be_clickable((By.ID, "Update")))
    update_input_element.click()

    print("Test 5 : Update successful")

    wait.until(EC.visibility_of_element_located((By.ID, "Reset")))
    wait.until(EC.presence_of_element_located((By.ID, "Reset")))
    reset_input_element = driver.find_element(By.ID, "Reset")
    wait.until(EC.element_to_be_clickable((By.ID, "Reset")))
    reset_input_element.click()

    print("Test 6 : Reset successful")

    wait.until(EC.visibility_of_element_located((By.ID, "Save")))
    wait.until(EC.presence_of_element_located((By.ID, "Save")))
    save_input_element = driver.find_element(By.ID, "Save")
    wait.until(EC.element_to_be_clickable((By.ID, "Save")))
    save_input_element.click()

    print("Test 7 : Save successful")

    wait.until(EC.visibility_of_element_located((By.ID, "Cancel")))
    wait.until(EC.presence_of_element_located((By.ID, "Cancel")))
    cancel_input_element = driver.find_element(By.ID, "Cancel")
    wait.until(EC.element_to_be_clickable((By.ID, "Cancel")))
    cancel_input_element.click()

    print("Test 8 : Cancel successful")

    oldpassword_input_element = driver.find_element(By.ID, "id_oldpassword")
    oldpassword_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_oldpassword")))

    oldpassword_input_element.send_keys(password)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_oldpassword"), password))

    print("oldpassword filled successfully")

    password_input_element = driver.find_element(By.ID, "id_password")
    password_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password")))

    password_input_element.send_keys(newpassword)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password"), newpassword))

    print("newpassword filled successfully")

    # Scroll down the page
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)

    time.sleep(0.5)

    password2_input_element = driver.find_element(By.ID, "id_password2")
    password2_input_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_password2")))

    password2_input_element.send_keys(newpassword)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_password2"), newpassword))

    print("confirmpassword filled successfully")

    wait.until(EC.visibility_of_element_located((By.ID, "Save")))
    wait.until(EC.presence_of_element_located((By.ID, "Save")))
    save_input_element = driver.find_element(By.ID, "Save")
    wait.until(EC.element_to_be_clickable((By.ID, "Save")))
    save_input_element.click()

    print("Save successful")

    wait.until(EC.visibility_of_element_located((By.ID, "Update")))
    wait.until(EC.presence_of_element_located((By.ID, "Update")))
    update_input_element = driver.find_element(By.ID, "Update")
    wait.until(EC.element_to_be_clickable((By.ID, "Update")))
    update_input_element.click()

    print("Update successful")

    # Wait for the URL to change to the admin page URL
    wait.until(EC.url_contains('/login'))

    # Check if the URL contains the expected profile page URL
    if '/login' in driver.current_url:
        print("TEST: 9 `Setting` successful")
    else:
        print("TEST: 9 `Setting` failed")


# Create a ChromeOptions object with the log level set to 3
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 60)

# Call the profile page test function with appropriate input values
print("Setting Page test Start")
driver.get('http://localhost:8000/login')
time.sleep(0.5)
setting_test(driver, 'adrian', 'cclemon0912', 'bigproject5')
setting_test(driver, 'adrian', 'bigproject5' , 'cclemon0912')
print("Setting Page test Completed")

# Close the webdriver
driver.quit()

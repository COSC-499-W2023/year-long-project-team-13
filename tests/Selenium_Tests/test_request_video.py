from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
# For selecting dropdown username
from selenium.webdriver.support.select import Select

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

    # Find the element with the id "Login Submit Button" and click it
    login_submit_button_element = driver.find_element(By.ID, "login")
    wait.until(EC.element_to_be_clickable((By.ID, "login")))
    login_submit_button_element.click()

    # Wait for the URL to change to the home page URL
    wait.until(EC.url_contains('/'))
    if '/' in driver.current_url:
        print("Login Successful")
    else:
        print("Login Failed")

def logout(driver, location):

    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("`User hover` successful")
    # Find the element with the id "Logout Button" and click it
    logout_element = driver.find_element(By.ID, "Logout Button")
    wait.until(EC.presence_of_element_located((By.ID, "Logout Button")))
    hover = ActionChains(driver).move_to_element(logout_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Logout Button")))
    ActionChains(driver).click(logout_element).perform()
    wait.until(EC.url_contains(location))

    # Confirm logout
    logout_confirm_element = driver.find_element(By.ID, "logout")
    wait.until(EC.presence_of_element_located((By.ID, "logout")))
    logout_confirm_element.click()

    # Wait for the URL to change to the logout page URL
    wait.until(EC.url_contains('/logout'))

    # Check if the URL contains the expected logout page URL
    if '/logout' in driver.current_url:
        print("`Logout` successful")
    else:
        print("`Logout` failed")

def hoverTest(hoverButton, buttonID, location, message):

    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, hoverButton)
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, hoverButton)))
    print("`Video hover` successful")

    # Find the element with the buttonID and click it
    hover_button_element = driver.find_element(By.ID, buttonID)
    wait.until(EC.presence_of_element_located((By.ID, buttonID)))
    hover = ActionChains(driver).move_to_element(hover_button_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, buttonID)))
    ActionChains(driver).click(hover_button_element).perform()

    wait.until(EC.url_contains(location))

    # Check if the URL contains the expected notification page URL
    if location in driver.current_url:
        print(message + " successful")
    else:
        print(message + " failed")

# Send video request test function for sender
def request_video_test(driver, description, dueDateYear, dueDateMonthDay, dueDateTime):
    # Find the element with the id "Topbar" and hover over it
    hoverTest("Videos Hover","Video Request Button", '/request-video', "`Video Request page found`")

    # Check receiver button
    receiver_button_element = driver.find_element(By.ID, "id_receiver")
    receiver_button_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_receiver")))
    # Select username "adrian"
    usernameSelect = Select(receiver_button_element)
    usernameSelect.select_by_index(1)

    # Check description text area
    description_button_element = driver.find_element(By.ID, "id_description")
    description_button_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_description")))
    description_button_element.send_keys(description)
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_description"), description))


    # Check due date button
    dueDate_button_element = driver.find_element(By.ID, "id_due_date")
    dueDate_button_element.click()
    wait.until(EC.presence_of_element_located((By.ID, "id_due_date")))
    dueDate_button_element.send_keys(dueDateTime)
    time.sleep(0.5)
    dueDate_button_element.send_keys(Keys.TAB)
    dueDate_button_element.send_keys(dueDateYear)
    dueDate_button_element.send_keys(dueDateMonthDay)
    time.sleep(0.5)

    # Check that the send button goes to notification page
    send_button_element = driver.find_element(By.ID, "send")
    send_button_element.click()

    # Wait for the URL to change to the notification page URL
    wait.until(EC.url_contains('/notifications'))

    # Check if the URL contains the expected page URL
    if '/notifications' in driver.current_url:
        print("TEST: 0 `Request Video` Successful")
    else:
        print("TEST: 0 `Request Video` Failed")

# Remove video request test function on sender
def remove_request_video_test(driver, description, dueDateYear, dueDateMonthDay, dueDateTime):
    # Find the remove video request button
    remove_video_request_button = wait.until(EC.presence_of_element_located((By.ID, "delete video request button")))

    # Click the remove video request button
    remove_video_request_button.click()

    # Wait for the URL to change to the notification page URL
    wait.until(EC.url_contains('/notifications'))

    # Check if the URL contains the expected notification page URL
    if '/notifications' in driver.current_url:
        print("TEST 1: `Remove Video Request` successful")
    else:
        print("TEST 1: `Remove Video Request` Failed")

    request_video_test(driver, description, dueDateYear, dueDateMonthDay, dueDateTime)

    logout(driver, '/notifications#')

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
print("Request Page test Start")
login(driver, 'linus', 'Admin123')  # Replace with actual credentials
time.sleep(0.5)
request_video_test(driver, "request video description testing", "2024", "0101", "1000AM")
remove_request_video_test(driver, "request video description testing", "2024", "0101", "1000AM")
print("Request Page test Completed")

# Close the webdriver
driver.quit()


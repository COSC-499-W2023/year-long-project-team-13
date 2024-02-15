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
    login_submit_button_element.click()

    # Wait for the URL to change to the home page URL
    WebDriverWait(driver, 60).until(EC.url_contains('/'))

    # Check if the URL contains the expected post-login page URL
    if '/login' in driver.current_url:
        print("Login failed")
    else:
        print("Login successful")


# add contact page (friend search) (friend request send) test function
def add_contact_page_search_and_friend_request_test(driver, username, password):

    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 0 `User hover` successful")

    # Find the element with the id "Add Contacts Button" and click it
    add_contacts_button_element = driver.find_element(By.ID, "Add Contacts Button")
    wait.until(EC.presence_of_element_located((By.ID, "Add Contacts Button")))
    hover = ActionChains(driver).move_to_element(add_contacts_button_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Add Contacts Button")))
    ActionChains(driver).click(add_contacts_button_element).perform()

    # Wait for the URL to change to the contact page URL
    wait.until(EC.url_contains('/contact'))
    print("TEST: 1 `Add Contact page found` successful")

    # Find the search input field and submit button
    search_input = wait.until(EC.presence_of_element_located((By.NAME, "search")))
    search_button = wait.until(EC.presence_of_element_located((By.ID, "search button")))

    # Enter a search query and click the search button
    search_input.send_keys("adrian")  # replace "test" with your actual search query
    search_button.click()
    print("TEST 2: `Add contact search` successful")

    # Wait until the first add contact button is clickable
    first_add_contact_button = wait.until(EC.element_to_be_clickable((By.ID, "add contact button")))

    # Click the first add contact button
    first_add_contact_button.click()

    # Wait for the URL to change to the notification page URL
    wait.until(EC.url_contains('/notifications'))

    # Check if the URL contains the expected notification page URL
    if '/notifications' in driver.current_url:
        print("TEST 3: `Friend Request sent` successful")
    else:
        print("TEST 3: `Friend Request sent` failed")


# Remove friend request test function for sender
def remove_friend_request_test(driver, username, password):

    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 0 `User hover` successful")

    # Find the element with the id "Notification Button" and click it
    notification_button_element = driver.find_element(By.ID, "Notification Button")
    wait.until(EC.presence_of_element_located((By.ID, "Notification Button")))
    hover = ActionChains(driver).move_to_element(notification_button_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Notification Button")))
    ActionChains(driver).click(notification_button_element).perform()

    # Check if the URL contains the expected notification page URL
    if '/notifications' in driver.current_url:
        print("TEST 1: `Notifications` successful")
    else:
        print("TEST 1: `Notifications` failed")

    # Find the remove friend request button
    remove_friend_request_button = wait.until(EC.presence_of_element_located((By.ID, "delete friend request button")))

    # Click the remove friend request button
    remove_friend_request_button.click()

    # Wait for the URL to change to the notification page URL
    wait.until(EC.url_contains('/notifications'))

    # Check if the URL contains the expected notification page URL
    if '/notifications' in driver.current_url:
        print("TEST 2: `Remove Friend Request` successful")
    else:
        print("TEST 2: `Remove Friend Request` successful")

# logout function
def logout(driver, username, password):

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

    # click login again button
    login_again_element = driver.find_element(By.ID, "btn")
    login_again_element.click()

    # Wait for the URL to change to the logout page URL
    wait.until(EC.url_contains('/login'))

    # Check if the URL contains the expected logout page URL
    if '/login' in driver.current_url:
        print("TEST: 3 `Login again` successful")
    else:
        print("TEST: 3 `Login again` failed")

# Reject friend request test function for receiver
def reject_friend_request_test(driver, username, password):

    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 0 `User hover` successful")

    # Find the element with the id "Notification Button" and click it
    notification_button_element = driver.find_element(By.ID, "Notification Button")
    wait.until(EC.presence_of_element_located((By.ID, "Notification Button")))
    hover = ActionChains(driver).move_to_element(notification_button_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Notification Button")))
    ActionChains(driver).click(notification_button_element).perform()

    # Check if the URL contains the expected notification page URL
    if '/notifications' in driver.current_url:
        print("TEST 1: `Notifications` successful")
    else:
        print("TEST 1: `Notifications` failed")

    # Find the reject friend request button
    reject_friend_request_button = wait.until(EC.presence_of_element_located((By.ID, "reject friend request button")))

    # Click the reject friend request button
    reject_friend_request_button.click()

    # Wait for the URL to change to the notification page URL
    wait.until(EC.url_contains('/notifications'))

    # Check if the URL contains the expected notification page URL
    if '/notifications' in driver.current_url:
        print("TEST 2: `Reject Friend Request` successful")
    else:
        print("TEST 2: `Reject Friend Request` successful")

# Accept friend request test function for receiver
def accept_friend_request_test(driver, username, password):

    # Find the element with the id "Topbar" and hover over it
    topbar_element = driver.find_element(By.ID, "User Hover")
    hover = ActionChains(driver).move_to_element(topbar_element)
    hover.perform()
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
    print("TEST: 0 `User hover` successful")

    # Find the element with the id "Notification Button" and click it
    notification_button_element = driver.find_element(By.ID, "Notification Button")
    wait.until(EC.presence_of_element_located((By.ID, "Notification Button")))
    hover = ActionChains(driver).move_to_element(notification_button_element)
    hover.perform()
    wait.until(EC.element_to_be_clickable((By.ID, "Notification Button")))
    ActionChains(driver).click(notification_button_element).perform()

    # Check if the URL contains the expected notification page URL
    if '/notifications' in driver.current_url:
        print("TEST 1: `Notifications` successful")
    else:
        print("TEST 1: `Notifications` failed")

    # Find the accept friend request button
    accept_friend_request_button = wait.until(EC.presence_of_element_located((By.ID, "accept friend request button")))

    # Click the accept friend request button
    accept_friend_request_button.click()

    # Wait for the URL to change to the notification page URL
    wait.until(EC.url_contains('/notifications'))

    # Check if the URL contains the expected notification page URL
    if '/notifications' in driver.current_url:
        print("TEST 2: `Accept Friend Request` successful")
    else:
        print("TEST 2: `Accept Friend Request` successful")


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

# Call the video page test function
print("Contact Video Page Test Start")
login(driver, 'linus', 'Admin123')
time.sleep(0.5)
add_contact_page_search_and_friend_request_test(driver, 'linus', 'Admin123')
remove_friend_request_test(driver, 'linus', 'Admin123')
add_contact_page_search_and_friend_request_test(driver, 'linus', 'Admin123')
logout(driver, 'linus', 'Admin123')
login(driver, 'adrian', 'cclemon0912')
reject_friend_request_test(driver, 'adrian', 'cclemon0912')
logout(driver, 'linus', 'Admin123')
login(driver, 'linus', 'Admin123')
add_contact_page_search_and_friend_request_test(driver, 'linus', 'Admin123')
logout(driver, 'linus', 'Admin123')
login(driver, 'adrian', 'cclemon0912')
accept_friend_request_test(driver, 'adrian', 'cclemon0912')
logout(driver, 'adrian', 'cclemon0912')
print("Contact Video Page Test Completed")

# close the webdriver
driver.quit()

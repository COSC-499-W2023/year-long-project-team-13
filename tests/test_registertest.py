# # Test for register.html page
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
# from selenium import webdriver

# def register_page_test(driver):
#     video_button_element = driver.find_element(By.ID, "register")
#     video_button_element.click()
#     wait.until(EC.url_contains('/register'))
#     if '/register' in driver.current_url:
#          # Check if the URL contains the expected video page URL
#         print("Test successful")
#     else:
#         print("Test failed")

# # Create a ChromeOptions object with the log level set to 3
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# # Use the ChromeOptions and Service with suppressed logging
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
# driver.maximize_window()

# # Set the wait time for the driver
# wait = WebDriverWait(driver, 60)

# # Navigate to the homepage
# driver.get('http://localhost:8000')

# # Call the video page test function
# register_page_test(driver)

# # close the webdriver
# driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def register_page_test(driver, username, email, password):
    # Find the username, email, and password fields and fill them out
    username_element = driver.find_element(By.ID, "id_username")
    username_element.send_keys(username)

    email_element = driver.find_element(By.ID, "id_email")
    email_element.send_keys(email)

    password1_element = driver.find_element(By.ID, "id_password1")
    password1_element.send_keys(password)

    password2_element = driver.find_element(By.ID, "id_password2")
    password2_element.send_keys(password)

    # Submit the form
    password2_element.send_keys(Keys.RETURN)

    # Wait for the registration to complete (you might need to adjust the wait time)
    wait.until(EC.url_contains('/login'))

    # Check if the URL contains the expected login page URL
    if '/login' in driver.current_url:
        print("Registration successful")
    else:
        print("Registration failed")

# Create a ChromeOptions object with the log level set to 3
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

# Set the wait time for the driver
wait = WebDriverWait(driver, 10)  # Adjust the wait time as needed

# Navigate to the registration page
driver.get('http://localhost:8000/register/')  # Update the URL if needed

# Call the register page test function with appropriate input values
register_page_test(driver, 'your_username', 'your_email@example.com', 'your_password')

# Close the webdriver
driver.quit()

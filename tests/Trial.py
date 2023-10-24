from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

def click_element_by_id(driver, element_id):
    element = driver.find_element(By.ID, element_id)
    element.click()

def page_test(driver, page_url, element_id, expected_url):
    driver.get(page_url)
    wait.until(EC.url_to_be(page_url))
    click_element_by_id(driver, element_id)
    wait.until(EC.url_contains(expected_url))
    if expected_url in driver.current_url:
        print("Test successful")
    else:
        print("Test failed")

def add_contact_page_test(driver):
    page_test(driver, 'http://localhost:8000', 'Contact Button', '/contact-page-url')

def add_home_page_test(driver):
    page_test(driver, 'http://localhost:8000', 'Home Button', '/home-page-url')

def add_login_page_test(driver):
    page_test(driver, 'http://localhost:8000', 'Login Button', '/login-page-url')

def add_register_page_test(driver):
    page_test(driver, 'http://localhost:8000', 'Register Button', '/register-page-url')

def add_profile_page_test(driver):
    page_test(driver, 'http://localhost:8000', 'Profile Button', '/profile-page-url')

def add_new_video_page_test(driver):
    page_test(driver, 'http://localhost:8000', 'New Video Button', '/new-video-page-url')

def add_logout_page_test(driver):
    page_test(driver, 'http://localhost:8000', 'Logout Button', '/logout-page-url')

# Create the WebDriver instance
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")  # Suppress log messages

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 60)

# Call the test functions for different pages
add_contact_page_test(driver)
add_home_page_test(driver)
add_login_page_test(driver)
add_register_page_test(driver)
add_profile_page_test(driver)
add_new_video_page_test(driver)
add_logout_page_test(driver)

# Close the WebDriver when done
driver.quit()

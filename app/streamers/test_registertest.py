# Test for register.html page
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--log-level=3")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.maximize_window()

# driver wait time
wait = WebDriverWait(driver, 60)

def test_register_page():
    driver.get('http://127.0.0.1:8000/register/')

    # Test that the page title is correct
    assert driver.title == "Register"

    # Test that the form fields are present
    assert driver.find_element(By.ID, "id_username").is_displayed()
    assert driver.find_element(By.ID, "id_email").is_displayed()
    assert driver.find_element(By.ID, "id_password1").is_displayed()
    assert driver.find_element(By.ID, "id_password2").is_displayed()

    # Test that the "I agree" checkbox is present
    assert driver.find_element(By.ID, "id_agree").is_displayed()

    # Test that the "Register" button is present
    assert driver.find_element(By.XPATH, "//button[text()='Register']").is_displayed()

    # Test that clicking the "Register" button redirects to the login page
    register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
    register_button.click()
    wait.until(EC.url_to_be('http://127.0.0.1:8000/login/'))

    # Test that the "Already have an account" link is present
    assert driver.find_element(By.XPATH, "//a[text()='Sign In']").is_displayed()

    # Test that clicking the "Already have an account" link redirects to the login page
    login_link = driver.find_element(By.XPATH, "//a[text()='Sign In']")
    login_link.click()
    wait.until(EC.url_to_be('http://127.0.0.1:8000/login/'))

    driver.quit()

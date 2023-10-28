from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()

wait = WebDriverWait(driver, 60)

driver.get('https://www.bstackdemo.com/')

wait.until(EC.url_to_be('https://www.bstackdemo.com/'))

sign_in=driver.find_element(By.ID, "signin")
sign_in.click()

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/form/div[2]/div[1]/div/div[1]/div[1]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/form/div[2]/div[1]/div/div[1]/div[1]/div[1]"))).click()
active_ele = driver.switch_to.active_element
active_ele.send_keys("demouser")
active_ele.send_keys(Keys.ENTER)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/form/div[2]/div[2]/div/div[1]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/form/div[2]/div[2]/div/div[1]/div[1]"))).click()


active_ele = driver.switch_to.active_element
active_ele.send_keys("testingisfun99")
active_ele.send_keys(Keys.ENTER)

sign_in=driver.find_element(By.ID, "login-btn")
sign_in.click()

#Select a Google phone and add it to the cart
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/main/div[1]/div[3]/label/span"))).click()
#Like a phone
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/main/div[2]/div[2]/div[1]/button"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div/div/main/div[2]/div[3]/div[4]"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,"buy-btn"))).click()

#Checkout
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "firstNameInput"))).click()
active_ele = driver.switch_to.active_element
active_ele.send_keys("Alice")
active_ele.send_keys(Keys.ENTER)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "lastNameInput"))).click()
active_ele = driver.switch_to.active_element
active_ele.send_keys("Cooper")
active_ele.send_keys(Keys.ENTER)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "addressLine1Input"))).click()
active_ele = driver.switch_to.active_element
active_ele.send_keys("Apt.5, Downton Building, Cherryblossom Road")
active_ele.send_keys(Keys.ENTER)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "provinceInput"))).click()
active_ele = driver.switch_to.active_element
active_ele.send_keys("Canterbury")
active_ele.send_keys(Keys.ENTER)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "postCodeInput"))).click()
active_ele = driver.switch_to.active_element
active_ele.send_keys("CT3")
active_ele.send_keys(Keys.ENTER)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,"downloadpdf"))).click()
driver.quit()

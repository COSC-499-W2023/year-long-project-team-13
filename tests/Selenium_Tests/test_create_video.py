from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import os


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
    wait.until(EC.url_contains('/'))
    print("Login Successful")

def logout(driver, location):

    # Find the element with the id "Topbar" and hover over it
    wait.until(EC.presence_of_element_located((By.ID, "User Hover")))
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
    wait.until(EC.presence_of_element_located((By.ID, hoverButton)))
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


def create_record_video_test(driver, dueDateYear, dueDateMonthDay, dueDateTime):
    # Find the element with the id "videos hover" and hover over it
    hoverTest("Videos Hover","New Video Button", '/new', "`Send Video page found`")

    # Find the element with the id "side-bar-btn" and click it
    wait.until(EC.visibility_of_element_located((By.ID, "side-bar-btn")))
    side_bar_btn = driver.find_element(By.ID, "side-bar-btn")
    wait.until(EC.element_to_be_clickable((By.ID, "side-bar-btn")))
    side_bar_btn.click()
    wait.until(EC.visibility_of_element_located((By.ID, "close-btn")))
    close_btn = driver.find_element(By.ID, "close-btn")
    wait.until(EC.element_to_be_clickable((By.ID, "close-btn")))
    close_btn.click()
    print("TEST: 0 `Side Bar Button` Successful")

    # Find the element with the id "start-camera" and click it
    start_camera_element = driver.find_element(By.ID, "start-camera")
    wait.until(EC.element_to_be_clickable((By.ID, "start-camera")))
    start_camera_element.click()
    print("TEST: 1 `Start Camera` Successful")
    # time.sleep(10)
    wait.until(EC.visibility_of_element_located((By.ID, "video")))

    # Find the element with the id "start-record" and click it
    # Scroll down the page
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)
    wait.until(EC.visibility_of_element_located((By.ID, "start-record")))
    wait.until(EC.presence_of_element_located((By.ID, "start-record")))
    start_record_element = driver.find_element(By.ID, "start-record")
    wait.until(EC.element_to_be_clickable((By.ID, "start-record")))
    time.sleep(3)
    start_record_element.click()
    print("TEST: 2 `Start Record` Successful")

    # Find the element with the id "stop-record" and click it
    stop_record_element = driver.find_element(By.ID, "stop-record")
    wait.until(EC.element_to_be_clickable((By.ID, "stop-record")))
    stop_record_element.click()
    print("TEST: 3 `Stop Record` Successful")

    # Find the element with the id "next" and click it
    next_element = driver.find_element(By.ID, "next")
    wait.until(EC.element_to_be_clickable((By.ID, "next")))
    next_element.click()
    print("TEST: 4 `Next` Successful")

    # Find the element with the id "preview" and click it
    preview_element = driver.find_element(By.ID, "preview")
    wait.until(EC.element_to_be_clickable((By.ID, "preview")))
    preview_element.click()
    print("TEST: 5 `Preview` Successful")

    # Find the element with the id "back-details" and click it
    wait.until(EC.visibility_of_element_located((By.ID, "preview-title")))
    html.send_keys(Keys.PAGE_DOWN)
    wait.until(EC.visibility_of_element_located((By.ID, "back-details")))
    wait.until(EC.presence_of_element_located((By.ID, "back-details")))
    back_details_element = driver.find_element(By.ID, "back-details")
    wait.until(EC.element_to_be_clickable((By.ID, "back-details")))
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    html.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    back_details_element.click()
    print("TEST: 6 `Back Details` Successful")

    # Find the element with the id "back-record" and click it
    back_record_element = driver.find_element(By.ID, "back-record")
    wait.until(EC.element_to_be_clickable((By.ID, "back-record")))
    back_record_element.click()
    print("TEST: 7 `Back Record` Successful")

    # Find the element with the id "start-record" and click it
    wait.until(EC.visibility_of_element_located((By.ID, "video")))
    html.send_keys(Keys.PAGE_DOWN)
    wait.until(EC.visibility_of_element_located((By.ID, "start-record")))
    wait.until(EC.presence_of_element_located((By.ID, "start-record")))
    start_record_element = driver.find_element(By.ID, "start-record")
    wait.until(EC.element_to_be_clickable((By.ID, "start-record")))
    time.sleep(3)
    start_record_element.click()
    print("TEST: 8 `Start Record 2` Successful")

    # Find the element with the id "stop-record" and click it
    stop_record_element = driver.find_element(By.ID, "stop-record")
    wait.until(EC.element_to_be_clickable((By.ID, "stop-record")))
    time.sleep(3)
    stop_record_element.click()
    print("TEST: 9 `Stop Record 2` Successful")

    # Find the element with the id "download-video" and click it
    download_video_element = driver.find_element(By.ID, "download-video")
    wait.until(EC.element_to_be_clickable((By.ID, "download-video")))
    time.sleep(3)
    download_video_element.click()
    print("TEST: 10 `Download Video` Successful")

    # Find the element with the id "next" and click it
    next_element = driver.find_element(By.ID, "next")
    wait.until(EC.element_to_be_clickable((By.ID, "next")))
    time.sleep(3)
    next_element.click()

    # Find the element with the form request id and click it
    request_id_element = driver.find_element(By.ID, "id_request_id")
    wait.until(EC.presence_of_element_located((By.ID, "id_request_id")))
    Select(request_id_element).select_by_index(1)
    time.sleep(0.5)

    # Find the element with the form title and click it
    title_element = driver.find_element(By.ID, "id_title")
    wait.until(EC.presence_of_element_located((By.ID, "id_title")))
    title_element.click()
    title_element.send_keys("Test Record Video Title")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_title"), "Test Record Video Title"))

    # Find the element with the form description and click it
    description_element = driver.find_element(By.ID, "id_description")
    wait.until(EC.presence_of_element_located((By.ID, "id_description")))
    description_element.click()
    description_element.send_keys("Test Record Video Description")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_description"), "Test Record Video Description"))

    # Find the element with the form timelimit and click it
    timelimit_element = driver.find_element(By.ID, "id_timelimit")
    wait.until(EC.presence_of_element_located((By.ID, "id_timelimit")))
    timelimit_element.click()
    timelimit_element.send_keys(dueDateTime)
    time.sleep(0.5)
    timelimit_element.send_keys(Keys.TAB)
    timelimit_element.send_keys(dueDateYear)
    timelimit_element.send_keys(dueDateMonthDay)
    time.sleep(0.5)
    print("TEST: 11 `Video Record Info` Successful")

    blurface_element = driver.find_element(By.ID, "blurFace")
    wait.until(EC.presence_of_element_located((By.ID, "blurFace")))
    wait.until(EC.element_to_be_clickable((By.ID, "blurFace")))
    blurface_element.click()

    # Find the element with the id "preview" and click it
    preview_element = driver.find_element(By.ID, "preview")
    wait.until(EC.element_to_be_clickable((By.ID, "preview")))
    preview_element.click()
    print("TEST: 12 `Preview` Successful")

    # Find the element with the id "submit" and click it
    wait.until(EC.visibility_of_element_located((By.ID, "preview-title")))
    html.send_keys(Keys.PAGE_DOWN)
    wait.until(EC.visibility_of_element_located((By.ID, "submit")))
    wait.until(EC.presence_of_element_located((By.ID, "submit")))
    submit_element = driver.find_element(By.ID, "submit")
    wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    time.sleep(3)
    submit_element.click()

    # Wait for the URL to change to the video page URL
    wait.until(EC.url_contains('/video'))

    # Check if the URL contains the expected page URL
    if '/video' in driver.current_url:
        print("TEST 13: `Send Record Video` Successful")
    else:
        print("TEST 13: `Send Record Video` Failed")


def remove_video_post_test(driver):
    # Find the element with the id "videos hover" and hover over it
    hoverTest("User Hover","Notification-Button", '/notifications', "`Notification page found`")

    # Find the remove video post button
    remove_video_post_button = wait.until(EC.element_to_be_clickable((By.ID, "delete video post button")))

    # Click the remove video post button
    remove_video_post_button.click()

    # Wait for the URL to change to the notification page URL
    wait.until(EC.url_contains('/notifications'))

    # Check if the URL contains the expected notification page URL
    if '/notifications' in driver.current_url:
        print("TEST 13: `Remove Video Post` successful")
    else:
        print("TEST 13: `Remove Video Post` Failed")


def upload_video_test(driver, dueDateYear, dueDateMonthDay, dueDateTime, video):
    # Find the element with the id "videos hover" and hover over it
    hoverTest("Videos Hover","New Video Button", '/new', "`Send Video page found`")
    html = driver.find_element(By.TAG_NAME, "html")

    # Find the top upload button and click it
    wait.until(EC.visibility_of_element_located((By.ID, "top_upload")))
    wait.until(EC.presence_of_element_located((By.ID, "top_upload")))
    top_upload_button = driver.find_element(By.ID, "top_upload")
    wait.until(EC.element_to_be_clickable((By.ID, "top_upload")))
    time.sleep(3)
    top_upload_button.click()

    # Find the element with the id "side-bar-btn" and click it
    wait.until(EC.visibility_of_element_located((By.ID, "side-bar-btn")))
    side_bar_btn = driver.find_element(By.ID, "side-bar-btn")
    wait.until(EC.element_to_be_clickable((By.ID, "side-bar-btn")))
    side_bar_btn.click()

    wait.until(EC.visibility_of_element_located((By.ID, "close-btn")))
    close_btn = driver.find_element(By.ID, "close-btn")
    wait.until(EC.element_to_be_clickable((By.ID, "close-btn")))
    close_btn.click()
    print("TEST: 0 `Side Bar Button` Successful")
    # scroll down the page without using html.send_keys(Keys.PAGE_DOWN)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait for the URL to change to the upload page URL
    wait.until(EC.url_contains('video/new'))

    # Find the element with the form request id and click it
    request_id_element = driver.find_element(By.ID, "id_request_id")
    wait.until(EC.presence_of_element_located((By.ID, "id_request_id")))
    Select(request_id_element).select_by_index(1)
    time.sleep(0.5)

    # Find the element with the form title and click it
    title_element = driver.find_element(By.ID, "id_title")
    wait.until(EC.presence_of_element_located((By.ID, "id_title")))
    title_element.click()
    title_element.send_keys("Test Upload Video Title")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_title"), "Test Upload Video Title"))

    # Find the element with the form description and click it
    description_element = driver.find_element(By.ID, "id_description")
    wait.until(EC.presence_of_element_located((By.ID, "id_description")))
    description_element.click()
    description_element.send_keys("Test Upload Video Description")
    wait.until(EC.text_to_be_present_in_element_value((By.ID, "id_description"), "Test Upload Video Description"))

    # Find the element with the form timelimit and click it
    timelimit_element = driver.find_element(By.ID, "id_timelimit")
    wait.until(EC.presence_of_element_located((By.ID, "id_timelimit")))
    timelimit_element.click()
    timelimit_element.send_keys(dueDateTime)
    time.sleep(0.5)
    timelimit_element.send_keys(Keys.TAB)
    timelimit_element.send_keys(dueDateYear)
    timelimit_element.send_keys(dueDateMonthDay)
    time.sleep(0.5)

    # Find the element with the form video and upload video file
    uploadvideo = driver.find_element(By.ID, "video_upload")
    uploadvideo.send_keys(video)
    time.sleep(0.5)

    # Check that the upload button goes to home page
    wait.until(EC.visibility_of_element_located((By.ID, "upload")))
    wait.until(EC.presence_of_element_located((By.ID, "upload")))
    upload_button_element = driver.find_element(By.ID, "upload")
    wait.until(EC.element_to_be_clickable((By.ID, "upload")))
    upload_button_element.click()

    # Wait for the URL to change to the video page URL
    wait.until(EC.url_contains('/video'))

    # Check if the URL contains the expected video page URL
    if '/video' in driver.current_url:
        print("TEST: 14 `Video Upload Post` Successful")
    else:
        print("TEST: 14 `Video Upload Post` Failed")



def filled_record_video_test(driver):
    # Find the element with the id "Notification-Button" and hover over it
    hoverTest("Notification-Button","Notification-Button", '/notifications', "`Notifications page found`")
    html = driver.find_element(By.TAG_NAME, "html")
    html.send_keys(Keys.PAGE_DOWN)

    # Find the element with the id "Send Video" and click it
    send_video_element = driver.find_element(By.ID, "Send Video")
    wait.until(EC.element_to_be_clickable((By.ID, "Send Video")))
    send_video_element.click()
    wait.until(EC.url_contains('/record'))
    if EC.url_contains('/record'):
        print("TEST: 15 `Send Video` Successful")
    else:
        print("TEST: 15 `Send Video` Failed")

    # Find the element with the id "top_upload" and click it
    wait.until(EC.presence_of_all_elements_located((By.ID, "top_upload")))
    top_upload_element = driver.find_element(By.ID, "top_upload")
    wait.until(EC.element_to_be_clickable((By.ID, "top_upload")))
    top_upload_element.click()

    wait.until(EC.url_contains('/upload'))
    if EC.url_contains('/upload'):
        print("TEST: 16 `Upload Video` Successful")
    else:
        print("TEST: 16 `Upload Video` Failed")

# Create a ChromeOptions object with the log level set to 3
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("--start-maximized")
opt.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--log-level=3")  # Set log level to suppress warnings

# Use the ChromeOptions and Service with suppressed logging
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opt)
driver.maximize_window()

# Set the wait time for the driver
wait = WebDriverWait(driver, 60)

# Navigate to the homepage
driver.get('http://localhost:8000/login')

# Call the login page test function with appropriate input values
print("Create Video Test Start")
login(driver, 'adrian', 'cclemon0912')  # Replace with actual credentials
time.sleep(0.5)
create_record_video_test(driver, "2024", "0101", "1000AM")
remove_video_post_test(driver)
upload_video_test(driver, "2024", "0101", "1000AM", os.path.abspath('../../app/media/Beautiful_City_SEA_VIEW___Creative_Commons_Videos___Free_HD_Videos_-_no_copyright.mp4'))
filled_record_video_test(driver)
logout(driver, '/upload/#')
print("Create Video Test Completed")

# Close the webdriver
driver.quit()


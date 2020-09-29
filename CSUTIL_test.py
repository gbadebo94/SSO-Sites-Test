import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(
    'https://cstutil.it.siu.edu/CSRfrontend/')
time.sleep(2)

link = driver.find_element_by_link_text(
    '>>SSL Certificate Signing Request/C-S-C Authorization Submission<<')
link.click()
time.sleep(2)

window_after = driver.window_handles[1]
driver.switch_to.window(window_after)

email = driver.find_element_by_id("userNameInput")
email.clear()
email.send_keys("SIU921000021")

password = driver.find_element_by_name("Password")
password.clear()
password.send_keys("]V.TZbHIrkBDxOzEWzQ{")

login_button = driver.find_element_by_id("submitButton")
login_button.click()

driver.implicitly_wait(5)



try:
    elem = driver.find_element_by_id('CSRformSetup')
    if elem.is_displayed():
        elem.click()
        print("Login is successful")

except NoSuchElementException:
    print("Login is Unsuccessful, element cannot be found")





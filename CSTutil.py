from selenium import webdriver
from siuSiteTest import WebDriverTest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

rd = WebDriverTest('firefox')
# rd.setBrowserPath("/opt/firefox/firefox")
rd.createBrowserDriver()
rd.setSite("https://cstutil.it.siu.edu/CSRfrontend/")

elem = rd.driver.find_element_by_link_text(
    '>>SSL Certificate Signing Request/C-S-C Authorization Submission<<')
elem.click()

time.sleep(2)

window_after = rd.driver.window_handles[1]
rd.driver.switch_to.window(window_after)
# rd.login("UserName", "Password", "email/netid", "password", "submitButton")
# rd.login("UserName", "Password", "SIU921000021", "]V.TZbHIrkBDxOzEWzQ{", "submitButton")
rd.login("UserName", "Password", "SIU853154227", "TayoSegiFunmiMayowaSeunTobi-", "submitButton")

rd.driver.implicitly_wait(5)
#elem = rd.driver.find_element_by_link_text(
 #   'Required digital signature algorithm (minimum of SHA-2)')
#elem.click()



#elem = rd.driver.find_element_by_xpath("//input[@name='saveForm' and @value='Submit SSL CSR/C-S-C Authorization Request']")[0]
#elem.click()


elem = rd.driver.find_element_by_id('element textarea large')
elem.click()
#elem = rd.driver.find_element_by_link_text("Proudly powered by WordPress")
#elem.click()
# if elem.is_displayed():
#print("Login Success")

#else:
#print("Login failure")

# print(rd.driver.title)

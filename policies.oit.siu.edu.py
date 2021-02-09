from selenium.common.exceptions import NoSuchElementException

from siuSiteTest import WebDriverTest

rd = WebDriverTest("firefox")
# rd.setBrowserPath("/opt/firefox/firefox")
rd.createBrowserDriver()
rd.setSite("https://policies.oit.siu.edu")

elem = rd.driver.find_element_by_link_text("Sign in with SIU SSO")
elem.click()

# rd.login("UserName", "Password", "email/netid", "password", "submitButton")
rd.login("UserName", "Password", "", "", "submitButton")


rd.driver.implicitly_wait(5)

try:
    elem = rd.driver.find_element_by_partial_link_text('Entries feed')
    if elem.is_displayed():
        elem.click()
        print("Login is successful")

except NoSuchElementException:
    print("Login is Unsuccessful, element cannot be found")


from selenium import webdriver
from bs4 import BeautifulSoup

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path='geckodriver.exe')

# load the website to driver using driver
driver.get("https://itmfs1.it.siu.edu/PF/")

# Beautiful Soup is a Python package for parsing HTML and XML documents.
# It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping
soup_level2 = BeautifulSoup(driver.page_source, 'lxml')

href = soup_level2.find('frame')

# https://itmfs1.it.siu.edu/PF/ URL is hidden page. we cant get directly from this website.
# so taking src from this site and loading into another driver
url = "https://itmfs1.it.siu.edu/PF/" + href.get('src')
driver.close()
driver1 = webdriver.Firefox(executable_path='geckodriver.exe')
driver1.get(url)

driver1.find_element_by_link_text("LOGIN").click()

username = driver1.find_element_by_id("userNameInput")
username.clear()
username.send_keys("")

password = driver1.find_element_by_name("Password")
password.clear()
password.send_keys("")

login_button = driver.find_element_by_id("submitButton")
login_button.click()

""" Chrome Options in Selenium Webdriver """

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.add_argument("--start-maximized")
options.add_argument("headless")
options.add_argument("--ignore-certificate-errors")

service_obj = Service()

# Invocation of Chrome browser
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")

print(driver.title)


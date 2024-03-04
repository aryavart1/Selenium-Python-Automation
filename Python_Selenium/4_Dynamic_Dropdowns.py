"""Handling auto-suggestive dynamic drop-downs using Selenium Webdriver"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

# Country dropdown field on Page 1
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(2)

countries = driver.find_elements(By.CLASS_NAME, "ui-menu-item")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

# Can't use Text method as the text information is not present on page, it came dynamically through running the script
# Using Get Attribute of values to validate dynamic texts on the browser (checks the value updated in the HTML DOM)
print(driver.find_element(By.ID, "autosuggest").get_attribute("value"))
assert (driver.find_element(By.ID, "autosuggest").get_attribute("value")) == "India"


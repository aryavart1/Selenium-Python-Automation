""" Handling Java/Javascript Alert popups using Selenium """

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Switch To Alert Example field on the Page
text = "Test Alert pop-up"
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(text)

# Clicking on Alert button on the Page
driver.find_element(By.CSS_SELECTOR, "#alertbtn").click()

alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
time.sleep(2)
assert text in alertText
# To accept the alert popup
alert.accept()

# To dismiss the alert popup
# alert.dismiss()
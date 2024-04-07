from selenium import webdriver

# chrome driver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# XPath and CSS selector can also be used for partial values
# Using regular expression CSS -> tagname[attribute*='value']
# Using regular expression Xpath ->  //tagname[contains(@attribute,'value')]
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()




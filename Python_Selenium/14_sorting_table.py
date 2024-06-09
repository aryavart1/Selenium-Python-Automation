""" Sorting the Web tables using Selenium Python """

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

browser_sorted_veg = []

# Click on column header
# driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
driver.find_element(By.XPATH, "//span[starts-with(text(),'Veg/fruit')]").click()   # Xpath with starts-with()
time.sleep(4)

# Collect all browser sorted vegetable names -> browser_sorted_veg
# To check XPath -> Go to console -> $x("//tr/td[1])
veg_web_elements = driver.find_elements(By.XPATH, "//tr/td[1]")

for veg in veg_web_elements:
    browser_sorted_veg.append(veg.text)

original_browser_sorted_veg = browser_sorted_veg.copy()

# Sorting browser_sorted_veg -> new_sorted_list
browser_sorted_veg.sort()

# Verify that browser_sorted_veg == new_sorted_list
assert browser_sorted_veg == original_browser_sorted_veg


""" Sorting the Web tables using Selenium Python """

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# Click on column header
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
# Collecting all browser sorted vegetable names -> veg_list
# Sorting veg_list -> new_sorted_list
# Verify that veg_list == new_sorted_list


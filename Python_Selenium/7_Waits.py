""" Developing End to End Testcase to Automate ecommerce GreenKart Application
    Synchronization (Explicit & Implicit Waits) in Selenium Webdriver """


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

# Implicit wait (It's a global timeout and it's applied to each line of code)
driver.implicitly_wait(5)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results) 
assert count > 0

# Chaining -> from parent webelements accessing child webelements under it
# Adding products in cart by clicking on ADD TO CART button
for result in results:
    result.find_element(By.XPATH, "div/button").click()

# Clicking on Cart image on top right corner of the Page
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart").click()

# Clicking on Cart image on top right corner of the Page
# Locator used -> Xpath for text - //tagname[text()='text name']
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sending value in the "Enter promo code" text field of the page.
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# Clicking on Apply button next to "Enter promo code" text field on the Page
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)












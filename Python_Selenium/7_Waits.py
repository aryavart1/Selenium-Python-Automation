""" Functional Automation & Developing End to End Testcase to Automate ecommerce GreenKart Application"""

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expected_list = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actual_list = []


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)


""" Synchronization (Explicit & Implicit Waits) in Selenium Webdriver """

# Adding Implicit wait (It's a global timeout, and it's applied to each line of code)
# Implicit wait doesn't catch performance errors
# Maximum implicit wait time is applied to the testcase before throwing an exception
driver.implicitly_wait(2)

results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results) 
assert count > 0

""" Chaining -> from parent webelements accessing child webelements under it """
# Adding products in cart by clicking on ADD TO CART button
for result in results:
    actual_list.append(result.find_element(By.XPATH, "h4").text)  # Adding Product name in the List
    result.find_element(By.XPATH, "div/button").click()

assert expected_list == actual_list

# Clicking on Cart image on top right corner of the Page
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart").click()

# Clicking on Cart image on top right corner of the Page
# Locator used -> Xpath for text - //tagname[text()='text name']
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Functional Automation
# Sum validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0

for price in prices:
    sum = sum + int(price.text)
print(sum)

total_amount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)

assert sum == total_amount

# Sending value in the "Enter promo code" text field of the page.
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")

# Clicking on Apply button next to "Enter promo code" text field on the Page
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Adding Explicit wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

# Checking if discounted amount is always lesser than total amount
discounted_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert total_amount > discounted_amount











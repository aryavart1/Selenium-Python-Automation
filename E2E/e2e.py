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

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# Chaining of web elements
for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text
    if product_name == "Blackberry":
        product.find_element(By.XPATH, "div/button").click()

# Cart button
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

# Checkout button
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

driver.find_element(By.ID, "country").send_keys("Ind")

# Adding Explicit wait
wait = WebDriverWait(driver, 10)
"""presenceOfElementLocated - element is present on the DOM of a page. 
   visibilityOfElementLocated -> element is present on the DOM of a page and visible"""
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()

driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

success_text = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you! Your order will be delivered in next few weeks :-)." in success_text




"""Handling static drop-downs using Select class in Selenium Webdriver"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")


# ID, Xpath, CSS Selector, Classname, name, Link Text

# To verify the locator is pointing to the right web element
# Go to console
# $x("") -> Xpath
# $("") -> CSS

# Name field on the form
# Locator used -> CSS Selector - tagname[attribute='value'],  #id, .classname
# Tag name is optional for CSS selectors
driver.find_element(By.CSS_SELECTOR, "input[name = 'name']").send_keys("James")

# Email field on the form
# Locator used -> NAME
driver.find_element(By.NAME, "email").send_keys("test_email@xyz.com")

# Password field on the form
# Locator used -> ID
driver.find_element(By.ID, "exampleInputPassword1").send_keys("test_pass")

# Checkbox field under password field on the form
# Locator used -> CSS Selector (tagname[attribute='value'],  #id, .classname)
driver.find_element(By.CSS_SELECTOR, "input[id='exampleCheck1']").click()

# Gender field on form (Static Drop-down)
# By using Select class in Selenium
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
# dropdown.select_by_visible_text("Female")
# dropdown.select_by_value("")  #Using value attribute if defined

# Employee Status field on the form
# Locator used -> CSS Selector (#id method)
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Submit button on the form
# Locator used -> Xpath -  //tagname[@attribute='value']
# Xpath for text - //tagname[text()='text name']
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Success message after clicking on Submit button
# Locator used -> Class name
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
# Check "Success" word in message
assert "Success" in message

# "Two-way Data Binding example:" field on form
# Selenium scans everything on web application from top left
# If multiple elements are identified with the same Xpath then we can use Index to make it unique
# Locator used -> Xpath -  //(tagname[@attribute='value'])[index]
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys(" Bond")
driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()
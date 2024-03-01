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

# Email field on the form
# Locator used -> NAME
driver.find_element(By.NAME, "email").send_keys("test_email@xyz.com")

# Password field on the form
# Locator used -> ID
driver.find_element(By.ID, "exampleInputPassword1").send_keys("test_pass")

# Xpath -  //tagname[@attribute='value'] -> //input[@type='submit']
# Xpath for text - //tagname[text()='text name'] -> //button[text()='Save New Password']

# CSS -  tagname[attribute='value'] -> //input[@type='submit'],  #id, .classname

driver.find_element(By.CSS_SELECTOR, "input[id='exampleCheck1']").click()

driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()  # used '#id' method

# Static Drop-down
# By using Select class in Selenium

dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)

# dropdown.select_by_visible_text("Female")
# dropdown.select_by_value(1)         if value attribute is defined

driver.find_element(By.XPATH, "//input[@type='submit']").click()

message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

# If using elements multiple elements are identified then we can use Index to make it unique

driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").send_keys("hello again")

driver.find_element(By.XPATH, "(//input[@type = 'text'])[3]").clear()
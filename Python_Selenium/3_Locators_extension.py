from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/client")

# 2_Locators ->  ID, Xpath, CSS Selector, Classname, name, Link Text

# Clicking on Forgot Password link button on the Page 1
# Locator used -> Link Text (similar locator Partial Link Text can also be used)
# Verify that the HTML has anchor <a> tag for link
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# Email field present on Page 2
# Locator used -> XPath
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("test@gmail.com")

# Password field present on Page 2
# Locator used -> CSS Selector
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Password123")

# Confirm Password field on Page 2
# Locator used -> CSS Selector (#id method)
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Password123")

# Save New Password button on Page 2
# Locator used -> XPath for text -> //tagname[text()='text name']
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()


#driver.close()
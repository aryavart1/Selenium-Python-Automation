""" Handling CheckBox dynamically using Selenium Python programming """

# import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# To click on Option2 checkbox under Checkbox Example
# Locator used -> XPath
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()  # To verify if the checkbox is selected
        break

# To click on Radio2 under Radio Button example
# Locator used -> CSS Selector (.classname)
# A case where position of Radio buttons won't change we can directly use Index of buttons
radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()
assert radiobuttons[2].is_selected()  # To verify if the radio button is selected

# To verify Element Displayed Example field on form
assert driver.find_element(By.ID, "displayed-text").is_displayed()
# Clicking on Hide Button
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()

# To verify Show button on the form
driver.find_element(By.ID, "show-textbox").click()
assert driver.find_element(By.NAME, "show-hide").is_displayed()
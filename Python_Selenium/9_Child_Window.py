""" Techniques to handle Child Windows/Tabs with Selenium """


# import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
driver.implicitly_wait(2)

# 'Window_handle' returns all the windows in the same order they are opened in the form of list.
windows_opened = driver.window_handles

# Locator used -> Tag name
driver.switch_to.window(windows_opened[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.close()  # closes the window

# Locator used -> Tag name
driver.switch_to.window(windows_opened[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME, "h3").text























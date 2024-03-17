""" Techniques to handle iFrames with Selenium
    iFrames are separate entities sitting on top of HTML, they act as a different page"""


# import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")  # added ID value from iframe tag-name

driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("I am able to automate")

driver.switch_to.default_content()  # switches back to default browser page
print(driver.find_element(By.CSS_SELECTOR, "h3").text)





















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
driver.find_element((By.LINK_TEXT, "Click Here")).click()

""" Advanced UI Interactions with Browser elements using Action class """

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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
# action.double_click()
# action.context_click()  """ To right-click on any web element) """
# action.click_and_hold()
# action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()

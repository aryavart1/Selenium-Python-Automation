from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

item1 = driver.find_element(By.XPATH,"//ul[@id='gallery']/li[1]")
item2 = driver.find_element(By.XPATH,"//ul[@id='gallery']/li[2]")

trash = driver.find_element(By.XPATH,"//div[@id='trash']")

act=ActionChains(driver)

act.drag_and_drop(item1, trash).perform()
act.drag_and_drop(item2, trash).perform()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.snapdeal.com")
driver.get("http://www.amazon.com")

driver.back()  # snapdeal
driver.forward() # amazon

driver.refresh()

driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#driver.save_screenshot("C:\\Users\\admin\\PycharmProjects\\PythonSelenium\\day23\\homepage.png")
driver.save_screenshot(os.getcwd()+"\\homepage.png")
#driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")

#driver.get_screenshot_as_png()  #driver.get_screenshot_as_base64() #saves in binary format

driver.quit()

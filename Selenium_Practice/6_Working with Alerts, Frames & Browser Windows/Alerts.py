from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

'''serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)'''

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertwindow = driver.switch_to.alert
print(alertwindow.text)

alertwindow.send_keys("welcome")

# close alert window by using OK button
alertwindow.accept()

# close alert window by using Cancel button
# alertwindow.dismiss()
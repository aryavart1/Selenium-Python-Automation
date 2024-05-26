from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("http://www.google.com")
driver.maximize_window()

driver.find_element(By.NAME,"q").send_keys("selenium") #searchbox
searchitems=driver.find_elements(By.XPATH,"//ul[@role='listbox']/li/div/div[2]")

print(len(searchitems))

for item in searchitems:
    print(item.text)
    if item.text=='selenium':
        item.click()
        break
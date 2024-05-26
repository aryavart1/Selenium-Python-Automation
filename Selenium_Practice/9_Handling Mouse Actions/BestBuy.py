from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

#Edge
# serv_obj=Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
# driver=webdriver.Edge(service=serv_obj)

driver.implicitly_wait(10)

driver.get("https://www.bestbuy.com/?intl=nosplash")
driver.maximize_window()

#Approach1
# try:
#     signupbox=driver.find_element(By.XPATH,"//*[@id='widgets-view-email-modal-mount']/div/div/div[1]/div/div/div/div/button")
#     if signupbox.is_displayed():
#         signupbox.click() # this will close box
# except Exception:
#     print("Signup box not available")


#Approach2
act=ActionChains(driver)
act.send_keys(Keys.ESCAPE).perform()

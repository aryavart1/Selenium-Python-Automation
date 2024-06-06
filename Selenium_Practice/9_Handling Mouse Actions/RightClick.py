import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

'''serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)'''

driver.implicitly_wait(10)

driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)

act.context_click(button).perform()  # right click

time.sleep(5)
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click() # copy
time.sleep(3)
driver.switch_to.alert.accept()

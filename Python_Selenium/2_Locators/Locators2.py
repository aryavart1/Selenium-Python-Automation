from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("http://automationpractice.com/index.php")
driver.maximize_window()  #maximize the browser window

sliders=driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(len(sliders)) #5    total number of sliders on home page



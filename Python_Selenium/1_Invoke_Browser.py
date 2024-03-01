import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# Standard way of invoking Chrome browser
# Selenium webdriver -> Chrome driver service -> Chrome Browser
# By default Selenium checks the Chrome version and downloads the Chrome driver version
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# 2nd way - Using Service Class for invoking specific version of Chrome browser
# Chrome driver - Chrome browser
"""Service class sees what version of Chromedriver is installed in the local and runs the Chrome browser accordingly, It
makes runtime faster as Selenium manager doesn't need to identify what version of Chromedriver needs to be installed."""
# service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)

"""
#Firefox -> uses gecko driver 
service_obj = Service() 
driver = webdriver.Firefox(options=options,service=service_obj)
"""

"""
#Edge -> uses Microsoft Edge Web driver
service_obj = Service() 
driver = webdriver.Edge(options=options,service=service_obj)
"""

print(driver.title)
print(driver.current_url)
driver.refresh()

time.sleep(2)


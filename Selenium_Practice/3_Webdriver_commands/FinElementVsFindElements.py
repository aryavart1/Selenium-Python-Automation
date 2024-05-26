from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")

###########    find_element() - Returns single webelement

#1)Locator matching with single webelement
# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro 13-inch")

#2) Locator matching with multiple webelements
# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)  #prints first link from the footer "Sitemap"

#3) Element not available then throw NoSuchElementException
# login_element=driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()

#######   find_elements() - Returns multiple webElements

#1)Locator matching with single webelement
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))  #1
# elements[0].send_keys("Apple MacBook Pro 13-inch")

#2) Locator matching with multiple webelements
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))  #23
# #print(elements[0].text) #Sitemap
# for ele in elements:
#     print(ele.text)

#3) Element not available - zero
elements=driver.find_elements(By.LINK_TEXT,"Log")
print("elementws returend:",len(elements))

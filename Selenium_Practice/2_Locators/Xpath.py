from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/self::a").text
# print(text_msg) #India Tourism De

#parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/parent::td").text
# print(text_msg) #India Tourism De

#child
# childs=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/child::td")
# print(len(childs))  #5

#Ancestor
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr").text
# print(text_msg) #India Tourism De A 358.35 375.30 + 4.73

#Decendant
# descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/descendant::*")
# print("Number of descendant nodes:",len(descendants)) #7

#Following
# followings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/following::*")
# print("Number of descendant nodes:",len(followings)) #719

#Folowing-sibling
# followingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/following-sibling::*")
# print("Number of descendant nodes:",len(followingsiblings)) #72

#preceding
# precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/preceding::*")
# print(len(precedings)) #251


#preceding-sibling
precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/preceding-sibling::tr")
print(len(precedingsiblings)) #11

driver.close()

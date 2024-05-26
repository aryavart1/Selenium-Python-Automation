
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

#drpcountry_ele=driver.find_element(By.XPATH,"//select[@id='input-country']")
drpcountry=Select(driver.find_element(By.XPATH,"//select[@id='input-country']"))

#select option fro the edropdown
# drpcountry.select_by_visible_text("India")
# #drpcountry.select_by_value("10")  #Argentina
# #drpcountry.select_by_index(13)  # index

# capture all the options and print them
alloptions=drpcountry.options
print("total number of options:",len(alloptions))

# for opt in alloptions:
#     print(opt.text)

# select option from dropdown without using built-in method
# for opt in alloptions:
#     if opt.text=="India":
#         opt.click()
#         break

allOptions=driver.find_elements(By.XPATH,'//*[@id="input-country"]/option')
print(len(allOptions))

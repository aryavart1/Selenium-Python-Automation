# 1) Count number of rows & columns
# 2) Read specific row & Column data
# 3) Read all the rows & Columns data
# 4) Read data based on condition(List books name whose author is Mukesh)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()  # maximize window

# 1) Count number of rows & columns

noOfRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
noOfColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

print(noOfRows)  #7
print(noOfColumns) #4

# 2) Read specific row & Column data  - Master In Selenium

data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
#print(data)

# 3) Read all the rows & Columns data
print("printing all the rows and columns data.....................")

# for r in range(2,noOfRows+1):
#     for c in range(1,noOfColumns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end='             ')
#     print()

# 4) Read data based on condition(List books name whose author is Mukesh)
for r in range(2,noOfRows+1):
    authorName=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName=="Mukesh":
        bookName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(bookName,"         ",authorName,"       ",price)


driver.close()







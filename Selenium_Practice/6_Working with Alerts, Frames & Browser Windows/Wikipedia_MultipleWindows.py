from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("testing")
driver.find_element(By.XPATH,"//input[@type='submit']").click()

searchlinks=driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']//div/a")
print("Number of links:",len(searchlinks))

print("printing and clicking on links...............")
for link in searchlinks:
    print(link.text)
    link.click()

#After opening all the pages, capture windowid's
windowIds=driver.window_handles

print("Switching to each browser window and getting the titles........")
for windowid in windowIds:
    driver.switch_to.window(windowid)
    print(driver.title)

driver.quit()
# we need to install requests package through File-->Settings-->ProjectIntrepreter-->+--> requests

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

allLinks = driver.find_elements(By.TAG_NAME, 'a')
count = 0

for link in allLinks:
    url = link.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, "  is broken link")
        count += 1
    else:
        print(url, "   is valid link")

print("Total number of broken links:", count)

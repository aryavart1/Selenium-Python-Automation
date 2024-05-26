from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver=webdriver.Chrome(service=serv_obj,options=ops)
    return driver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("C:\Drivers\edgedriver_win64\msedgedriver.exe")
    ops=webdriver.EdgeOptions()
    ops.headless=True
    driver=webdriver.Edge(service=serv_obj,options=ops)
    return driver


def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    serv_obj = Service("C:\Drivers\geckodriver-v0.29.1-win64\geckodriver.exe")
    ops=webdriver.FirefoxOptions()
    ops.headless=True
    driver=webdriver.Edge(service=serv_obj,options=ops)
    return driver

#driver=headless_chrome()
#driver=headless_edge()
driver=headless_firefox()


driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.close()
# Test Case
# ------------------
# 1) Open Web Browser(Chrome/firefox/Edge).
# 2) Open URL  https://opensource-demo.orangehrmlive.com/
# 3) Enter username  (Admin).
# 4) Enter password  (admin123).
# 5) Click on Login.
# 6) Capture title of the home page.(Actual title)
# 7) Verify title of the page: OrangeHRM    (Expected)
# 8) close browser

from selenium import webdriver

# Selenium 3
# driver=webdriver.Chrome(executable_path="")
## driver=webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.find_element_by_name("txtUsername").send_keys("Admin")
# driver.find_element_by_id("txtPassword").send_keys("admin123")
# driver.find_element_by_id("btnLogin").click()
# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
# driver.close()

# Selenium4
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# serv_obj=Service("")
# driver=webdriver.Chrome(service=serv_obj)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.implicitly_wait(2)

driver.get("https://opensource-demo.orangehrmlive.com/")

driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

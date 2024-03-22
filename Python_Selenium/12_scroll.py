""" Scrolling with JavaScript executor as Webdriver doesn't include that functionality """

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=options, service=service_obj)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# To scroll to the bottom of the page using JavaScript
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# Take the screenshot at the particular step and will add it to the folder 
driver.get_screenshot_as_file("screen.png")

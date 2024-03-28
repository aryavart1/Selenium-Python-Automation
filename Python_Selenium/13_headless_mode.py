""" Running Selenium Webdriver in headless mode
    In headless mode the automation script will run in invisible mode and there will be no browser invocation """

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option("detach", True)

service_obj = Service()
driver = webdriver.Chrome(options=chrome_options, service=service_obj)

# Running in Headless mode
chrome_options.add_argument("headless")

# Maximize window
chrome_options.add_argument("--start-maximized")

#  To ignore certificate errors on webpage
chrome_options.add_argument("--ignore-certificate-errors")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# To scroll to the bottom of the page using JavaScript
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

# Take the screenshot at the particular step and will add it to the folder
driver.get_screenshot_as_file("screen.png")
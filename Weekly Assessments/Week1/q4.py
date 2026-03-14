"""
Automate Product Search on Myntra Using Class Name Locator
Description
Description
Open the Myntra website using Selenium WebDriver.
 Locate the search input field on the homepage using the class name locator.
 Enter the text "shoes" into the search field using Selenium’s send_keys() method.

Ensure that the correct locator is used to identify the search box before entering the text.
"""

from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://myntra.com")
sleep(2)
search = driver.find_element(By.CLASS_NAME, "desktop-searchBar")
search.send_keys("shoes")
sleep(2)
btn = driver.find_element(By.CLASS_NAME, "desktop-submit")
btn.click()
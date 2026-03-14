'''
Automate Search on YouTube Using Name Locator
Description
Description
Open the YouTube website using Selenium WebDriver.
 Locate the search input field on the homepage and enter the text "melody hits" into the search box.

Use Selenium’s send_keys() method to type the text into the search field.
'''
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.youtube.com/")
sleep(2)
search = driver.find_element(By.NAME, "search_query")
search.send_keys("melody hits")
sleep(2)
btn = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Search"]')
btn.click()
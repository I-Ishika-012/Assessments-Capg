'''
Automate Login Process on Facebook Using CSS Selectors
Description
Description
Open the Facebook login page using Selenium WebDriver.
 Maximize the browser window and locate the username/email field and password field using CSS selectors.

Enter sample login credentials into the respective fields and then locate the Login button using a CSS selector and click it.

Use appropriate waits if necessary to ensure elements are loaded before interacting with them.
'''
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.facebook.com")
sleep(2)
uname = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
uname.send_keys("Bruce Wayne")
sleep(2)
pwd = driver.find_element(By.CSS_SELECTOR, 'input[name="pass"]')
pwd.send_keys("iamnot@batman")
sleep(2)
btn = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Log in"]')
btn.click()
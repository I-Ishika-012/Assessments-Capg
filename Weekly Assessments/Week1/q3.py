"""
Automate Text Field Entry Using ID Locator
Description
Description
Open the Naukri.com website using Selenium WebDriver.
 Navigate to the registration page and identify the text input fields such as Name, Email, and Password.

Use the ID locator strategy to locate these elements and enter appropriate sample data into each field using Selenium commands.

Students should ensure that the browser opens successfully, elements are identified correctly, and the values are entered into the fields.
"""
from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://naukri.com/")
sleep(2)
reg = driver.find_element(By.ID, 'register_Layer')
reg.click()
sleep(2)
name = driver.find_element(By.ID, 'name')
name.send_keys("Bruce Wayne")
sleep(2)
email = driver.find_element(By.ID, 'email')
email.send_keys("brucewayne@gmail.com")
sleep(2)
password = driver.find_element(By.ID, 'password')
password.send_keys("iamnot@batman")
sleep(2)
mobile = driver.find_element(By.ID, 'mobile')
mobile.send_keys("8077700080")
sleep(2)
"""
## Practical Exercise 2

### Title
**Automate SauceDemo Login and Product Page with Explicit Waits and Verification**

### Description
Open the SauceDemo website using Selenium WebDriver (https://www.saucedemo.com/).

Implement the login flow and product page interactions using **Explicit Waits** to ensure elements are properly loaded and interactable.

Perform the following steps:
- Wait for the **Username** field to be clickable and enter `"standard_user"`
- Wait for the **Password** field to be clickable and enter `"secret_sauce"`
- Wait for the **Login** button to be clickable and click on it
- After login, wait for the **Products title** to be visible
- Capture and print the page title text

Continue with product page actions:
- Find ALL product names and print each name
- Find ALL product prices and print each price
- Click on the fourth product’s **Add to cart** button


Use **WebDriverWait** along with **Expected Conditions** for synchronization.
"""
# from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
driver.get("https://www.saucedemo.com/")
uname = driver.find_element(By.ID, "user-name")
wait.until(EC.element_to_be_clickable(uname)).send_keys("standard_user")
pwd = driver.find_element(By.ID, "password")
wait.until(EC.element_to_be_clickable(pwd)).send_keys("secret_sauce")
login_btn = driver.find_element(By.ID, "login-button")
wait.until(EC.element_to_be_clickable(login_btn)).click()
page_title = driver.find_element(By.CSS_SELECTOR, "span[data-test='title']")
#wait until title is visible
wait.until(EC.element_to_be_clickable(page_title))
print(page_title.text)

products = driver.find_elements(By.CSS_SELECTOR, "div[class='inventory_item_name']")
for product in products:
    print(product.text)

driver.close()




"""
Automate Data Extraction from Pro Kabaddi Standings**

### Description

Open the Pro Kabaddi website using Selenium WebDriver (https://www.prokabaddi.com/)
Navigate to the **Standings** section and locate the team **Jaipur Pink Panthers** in the points table.

Identify and extract the following details for the team:

* Matches Played
* Won
* Lost
* Score Difference (Diff)
* Points

Use appropriate locator strategies such as **XPath / CSS Selectors** to fetch the data dynamically from the table.
"""

from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()

driver.get("https://www.prokabaddi.com/")
sleep(2)
standings = driver.find_element(By.XPATH, "//span[text()='Standings']")
standings.click()
sleep(2)
team = driver.find_element(By.XPATH, "//p[text()='Jaipur Pink Panthers']")
matches = driver.find_element(By.XPATH, "//p[.='Jaipur Pink Panthers']/../../..//following-sibling::div")
won = driver.find_element(By.XPATH, "//p[.='Jaipur Pink Panthers']/../../..//following-sibling::div[2]")
lost = driver.find_element(By.XPATH, "//p[.='Jaipur Pink Panthers']/../../..//following-sibling::div[3]")
diff = driver.find_element(By.XPATH, "//p[.='Jaipur Pink Panthers']/../../..//following-sibling::div[4]")
points = driver.find_element(By.XPATH, "//p[.='Jaipur Pink Panthers']/../../..//following-sibling::div[5]")
print(team.text)
print(matches.text)
print(won.text)
print(lost.text)
print(diff.text)
driver.quit()
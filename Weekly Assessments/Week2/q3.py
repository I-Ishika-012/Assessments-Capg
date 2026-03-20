"""


### Title
**Automate Resume Upload on Shine Registration Page**

### Description
Open the Shine registration page using Selenium WebDriver (https://www.shine.com/registration/).

Automate the process of uploading a resume file using Selenium.

Perform the following steps:
- Launch the browser and open the Shine registration page
- Locate the **Upload Resume** file input field
- Upload a resume file
"""
from time import sleep

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

opt = ChromeOptions()
opt.add_experimental_option("detach", True)
driver = Chrome(options=opt)
driver.maximize_window()
driver.get("https://www.shine.com/registration/")
sleep(3)
resume = driver.find_element(By.ID, "id_file")
resume.send_keys(r"C:\Users\Hp\Downloads\Ishika_Turing_BA.pdf")
driver.quit()


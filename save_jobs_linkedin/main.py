import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("/Users/sidakveersingh/Desktop/development/chromedriver")
browser = webdriver.Chrome(service=service)
browser.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=101330853&keywords=python%20developer&location=Montreal%2C%20Quebec%2C%20Canada")

sign_in = browser.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()


username = browser.find_element(By.ID, "username")
username.send_keys("Your username")

password = browser.find_element(By.ID, "password")
password.send_keys("YOUR PASS")

sign_in1 = browser.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in1.click()

time.sleep(2)

jobs = browser.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for x in jobs:
    x.click()
    time.sleep(2)
    save = browser.find_element(By.CSS_SELECTOR, ".jobs-save-button")
    save.click()
    time.sleep(2)
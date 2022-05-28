from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("/Users/sidakveersingh/Desktop/development/chromedriver")
browser = webdriver.Chrome(service=service)
browser.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = browser.find_element(By.ID, "cookie")
money = browser.find_element(By.ID, "money")
while True:
    cookie.click()



# browser.quit()
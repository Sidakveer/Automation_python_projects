from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service("/Users/")
browser = webdriver.Chrome(service=service)
browser.get("http://orteil.dashnet.org/experiments/cookie/")


cookie = browser.find_element(By.ID, "cookie")


def upgrade():
    money = int(browser.find_element(By.ID, "money").text.replace(",", ""))
    upgrade_list = browser.find_elements(By.CSS_SELECTOR, "#store b")
    dict1 = {}
    for x in upgrade_list[:-1]:
        parts = x.text.split(" - ")
        name = parts[0]
        price = int(parts[1].replace(",", ""))
        dict1[name] = price

    available_upgrades = [x for x in dict1 if money > dict1[x]]
    print(available_upgrades)
    if available_upgrades:
        max_upgrade = available_upgrades[-1]
        browser.find_element(By.ID, f"buy{max_upgrade}").click()


timeout = time.time() + 5
five_min = time.time() + (60 * 5)

while True:
    cookie.click()
    if time.time() > timeout:
        upgrade()
        timeout = time.time() + 5

    if time.time() > five_min:
        cps = browser.find_element(By.ID, "cps")
        print("Cookies/Second: ", cps.text)
        browser.quit()
        break

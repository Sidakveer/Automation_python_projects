from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "/Users//Desktop/development/chromedriver"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")


time_list = driver.find_elements(By.CSS_SELECTOR, '.last .menu time')


article_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu a")


dict1 = {}
final_dict = {} 
for x in range(len(time_list)):
    dict1["name"] = article_list[x].text
    dict1["time"] = time_list[x].text
    final_dict[x] = dict1
    
print(final_dict)

driver.quit()

#================================================

#more rough code

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

service = Service("/Users/sidakveersingh/Desktop/development/chromedriver")
browser = webdriver.Chrome(service=service)
browser.get("https://en.wikipedia.org/wiki/Main_Page")

element = browser.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# element.click()

all_portals = browser.find_element(By.LINK_TEXT, "Contact us")
# all_portals.click()

search = browser.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

# browser.quit()
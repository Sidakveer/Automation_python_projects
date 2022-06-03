import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSfomuF_5p9zTms9t4KzlyHel2LmXSvnSQGn-tRUnl5nnYZo5A/viewform?usp=sf_link'
ZILLOW_LINK = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearch' \
              'Term%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37' \
              '.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'


header = {
    "User-Agent": "Mozi.36",
    "Accept-Language": "en-"
}

response = requests.get(url=ZILLOW_LINK, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

addresses = soup.find_all(name="address", class_="list-card-addr")
links = soup.find_all(class_="list-card-link list-card-link-top-margin")
prices = soup.find_all(name="div", class_="list-card-price")


addr_list = [x.text for x in addresses]
price_list = [x.text.split("+")[0].replace("/mo", '') for x in prices]
link_list = [x.get('href').split("+")[0].replace("/b", "https://www.zillow.com/b") for x in links]


# Use selenium to fill out google form
service = Service(executable_path="/Users//Desktop/development/chromedriver")
browser = webdriver.Chrome(service=service)
browser.get(FORM_LINK)


time.sleep(2)
for x in range(len(link_list)):
    first = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    first.send_keys(addr_list[x])
    time.sleep(1)
    second = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second.send_keys(price_list[x])
    time.sleep(1)
    third = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third.send_keys(link_list[x])
    time.sleep(1)
    submit = browser.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    time.sleep(2)
    browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
    time.sleep(1)






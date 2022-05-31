import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException

PROMISED_DOWN = 150.0
PROMISED_UP = 150.0
TWITTER_USERNAME = ""
TWITTER_PASSWORD = ""


class InternetSpeedTwitterBot:

    def __init__(self):
        self.up = 0
        self.down = 0
        service = Service(executable_path="your Path")
        self.browser = webdriver.Chrome(service=service)

    def get_internet_speed(self):
        self.browser.get("https://www.speedtest.net/")
        click = self.browser.find_element(By.CLASS_NAME, "start-text")
        click.click()
        time.sleep(45)
        self.down = self.browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.browser.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text



    def tweet_at_provider(self):
        if float(self.down) < PROMISED_DOWN and float(self.up) < PROMISED_UP:
            self.browser.get("https://twitter.com/compose/tweet")
            time.sleep(2)
            username = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
            username.send_keys(TWITTER_USERNAME)
            self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span').click()

            time.sleep(2)
            password = self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/div/label/div/div[2]/div[1]/input')
            password.send_keys(TWITTER_PASSWORD)
            self.browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span/span').click()

            time.sleep(5)
            tweet = self.browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            msg = f"Hey why is my internet speed only {self.down}/{self.up} when I was promised {PROMISED_DOWN}/{PROMISED_UP}"
            tweet.send_keys(msg)

if __name__ == '__main__':
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()
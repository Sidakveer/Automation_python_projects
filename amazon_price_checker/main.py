import requests
from bs4 import BeautifulSoup
import smtplib

amazon_url = "https://www.amazon.com/CHEF-Worlds-Smartest-Pressure-Cooker/dp/B0863JB424/ref=sr_1_2_sspa?crid=3PR59893J12ZT&keywords=electric+cooker&qid=1653599368&sprefix=electric+cooke%2Caps%2C108&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyU1JRUE4wN0ZOVUtKJmVuY3J5cHRlZElkPUEwMTE3MTQwNDJEREtJNk4wQlQ0JmVuY3J5cHRlZEFkSWQ9QTA5NDQ5MTIxMkE0SlRZNDE5QksxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36",
    "Accept-Language": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}
response = requests.get(amazon_url, headers=headers)
html_text = response.text
# print(html_text)

soup = BeautifulSoup(html_text, "html.parser")
price_str = soup.find(name="span", class_="a-offscreen").getText()
price = float(price_str.strip("$"))

password = "your email password"
username = "your email"

if price < 100:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr=username, to_addrs=username, msg=f"Subject:Price Alert\n\nPrice below 100 dollars\n{amazon_url}")
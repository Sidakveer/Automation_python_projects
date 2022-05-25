from bs4 import BeautifulSoup
import requests


response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
html_text = response.text

soup = BeautifulSoup(html_text, "html.parser")
title_list = []
for title in soup.find_all(name="h3", class_="title"):
    try:
        title_1 = title.getText().split(") ")[1]
        title_list.append(title_1)
    except IndexError:
        title_1 = title.getText().split(": ")[1]
        title_list.append(title_1)

print(title_list)

with open("movies.txt", "w", encoding="utf-8") as file:
    for index, movie in enumerate(title_list[::-1]):
        file.write(f"{index + 1} {movie}\n")
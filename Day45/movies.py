from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

soup = BeautifulSoup(response.text, "html.parser")
movies_parse = soup.find_all(name="h3", class_="title")
movies = [f"{movie.getText()}\n" for movie in movies_parse]
movies.reverse()

with open("Day45/movies.txt", "w", encoding="utf-8") as file:
    file.writelines(movies)
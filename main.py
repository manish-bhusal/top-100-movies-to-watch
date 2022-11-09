import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
top_100 = response.text

soup = BeautifulSoup(top_100, "html.parser")
movies = soup.select(selector=".article-title-description__text .title")
movie_titles = [movie.getText() for movie in movies][::-1]

with open("movies.txt", mode="w", encoding="utf8") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")

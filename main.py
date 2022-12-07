from bs4 import BeautifulSoup
import requests

url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
movie_web_page = response.text

soup = BeautifulSoup(movie_web_page, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
# print(article)
movie_list = [movie.getText() for movie in all_movies]
movies_rank = movie_list[::-1]
for n in range(len(movie_list)-1, -1, -1):
    print(movie_list[n])
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies_rank:
        file.write(f"{movie}\n")

# print(movies_rank)

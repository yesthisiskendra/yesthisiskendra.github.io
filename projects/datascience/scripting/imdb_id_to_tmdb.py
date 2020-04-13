import requests
import json
import csv
import pandas as pd
from urllib.parse import quote


def write_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('2018_movies_withbudget.csv', index=False)


headers = {'Accept-Language': 'en-US'}
payload = "{}"

all_movie_data = []
with open('tmdb_csv_0820_2018_withbudget.csv', encoding='utf-8') as csvfile:
    movies = csv.reader(csvfile)
    for movie in movies:
        try:
            url = "https://api.themoviedb.org/3/movie/"
            thing_looking_for = movie[1]
            my_api_key = "?api_key=cabf7122b6e3f7885485741c38d3df19"
            full_url = url + thing_looking_for + my_api_key
            res = requests.get(full_url, payload, headers=headers)
            data = res.content.decode('UTF-8')
            jdata = json.loads(data)
            try:
                title = jdata['title']
                budget = jdata['budget']
                genres = jdata['genres']
                production_companies = jdata['production_companies']
                release_date = jdata['release_date']
                revenue = jdata['revenue']
                profit = revenue - budget
                popularity = jdata['popularity']
                vote_average = jdata['vote_average']
                vote_count = jdata['vote_count']
            except KeyError:
                title = 'NA'
                budget = 'NA'
                genres = 'NA'
                production_companies = 'NA'
                release_date = 'NA'
                revenue = 'NA'
                profit = 'NA'
                popularity = 'NA'
                vote_average = 'NA'
                vote_count = 'NA'

            movie_data = {
                'release_date': release_date,
                'title': title,
                'budget': budget,
                'genres': genres,
                'production_companies': production_companies,
                'revenue': revenue,
                'profit': profit,
                'popularity': popularity,
                'vote_average': vote_average,
                'vote_count': vote_count
            }
            all_movie_data.append(movie_data)
        except UnicodeDecodeError:
            director_data = {}
all_movie_data_df = pd.DataFrame(all_movie_data)
print(all_movie_data_df)
write_csv(all_movie_data)

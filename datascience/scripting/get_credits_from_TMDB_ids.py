# INPUT: LIST OF TMDB MOVIE IDS
# OUTPUT: A CSV OF THE CAST & CREW FOR EACH MOVIE

import requests
import json
import csv
import pandas as pd
from urllib.parse import quote

# CHANGE THIS TO MATCH OUR INPUT FILE!
input_csv = 'tmdb_test_small.csv'
output_csv = input_csv.split('.')[0] + '_results.csv'

api_key = open('tmdb_api_key.txt')
api_key = api_key.read()


def write_csv(data):
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)


headers = {'Accept-Language': 'en-US'}
payload = "{}"

all_movie_data = []


def get_info_from_TMDB(movies):
    for movie in movies:
        try:
            url = 'https://api.themoviedb.org/3/movie/'

            # LINE TO MODIFY DEPENDING ON WHAT WE'RE GETTING!!
            # Currently getting credits :)
            thing_looking_for = movie[1] + '/credits'
            my_api_key = '?api_key=' + api_key
            full_url = url + thing_looking_for + my_api_key
            res = requests.get(full_url, payload, headers=headers)
            data = res.content.decode('UTF-8')
            jdata = json.loads(data)
            jdata['movie'] = movie
            all_movie_data.append(jdata)
        except:
            print('oops!')
    write_csv(all_movie_data)


with open(input_csv, encoding='utf-8') as csvfile:
    movies = csv.reader(csvfile)
    next(movies, None)
    get_info_from_TMDB(movies)

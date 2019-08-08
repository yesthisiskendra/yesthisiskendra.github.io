import http.client
import json
import csv
import pandas as pd


def write_csv(data):
    df = pd.DataFrame(data)
    df.to_csv('initial.csv', index=False)


conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

all_data = []
for num in range(1, 2):
    print(num)
    conn.request("GET", "/3/discover/movie?release_date.lte=2019-08-07&release_date.gte=1970-01-01&page=" + str(num) +
                 "&include_video=false&include_adult=false&sort_by=popularity.desc&language=en-US&api_key=" + api_key +, payload)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

    all_data.append(data.decode("utf-8"))

    # not done
    # movie_data = {'title': actor, 'gender': gender, 'popularity': popularity,
    #   'birthday': birthday, 'placeofbirth': placeofbirth, 'imdb_id': imdb_id}
    all_data.append(movie_data)

# write_csv(all_actor_data)

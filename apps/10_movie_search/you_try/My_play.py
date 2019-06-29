import requests
import collections

MovieResult = collections.namedtuple('MovieResult', "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")

search = input("What movie do you want to search for? ")

url = 'http://movie_service.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)

resp.raise_for_status()

movie_data = resp.json()
movies_list = movie_data.get('hits')

# movies = []

# for md in movies_list:
#     m = MovieResult(
#          imdb_code=md.get('imdb_code'),
#          title=md.get('title'),
#          duration=md.get('duration'),
#          director=md.get('director'),
#          year=md.get('year', 0),
#          rating=md.get('rating', 0),
#          imdb_score=md.get('imdb_score', 0.0),
#          keywords=md.get('keywords'),
#          genres=md.get('genres')
#      )
#     movies.append(m)


# def method(x, y, z, **kwargs):
#     print("kwargs=", kwargs)

# HUOMAA: Että parametrinä syötetty **kwargs tuottaa dictionaryn jossa k:v-pareina on
# annetut format: True ja age: 7 parit!!!
# method(7, 1, z=2, format=True, age=7)

"""HUOMAA: Yllä mainittu voidaan tehdä myös toisin päin, eli
tuottaa dictionarystä kwargs!!! Tässä tapauksessa alla oleva namedtuple-looppi
tuottaa tiedon dict-muodossa (esim. {title: 'title', year: 'year'}.
Siten MovieResultsin parametrin voidaan korvata **md:llä."""

#movies = []

#for md in movies_list:
#    m = MovieResult(**md)
#    movies.append(m)

"""HUOMAA: Tätä voidaan kuitenkin edelleen parantaa muuttamalla for-looppi
list comprehensioniksi:"""

movies = [MovieResult(**md) for md in movies_list
    ]


print('found {} movies for search {}'.format(len(movies), search))

for m in movies:
    print('{} -- {}'.format(m.year, m.title))


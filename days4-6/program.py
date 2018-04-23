import collections
import requests
import csv


def main():
    movies = get_movie_list()
    qualify_directors(movies)


def get_movie_list():
    url = 'https://raw.githubusercontent.com/sundeepblue/' \
          'movie_rating_prediction/master/movie_metadata.csv'
    r = requests.get(url)
    movies = list(csv.DictReader(r.content.decode('utf-8').splitlines()))
    for index, movie in enumerate(movies):
        movies[index] = collections.OrderedDict([
            ('director_name', movie['director_name']),
            ('movie_title', movie['movie_title']),
            ('title_year', movie['title_year']),
            ('imdb_score', movie['imdb_score']),
        ])
    return movies


def qualify_directors(movies):
    movie_count = collections.Counter([x['director_name'] for x in movies])
    print(movie_count.most_common(5))


if __name__ == '__main__':
    main()

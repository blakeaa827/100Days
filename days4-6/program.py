import collections
import math
import statistics

import requests
import csv


def main():
    movies = get_movie_list()
    experienced_directors = qualify_directors(movies, 4)
    movies_by_director = sort_movies_by_director(movies, experienced_directors)
    rated_directors = rate_directors(movies_by_director)
    display_top_directors(rated_directors, movies_by_director)
    # for director, rating in rated_directors.items():
    #     print(f"{director}'s avg rating is {rating:.1f}.")

def get_movie_list():
    url = 'https://raw.githubusercontent.com/sundeepblue/' \
          'movie_rating_prediction/master/movie_metadata.csv'
    r = requests.get(url)
    movies = list(csv.DictReader(r.content.decode('utf-8').splitlines()))
    processed_movies = list()
    for index, movie in enumerate(movies):
        for key, value in movie.items():
            movie[key] = value.replace(u'\xa0', '')
            movie[key] = value.strip()

        try:
            if int(movie['title_year']) < 1960:
                # print(f"Skipping {movie['movie_title']} - "
                #       f"{movie['title_year']}")
                continue
        except ValueError:
            # print(f"Skipping {movie['movie_title']}. "
            #       f"Unknown year.")
            # break
            pass

        if not movie['director_name']:
            # print(f"Skipping {movie['movie_title']}. "
            #       f"Unknown director.")
            continue

        processed_movies.append(collections.OrderedDict([
            ('director_name', movie['director_name'].strip()),
            ('movie_title', movie['movie_title'].rstrip(u'\xa0').strip()),
            ('title_year', movie['title_year'].strip()),
            ('imdb_score', movie['imdb_score'].strip()),
        ]))
    return processed_movies


def qualify_directors(movies, required_count):
    movie_count = collections.Counter([x['director_name'] for x in movies])
    directors = [director
                 for director, count in movie_count.items()
                 if count >= required_count]
    return directors


def sort_movies_by_director(movies, directors):
    sorted_movies = dict()
    for director in directors:
        sorted_movies[director] = sorted([
            movie
            for movie in movies
            if movie['director_name'] == director],
            key=lambda movie: float(movie['imdb_score']), reverse=True)
    return sorted_movies


def rate_directors(movies_by_director):
    rated_directors = collections.OrderedDict()
    for director, movies in movies_by_director.items():
        rated_directors[director] = statistics.mean(
            [float(x['imdb_score']) for x in movies]
        )
    rated_directors = collections.OrderedDict(sorted(
        rated_directors.items(), key=lambda director: director[1],
        reverse=True
    ))
    return rated_directors


def display_top_directors(rated_directors, movies_by_director, top=20):
    top_directors = [director for i, director
                     in enumerate(rated_directors.keys())
                     if i < top]
    for i, director in enumerate(top_directors):
        print(f"{i+1:2.0f}. {director}:     "
              f"average rating = {rated_directors[director]:1.1f}")
        print('------------------------------------------------------')
        for movie in movies_by_director[director]:
            print(f"    {movie['title_year']}] {movie['movie_title']}: "
                  f"{movie['imdb_score']}")
        print()


if __name__ == '__main__':
    main()

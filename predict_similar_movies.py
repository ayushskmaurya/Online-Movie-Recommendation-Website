import pandas as pd

# Reading prepared dataset.
movie_pre_info = pd.read_csv('prepared_data/movie_pre_info.csv')

year_diff = 2019 - 1950
movie_pre_info['year_of_release'] = pd.to_numeric(movie_pre_info['year_of_release'], errors='coerce')


# Returning genres, actors and released date of the movie.
def get_info(title):
    row = movie_pre_info[movie_pre_info['title'].str.lower() == title.lower()]
    data = next(row.iterrows(), None)
    
    if data is not None:
        genres = data[1].genres.split("|")
        actors = data[1].actors.split("|")[:-1]
        return {
            "genres": genres,
            "actors": actors,
			"imdb_rating": int(data[1].imdb_rating),
            "year_of_release": int(data[1].year_of_release),
            "genre_count": len(genres),
            "actor_count": len(actors)
        }
    
    else:
        return None


# Calculating the probability of similarity between the movies.
def probability(row, info):    
    counts = {'genre': 0, 'actor': 0}
    
    for genre in info['genres']:
        if genre in row[1]:
            counts['genre'] += 1
    
    for actor in info['actors']:
        if actor in row[2]:
            counts['actor'] += 1
    
    counts['diff_year'] = abs(info['year_of_release'] -  row[4])
        
    p = 0.45 * (counts['genre'] / info['genre_count'])
    p += 0.25 * (counts['actor'] / info['actor_count'])
    p += 0.2 * (row[3] / 10)
    p += 0.1 * (1 - (counts['diff_year'] / year_diff))
    return  p


# Getting top 10 similar movies.
def get_similar_movies(title):
    info = get_info(title)
    if info is not None:
        movie_pre_info['p'] = movie_pre_info.apply(lambda row: probability(row, info), axis=1)
        pre_movies = movie_pre_info[movie_pre_info['title'].str.lower() != title.lower()]
        return pre_movies.nlargest(10, 'p')
    else:
        return "No movie found!"

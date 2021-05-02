from flask import Flask, render_template, request, jsonify
import pandas as pd
import predict_similar_movies

app = Flask(__name__)
pd.set_option('display.max_colwidth', None)


# Show top rated 5 movies while searching
@app.route("/show_movies", methods=['POST'])
def show_movies():
	text = request.form['text']

	mdetails = pd.read_csv('prepared_data/movie_details.csv')
	movies = mdetails[mdetails['title'].str.match("(?i)" + text)]
	movies = movies.nlargest(5, 'imdb_rating')
	
	return jsonify(movies['title'].tolist())


# Returning details of particular movie
def get_info(mdetails, title):
    row = mdetails[mdetails['title'].str.lower() == title.lower()]
    data = next(row.iterrows(), None)
    
    if data is not None:
        return {
            "title": data[1].title,
            "genres": data[1].genres,
            "actors": data[1].actors,
            "release_date": data[1].release_date,
            "imdb_rating": data[1].imdb_rating,
            "summary": data[1].summary,
            "poster_path": data[1].poster_path,
            "wiki_link": data[1].wiki_link
        }
    
    else:
        return "0"


# Retrieving movie details from prepared csv file
@app.route("/movie_details", methods=['POST'])
def movie_details():
	title = request.form['title']
	mdetails = pd.read_csv('prepared_data/movie_details.csv')
	return get_info(mdetails, title)


# Retrieving poster paths
def get_poster_path(mdetails, movies):
	paths = {}
	for movie in movies:
		mdata = mdetails[mdetails['title'] == movie]
		if not mdata.empty:
			paths[movie] = mdata.poster_path.to_string(index=False)
		else:
			paths[movie] = "#"

	return paths


# Getting top 10 similar movies.
@app.route("/similar_movies", methods=['POST'])
def similar_movies():
	title = request.form['title']

	mdetails = pd.read_csv('prepared_data/movie_details.csv')        
	movies = predict_similar_movies.get_similar_movies(title)['title'].tolist()

	return get_poster_path(mdetails, movies)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/search")
def search():
	return render_template("search.html")


@app.route("/how_it_works")
def how_it_works():
	return render_template("how_it_works.html")


if __name__ == '__main__':
	app.run()

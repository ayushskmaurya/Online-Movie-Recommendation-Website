from flask import Flask, render_template, request, jsonify
import pandas as pd
app = Flask(__name__)


# Show top 5 rated movies while searching
@app.route("/show_movies", methods=['POST'])
def show_movies():
	text = request.form['text']

	movie_pre_info = pd.read_csv('prepared_data/movie_details.csv')
	movies = movie_pre_info[movie_pre_info['title'].str.match("(?i)" + text)]
	movies = movies.nlargest(5, 'imdb_rating')
	
	return jsonify(movies['title'].tolist())


# Returning details of particular movie
def get_info(movie_pre_info, title):
    row = movie_pre_info[movie_pre_info['title'].str.lower() == title.lower()]
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
	movie_pre_info = pd.read_csv('prepared_data/movie_details.csv')
	return get_info(movie_pre_info, title)


@app.route("/")
def index():
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)

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


@app.route("/")
def index():
	return render_template("index.html")


if __name__ == '__main__':
	app.run(debug=True)

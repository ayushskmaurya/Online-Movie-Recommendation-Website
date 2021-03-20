// Show top 5 rated movies while searching
function show_movies(text) {
	if(text.length >= 3) {
		$.ajax({
			url: "/show_movies",
			method: "POST",
			data: {text:text},
			success: function(movies) {
				document.getElementById("movies").innerHTML = "";
				for(let i in movies) {
					let div = document.createElement("DIV");
					div.innerHTML = "<button type='button' class='movie' onclick='search(this.value);' value='" + movies[i] + "'>" + movies[i] + "</button>";
					document.getElementById("movies").appendChild(div);
				}
			}
		});
		document.getElementById("movies").style.display = "block";
	}
	else
		document.getElementById("movies").style.display = "none";
}

// Getting movie name and searching for movie details
function movie_name() {
	let title = document.getElementById("title").value.trim();
	search(title);
}

// Retrieving movie details from prepared csv file
function search(title) {
	$.ajax({
		url: "/movie_details",
		method: "POST",
		data: {title:title},
		success: function(data) {
			if(data != "0") {
				document.getElementById("title").value = "";
				document.getElementById("movies").style.display = "none";
				document.getElementById("movie-poster").src = data['poster_path'];
				document.getElementById("movie-poster").alt = data['title'];
				document.getElementById("movie-title").innerHTML = data['title'];
				document.getElementById("movie-genres").innerHTML = data['genres'];
				document.getElementById("movie-imdb-rating").innerHTML = data['imdb_rating'];
				document.getElementById("movie-release-date").innerHTML = data['release_date'];
				document.getElementById("movie-cast").innerHTML = data['actors'];
				document.getElementById("movie-summary").innerHTML = data['summary'];
				document.getElementById("wiki").href = data['wiki_link'];
			}
		}
	});
}

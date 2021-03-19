function show_movies(text) {
	if(text.length >= 3)
		document.getElementById("movies").style.display = "block";
	else
		document.getElementById("movies").style.display = "none";
}

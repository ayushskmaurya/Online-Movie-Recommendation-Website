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
					div.innerHTML = "<button class='movie'>" + movies[i] + "</button>";
					document.getElementById("movies").appendChild(div);
				}
			}
		});
		document.getElementById("movies").style.display = "block";
	}
	else
		document.getElementById("movies").style.display = "none";
}

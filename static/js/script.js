function page(id) {
	for(let i=0; i<3; i++) {
		document.getElementsByClassName("menu-opt")[i].style.fontWeight = "normal";
	}
	document.getElementById(id).style.fontWeight = "500";
}

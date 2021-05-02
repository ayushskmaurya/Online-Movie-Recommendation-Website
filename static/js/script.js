// Changing the font weight of the active page.
let pathname = window.location.pathname;
let id = "btn-" + pathname.substring(1);
document.getElementById(id).style.fontWeight = "500";

// Redirecting to other page.
function page(id) {
	location.href = "/" + id.substring(4);
}

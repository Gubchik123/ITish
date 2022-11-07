const toggleBtn = document.querySelector("#toggle-theme");

toggleBtn.addEventListener("click", function () {
	if (document.documentElement.hasAttribute("theme")) {
		toggleBtn.children[0].name = "moon";
		sessionStorage.setItem("dark-theme", "no");
		document.documentElement.removeAttribute("theme");
	} else {
		set_dark_mode();
	}
});

function set_dark_mode() {
	toggleBtn.children[0].name = "sunny";
	sessionStorage.setItem("dark-theme", "yes");
	document.documentElement.setAttribute("theme", "dark");
}

if (sessionStorage.getItem("dark-theme") == "yes") set_dark_mode();
else toggleBtn.children[0].name = "moon";

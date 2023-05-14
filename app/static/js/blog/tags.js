const badge_bg_colors = [
	"dark",
	"info",
	"light",
	"danger",
	"primary",
	"warning",
	"success",
	"secondary",
];

function make_tags_smaller() {
	if (window.outerWidth <= 576) {
		for (const tag of document.querySelectorAll(".badge"))
			tag.style.fontSize = "1em";
	}
}

for (const tag of document.querySelectorAll(".badge")) {
	tag.style.fontSize =
		window.outerWidth > 576 ? `${Math.random() * 1 + 1}em` : "1em";
	tag.classList += ` text-bg-${
		badge_bg_colors[Math.floor(Math.random() * badge_bg_colors.length)]
	}`;
}

window.addEventListener("resize", make_tags_smaller);
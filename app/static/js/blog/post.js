// For post likes
const like_icon = document.querySelector("#like-icon");
const like_count = document.querySelector("#like-count");

const like_btn = document.querySelector("#like-button");
like_btn.addEventListener("click", function () {
	if (like_icon.name == "heart-outline") {
		like_icon.name = "heart";
		like_count.innerText = +like_count.innerText + 1;
	} else {
		like_icon.name = "heart-outline";
		like_count.innerText = +like_count.innerText - 1;
	}

	fetch(`./${post_url}/like`, {
		method: "POST",
		headers: {
			Accept: "application/json",
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			post_id: post_id, // Jinja2 variable from template
			user_id: user_id, // Jinja2 variable from template
		}),
	});
});

// For post comments
function ask_before_deleting(e) {
	let answer = confirm("Do you really want to delete this comment?");
	if (!answer) e.preventDefault();
}

for (const btn of document.querySelectorAll(".delete-comment-btn"))
	btn.addEventListener("click", ask_before_deleting);

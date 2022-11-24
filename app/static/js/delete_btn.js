for (const btn of document.querySelectorAll(".delete-btn"))
	btn.addEventListener("click", function (e) {
		let answer = confirm("Do you really want to delete this item?");
		if (!answer) e.preventDefault();
	});

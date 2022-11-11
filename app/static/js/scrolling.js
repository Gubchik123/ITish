// When the user scrolls down 200px from the top of the document, show the button
window.onscroll = function () {
	if (
		document.body.scrollTop > 200 ||
		document.documentElement.scrollTop > 200
	) {
		go_to_top_btn.classList =
			"rounded-circle d-flex justify-content-center align-items-center";
	} else {
		go_to_top_btn.classList = "";
	}
};

const go_to_top_btn = document.getElementById("go-to-top-btn");
go_to_top_btn.addEventListener("click", function () {
	document.body.scrollTop = 0; // For Safari
	document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and
});

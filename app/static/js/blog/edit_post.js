// * Global scope - start
const content_block = document.querySelector(".content");

const hidden_post_title_field = document.getElementById("post_title");
const hidden_post_body_field = document.getElementById("post_body");

const post_tags_field = document.getElementById("post_tags");

const create_post_btn = document.getElementById("post_submit");
create_post_btn.addEventListener("click", get_click_event_on_create_post_btn);

let apply_btn, cancel_btn;

if (content_block.previousElementSibling.tagName != "H2")
	add_post_title_input_field();
// * Global scope - end

// * Element processing functions - start
function warning(target) {
	target.style.border = "2px solid red";
}

function set_for_(area, id, placeholder) {
	area.id = id;
	area.placeholder = placeholder;
}
// * Element processing functions - end

// * Event functions - start
function get_click_event_on_create_post_btn() {
	// TODO: Event for button which create post and send data on the server
}

function get_click_event_on_apply_btn() {
	let check = true;
	let parent = apply_btn.parentElement;

	console.log(parent);

	for (let field of parent.querySelectorAll(".form-control")) {
		if (field.value == "") {
			warning(field);
			check = false;
		}
	}

	console.log(check);

	if (check) {
		content_block.removeChild(parent);
		add_needed_element_with_data_from(parent);
	}
}

function get_click_event_on_cancel_btn() {
	content_block.removeChild(cancel_btn.parentElement);
}

function get_click_event_on_close_btn(e) {
	let answer = confirm("Do you really want to delete this element?");
	if (answer) {
		let parent = e.target.parentElement;

		if (parent.id == "title") {
			let row_content_block = document.querySelector(".content_block");
			row_content_block.removeChild(parent);
			add_post_title_input_field();
		} else content_block.removeChild(parent);
	} else e.preventDefault();
}

function set_click_event_for_apply_btn() {
	apply_btn = content_block.querySelector(".btn.apply");
	if (apply_btn)
		apply_btn.addEventListener("click", get_click_event_on_apply_btn);
}

function set_click_event_for_cancel_btn() {
	cancel_btn = document.querySelector(".btn.cancel");
	if (cancel_btn)
		cancel_btn.addEventListener("click", get_click_event_on_cancel_btn);
}

function add_mouse_over_and_leave_event_for_(block) {
	block.addEventListener("mouseover", function () {
		block.classList.add("border");
		block.classList.add("border-info");

		let close_btn = block.querySelector(".btn-close");
		close_btn.style.display = "flex";
	});

	block.addEventListener("mouseleave", function () {
		block.classList.remove("border");
		block.classList.remove("border-info");

		let close_btn = block.querySelector(".btn-close");
		close_btn.style.display = "none";
	});

	return block;
}
// * Event functions - end

// * Getting improved element function - start
function get_nested_(element) {
	let block = get_div_block();
	block.classList = "mb-2 p-1 d-flex justify-content-between";
	block.appendChild(element);

	block = add_mouse_over_and_leave_event_for_(block);

	return block;
}
// * Getting improved element function - end

// * Get element functions - start
function get_input_area_(tag, id, placeholder) {
	let input_area = document.createElement(tag);
	input_area.classList = "form-control me-2 float_left";

	set_for_(input_area, id, placeholder);

	return input_area;
}

function get_div_block() {
	return document.createElement("div");
}

function get_btn_with_(inner_html, classList) {
	let button = document.createElement("button");
	button.innerHTML = inner_html;
	button.classList = classList;

	return button;
}

function get_apply_btn() {
	return get_btn_with_(
		"<ion-icon name='checkmark-outline'></ion-icon>",
		"btn apply btn-success btn-sm mb-2 me-2 float_left d-flex justify-content-center align-items-center"
	);
}

function get_cancel_btn() {
	return get_btn_with_(
		"<ion-icon name='close-outline'></ion-icon>",
		"btn cancel btn-danger btn-sm mb-2 d-flex justify-content-center align-items-center"
	);
}

function get_close_btn() {
	let close_btn = get_btn_with_("", "btn-close m-2");
	close_btn.addEventListener("click", get_click_event_on_close_btn);
	close_btn.style.display = "none";
	return close_btn;
}
// * Get element functions - end

// * Adding content functions - start
function add_post_title_input_field() {
	let block = get_div_block();
	block.id = "post_title_field";
	block.classList = "my-3";

	block.appendChild(get_input_area_("input", "title", "Post title"));
	block.appendChild(get_apply_btn());

	content_block.prepend(block);
	set_click_event_for_apply_btn();
}

function add_post_title_from_(text) {
	hidden_post_title_field.value = text;

	let title = document.createElement("h2");
	title.innerText = text;

	let title_block = get_nested_(title);
	title_block.id = "title";
	title_block.appendChild(get_close_btn());

	content_block.before(title_block);
}

function add_needed_element_with_data_from(parent) {
	if (parent.id == "post_title_field")
		add_post_title_from_(parent.children[0].value);
}
// * Adding content functions - end

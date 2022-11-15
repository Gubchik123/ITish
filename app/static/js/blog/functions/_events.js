import { check_filling_of_ } from "./_processing.js";
import { content_block } from "../_global_variables.js";
import { title, add_needed_element_with_data_from } from "../create_post.js";

export function get_click_event_on_create_post_btn() {
	// TODO: Event for button which create post and send data on the server
}

export function get_click_event_on_apply_btn() {
	let element_form = content_block.querySelector(".element-form");

	if (check_filling_of_(element_form)) {
		add_needed_element_with_data_from(element_form);
		content_block.removeChild(element_form);
	}
}

export function get_click_event_on_cancel_btn() {
	content_block.removeChild(
		document.querySelector(".btn.cancel").parentElement
	);
}

export function get_click_event_on_close_btn(e) {
	let answer = confirm("Do you really want to delete this element?");
	if (answer) {
		let element = e.target.parentElement;

		while (!element.classList.toString().includes("element "))
			element = element.parentElement;

		if (element.id == "title") {
			let row_content_block = document.querySelector(".content_block");
			row_content_block.removeChild(element);
			title.add_form_for_getting_element_data();
		} else content_block.removeChild(element);
	} else e.preventDefault();
}

export function get_click_event_on_align_btn(e, align) {
	let element_btns_block =
		e.target.tagName == "BUTTON"
			? e.target.parentElement.parentElement
			: e.target.parentElement.parentElement.parentElement;

	let class_list = element_btns_block.previousElementSibling.classList;

	for (const position of ["start", "center", "end"]) {
		if (class_list.toString().includes(position)) {
            if (position == align) break;
			element_btns_block.previousElementSibling.classList = class_list
				.toString()
				.replace(new RegExp(`${position}`, 'g'), align);
			break;
		}
	}
}

export function set_click_event_for_apply_btn() {
	let apply_btn = content_block.querySelector(".btn.apply");
	if (apply_btn)
		apply_btn.addEventListener("click", get_click_event_on_apply_btn);
}

export function set_click_event_for_cancel_btn() {
	let cancel_btn = document.querySelector(".btn.cancel");
	if (cancel_btn)
		cancel_btn.addEventListener("click", get_click_event_on_cancel_btn);
}

export function add_mouse_over_and_leave_event_for_(block) {
	block.addEventListener("mouseover", function () {
		block.classList.add("border");
		block.classList.add("border-info");

		block.querySelector(".element-btns").style.display = "flex";
	});

	block.addEventListener("mouseleave", function () {
		block.classList.remove("border");
		block.classList.remove("border-info");

		block.querySelector(".element-btns").style.display = "none";
	});

	return block;
}

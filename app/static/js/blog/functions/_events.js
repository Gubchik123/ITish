import {
	title,
	add_needed_element_with_data_from,
	get_needed_element_from_,
} from "../create_post.js";

import { check_filling_of_ } from "./_processing.js";
import { content_block, hidden_post_body_field } from "../_global_variables.js";
import { get_div_block } from "./_getting.js";

export function get_click_event_on_create_post_btn(e) {
	if (
		content_block.innerHTML.length != 0 &&
		!content_block.querySelector(".element-form")
	) {
		for (let element_content of content_block.querySelectorAll(
			".element-content"
		)) {
			let element = get_div_block();
			element.appendChild(element_content);
			hidden_post_body_field.value += element.innerHTML;
		}
	} else e.preventDefault();
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

function _get_element_value_from_(element_content) {
	let id = element_content.classList[1];

	if (id == "subtitle1") return element_content.querySelector("h2").innerText;
	else if (id == "subtitle2")
		return element_content.querySelector("h4").innerText;
	else if (id == "paragraph")
		return element_content.querySelector("p").innerText;
	else if (id == "link")
		return [
			element_content.querySelector("a").innerText,
			element_content.querySelector("a").href,
		];
	else if (id == "code")
		return element_content.querySelector("code").innerText;
	else if (id == "image")
		return [
			element_content.querySelector("img").src,
			element_content.querySelector("img").alt,
			element_content.querySelector("img").style.width.slice(0, -1),
		];
	else if (id == "alert")
		return [
			element_content.querySelector("h5").innerText,
			element_content.querySelector("span").innerText,
		];
	else if (id == "line")
		return element_content.querySelector("hr").style.width.slice(0, -1);
}

function _get_parent_from_(element) {
	while (!element.classList.toString().includes("element "))
		element = element.parentElement;

	return element;
}

function _delete_(element) {
	element = _get_parent_from_(element);

	if (element.id == "title") {
		let row_content_block = document.querySelector(".content_block");
		row_content_block.removeChild(element);
		title.get_form_for_getting_element_data();
	} else content_block.removeChild(element);
}

export function get_click_event_on_edit_btn(e) {
	let answer = confirm("Do you really want to edit this element?");
	if (answer) {
		let element = _get_parent_from_(e.target.parentElement);
		let element_content = element.children[0];

		element.after(
			get_needed_element_from_(
				element_content.classList[1]
			).get_form_for_getting_element_data(
				_get_element_value_from_(element_content)
			)
		);

		set_click_event_for_apply_btn();
		set_click_event_for_cancel_btn();

		_delete_(element);
	}
}

export function get_click_event_on_close_btn(e) {
	let answer = confirm("Do you really want to delete this element?");
	if (answer) _delete_(e.target.parentElement);
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
				.replace(new RegExp(`${position}`, "g"), align);
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

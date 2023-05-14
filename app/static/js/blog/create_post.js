import {
	get_click_event_on_create_post_btn,
	set_click_event_for_apply_btn,
	set_click_event_for_cancel_btn,
} from "./functions/_events.js";

import { Title } from "./element_classes/_title.js";
import { StringElement } from "./element_classes/_string_element.js";
import { Code } from "./element_classes/_code.js";
import { Image } from "./element_classes/_image.js";
import { Alert } from "./element_classes/_alert.js";
import { Line } from "./element_classes/_line.js";
import { Link } from "./element_classes/_link.js";

import { content_block } from "./_global_variables.js";
import { check_is_there_element_form } from "./functions/_processing.js";

export const title = new Title();

export function get_needed_element_from_(block_id) {
	return {
		title: title,
		subtitle1: new StringElement("subtitle1", "h2", "Subtitle I"),
		subtitle2: new StringElement("subtitle2", "h4", "Subtitle II"),
		paragraph: new StringElement("paragraph", "p", "Paragraph", "textarea"),
		code: new Code(),
		image: new Image(),
		alert: new Alert(),
		line: new Line(),
		link: new Link(),
	}[block_id];
}

export function add_needed_element_with_data_from(block) {
	get_needed_element_from_(block.id).add_element_block();
}

if (content_block.previousElementSibling.id != "title")
	title.get_form_for_getting_element_data();

// Loop for adding buttons to add click event
// for adding element in the content block
for (let adding_button of document.querySelector(".adding_buttons").children) {
	adding_button.addEventListener("click", function () {
		if (!check_is_there_element_form()) {
			content_block.appendChild(
				get_needed_element_from_(
					adding_button.id.split("_")[1] // Element title
				).get_form_for_getting_element_data()
			);

			set_click_event_for_apply_btn();
			set_click_event_for_cancel_btn();
		}
	});
}

const post_tags_field = document.querySelector("#post_tags");
const post_submit_btn = document.getElementById("post_submit");

post_submit_btn.addEventListener("click", get_click_event_on_create_post_btn);
post_submit_btn.addEventListener("click", function (e) {
	if (post_tags_field.value) {
		if (
			!post_tags_field.value.includes(",") &&
			post_tags_field.value.length > 30
		) {
			e.preventDefault();
			post_submit_btn.parentElement.parentElement.parentElement.nextElementSibling.classList =
				"bg-danger rounded-bottom";
		} else {
			for (const tag of post_tags_field.value.split(",")) {
				if (tag.length > 30) {
					e.preventDefault();
					if (!document.querySelector(".error-mess"))
						_add_error_paragraph();
				}
			}
		}
	}
});

function _add_error_paragraph() {
	const error_paragraph = document.createElement("p");
	error_paragraph.classList = "error-mess bg-danger px-2 rounded-bottom";
	error_paragraph.innerText = "Must include less than 30 characters";

	post_tags_field.after(error_paragraph);
}
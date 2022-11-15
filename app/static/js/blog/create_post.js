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
	}[block_id];
}

export function add_needed_element_with_data_from(block) {
	get_needed_element_from_(block.id).add_element_block();
}

if (!content_block.previousElementSibling.classList.element)
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

const post_submit_btn = document.getElementById("post_submit");
post_submit_btn.addEventListener("click", get_click_event_on_create_post_btn);

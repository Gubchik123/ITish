import {
	content_block,
	hidden_post_title_field,
} from "../_global_variables.js";

import {
	get_div_block,
	get_apply_btn,
	get_close_btn,
	get_input_area_,
	get_element_form_block,
} from "../functions/_getting.js";

import { _get_element_content } from "../functions/_improving.js";
import { set_click_event_for_apply_btn } from "../functions/_events.js";

export function get_wrapped_(element) {
	let block = get_div_block();
	block.classList = "element mb-2 p-1 d-flex justify-content-between";
	block.appendChild(_get_element_content(element));
	block.appendChild(get_close_btn());

	return block;
}

export class Title {
	id = "title";
	tag = "h2";
	placeholder = "Post title";

	add_element_block() {
		let text = this.get_element_data_from_form();

		hidden_post_title_field.value = text;

		let title = document.createElement(this.tag);
		title.innerText = text;

		let title_block = get_wrapped_(title);
		title_block.id = this.id;

		content_block.before(title_block);
	}

	get_element_data_from_form() {
		return content_block.querySelector("#title .form-control").value;
	}

	get_form_for_getting_element_data() {
		let block = get_element_form_block();
		block.id = this.id;

		let input = get_input_area_("input", this.placeholder);
        input.classList += " float_left";
		input.maxLength = 70;

		block.appendChild(input);
		block.appendChild(get_apply_btn());

		content_block.prepend(block);
		set_click_event_for_apply_btn();
	}
}

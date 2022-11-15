import {
	set_click_event_for_apply_btn,
	set_click_event_for_cancel_btn,
} from "../functions/_events.js";

import {
	get_apply_btn,
	get_cancel_btn,
	get_color_input,
	get_input_area_,
	get_element_form_block,
} from "../functions/_getting.js";

import { content_block } from "../_global_variables.js";
import { get_wrapped_ } from "../functions/_improving.js";

export class StringElement {
	constructor(id, tag, placeholder, input_tag="input") {
		this.id = id;
		this.tag = tag;
		this.input_tag = input_tag;
		this.placeholder = placeholder;
	}

	add_element_block() {
		let data = this.get_element_data_from_form();

		let string_element = document.createElement(this.tag);
		string_element.classList = "mb-2";
		string_element.innerText = data.text;

		if (data.color != "#000000") string_element.style.color = data.color;

		content_block.appendChild(get_wrapped_(string_element));
	}

	get_element_data_from_form() {
		return {
			text: content_block.querySelector(".form-control").value,
			color: content_block.querySelector(
				".form-control.form-control-color"
			).value,
		};
	}

	add_form_for_getting_element_data() {
		let block = get_element_form_block();
		block.id = this.id;

		block.appendChild(get_input_area_(this.input_tag, this.placeholder));
		block.appendChild(get_color_input());
		block.appendChild(get_apply_btn());
		block.appendChild(get_cancel_btn());

		content_block.appendChild(block);
		set_click_event_for_apply_btn();
		set_click_event_for_cancel_btn();
	}
}

import {
	set_click_event_for_apply_btn,
	set_click_event_for_cancel_btn,
} from "../functions/_events.js";

import {
	get_div_block,
	get_apply_btn,
	get_cancel_btn,
	get_color_input,
	get_input_area_,
	get_element_form_block,
} from "../functions/_getting.js";

import { content_block } from "../_global_variables.js";
import { get_wrapped_ } from "../functions/_improving.js";

export class Subtitle {
	constructor(level) {
		this.id = level == 1 ? "subtitle1" : "subtitle2";
		this.tag = level == 1 ? "h2" : "h4";
		this.placeholder =
			level == 1 ? "Post subtitle (I)" : "Post subtitle (II)";
	}

	add_element_block() {
		let content = this.get_element_data_from_form();

		let subtitle = document.createElement(this.tag);
		subtitle.classList.add("mb-2");
		subtitle.innerText = content.text;

		if (content.color != "#000000") subtitle.style.color = content.color;

		content_block.appendChild(get_wrapped_(subtitle));
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

		block.appendChild(get_input_area_("input", this.placeholder));
		block.appendChild(get_color_input());
		block.appendChild(get_apply_btn());
		block.appendChild(get_cancel_btn());

		content_block.appendChild(block);
		set_click_event_for_apply_btn();
		set_click_event_for_cancel_btn();
	}
}

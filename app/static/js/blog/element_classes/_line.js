import {
	set_click_event_for_apply_btn,
	set_click_event_for_cancel_btn,
} from "../functions/_events.js";

import {
	get_div_block,
	get_apply_btn,
	get_cancel_btn,
	get_element_form_block,
	get_select_color_block,
	get_range_input_with_label_,
} from "../functions/_getting.js";

import { content_block } from "../_global_variables.js";
import { get_wrapped_ } from "../functions/_improving.js";

function _get_block_with_fields() {
	let block_with_fields = get_div_block();
	block_with_fields.classList = "w-100 mb-3";
	block_with_fields.appendChild(
		get_range_input_with_label_("Line width and color")
	);
	block_with_fields.appendChild(get_select_color_block());
	return block_with_fields;
}

export class Line {
	id = "line";
	tag = "hr";

	add_element_block() {
		let content = this.get_element_data_from_form();

		let line = document.createElement(this.tag);
		line.style.borderTop = "5px solid";
		line.style.width = `${content.line_width}%`;
		line.style.color = `var(--bs-${content.line_color})`;

		content_block.appendChild(get_wrapped_(line));
	}

	get_element_data_from_form() {
		return {
			line_width: content_block.querySelector(".form-range").value,
			line_color: content_block.querySelector(".form-select").value,
		};
	}

	add_form_for_getting_element_data() {
		let block = get_element_form_block();
		block.id = this.id;

		block.appendChild(_get_block_with_fields());

		block.appendChild(get_apply_btn());
		block.appendChild(get_cancel_btn());

		content_block.appendChild(block);
		set_click_event_for_apply_btn();
		set_click_event_for_cancel_btn();
	}
}

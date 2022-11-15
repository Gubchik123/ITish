import {
	get_apply_and_cancel_btns_wrapped_in_,
	get_wrapped_,
} from "../functions/_improving.js";

import {
	get_div_block,
	get_element_form_block,
	get_select_color_block,
	get_range_input_with_label_,
} from "../functions/_getting.js";

import { content_block } from "../_global_variables.js";

function _get_block_with_fields(value = "") {
	let block_with_fields = get_div_block();
	block_with_fields.classList = "w-100 mb-3";
	block_with_fields.appendChild(
		get_range_input_with_label_("Line width and color", value)
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

		content_block
			.querySelector(".element-form")
			.after(get_wrapped_(line, this.id));
	}

	get_element_data_from_form() {
		return {
			line_width: content_block.querySelector(".form-range").value,
			line_color: content_block.querySelector(".form-select").value,
		};
	}

	get_form_for_getting_element_data(value = "") {
		let block = get_element_form_block();
		block.id = this.id;

		block.appendChild(_get_block_with_fields(value));

		return get_apply_and_cancel_btns_wrapped_in_(block);
	}
}

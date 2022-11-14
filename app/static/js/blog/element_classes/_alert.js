import {
	set_click_event_for_apply_btn,
	set_click_event_for_cancel_btn,
} from "../functions/_events.js";

import {
	get_div_block,
	get_apply_btn,
	get_cancel_btn,
	get_input_area_,
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
		get_input_area_("input", "Alert title", false)
	);
	block_with_fields.appendChild(
		get_input_area_("textarea", "Alert body", false)
	);
	block_with_fields.appendChild(get_select_color_block());
	return block_with_fields;
}

export class Alert {
	id = "alert";
	tag = "div";

	add_element_block() {
		let content = this.get_element_data_from_form();

		let alert = document.createElement(this.tag);
        alert.style.borderLeft = "7px solid";
		alert.classList = `alert alert-${content.alert_color}`;
        alert.innerHTML = `
            <h5>${content.alert_title}</h5>
            ${content.alert_body}
        `;

		content_block.appendChild(get_wrapped_(alert));
	}

	get_element_data_from_form() {
		let form_controls = content_block.querySelectorAll(".form-control");

		return {
			alert_title: form_controls[0].value,
			alert_body: form_controls[1].value,
			alert_color: content_block.querySelector(".form-select").value,
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

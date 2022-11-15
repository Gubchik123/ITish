import {
	get_block_with_fields,
	get_select_color_block,
	get_element_data_from_form_control_and_,
} from "../functions/_getting.js";

import {
    get_wrapped_,
	add_form_for_getting_element_data_with_,
} from "../functions/_improving.js";

import { content_block } from "../_global_variables.js";

export class Alert {
	id = "alert";
	tag = "div";

	add_element_block() {
		let data = this.get_element_data_from_form();

		let alert = document.createElement(this.tag);
		alert.style.borderLeft = "7px solid";
		alert.classList = `alert alert-${data.third}`;
		alert.innerHTML = `
            <h5>${data.first}</h5>
            ${data.second}
        `;

		content_block.appendChild(get_wrapped_(alert));
	}

	get_element_data_from_form() {
		return get_element_data_from_form_control_and_(".form-control");
	}

	add_form_for_getting_element_data() {
		add_form_for_getting_element_data_with_(
			this.id,
			get_block_with_fields(
				[
					{
						tag: "input",
						placeholder: "Alert title",
						is_float_left: false,
					},
					{
						tag: "textarea",
						placeholder: "Alert body",
						is_float_left: false,
					},
				],
				get_select_color_block()
			)
		);
	}
}

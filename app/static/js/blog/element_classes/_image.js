import {
	get_block_with_fields,
	get_range_input_with_label_,
	get_element_data_from_form_control_and_,
} from "../functions/_getting.js";

import {
    get_wrapped_,
	add_form_for_getting_element_data_with_,
} from "../functions/_improving.js";

import { content_block } from "../_global_variables.js";

export class Image {
	id = "image";
	tag = "img";

	add_element_block() {
		let data = this.get_element_data_from_form();

		let image = document.createElement(this.tag);
		image.classList += "image-fluid my-1";
		image.src = data.first;
		image.alt = data.second;
		image.style.width = `${data.third}%`;

		content_block.appendChild(get_wrapped_(image));
	}

	get_element_data_from_form() {
		return get_element_data_from_form_control_and_(".form-range");
	}

	add_form_for_getting_element_data() {
		add_form_for_getting_element_data_with_(
			this.id,
			get_block_with_fields(
				[
					{
						tag: "input",
						placeholder: "Image url",
						is_float_left: false,
					},
					{
						tag: "input",
						placeholder: "Image description",
						is_float_left: false,
					},
				],
				get_range_input_with_label_("Image width")
			)
		);
	}
}

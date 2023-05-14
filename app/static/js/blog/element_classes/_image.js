import {
	get_block_with_fields,
	get_range_input_with_label_,
	get_element_data_from_form_control_and_,
} from "../functions/_getting.js";

import {
	get_wrapped_,
	get_form_for_getting_element_data_with_,
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

		content_block
			.querySelector(".element-form")
			.after(get_wrapped_(image, this.id));
	}

	get_element_data_from_form() {
		return get_element_data_from_form_control_and_(".form-range");
	}

	get_form_for_getting_element_data(value = ["", "", ""]) {
		return get_form_for_getting_element_data_with_(
			this.id,
			get_block_with_fields(
				[
					{
						tag: "input",
						placeholder: "Image url",
						value: value[0],
					},
					{
						tag: "input",
						placeholder: "Image description",
						value: value[1],
					},
				],
				get_range_input_with_label_("Image width", value[2])
			)
		);
	}
}
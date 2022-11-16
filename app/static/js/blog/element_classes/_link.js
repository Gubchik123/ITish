import {
	get_block_with_fields,
	get_select_color_block,
	get_element_data_from_form_control_and_,
} from "../functions/_getting.js";

import {
	get_wrapped_,
	get_form_for_getting_element_data_with_,
} from "../functions/_improving.js";

import { content_block } from "../_global_variables.js";

export class Link {
	id = "link";
	tag = "a";

	add_element_block() {
		let data = this.get_element_data_from_form();

		let link = document.createElement(this.tag);
		link.target = "_blank";
		link.href = data.link_url;
		link.innerText = data.link_text;
		link.classList = "my-text-color";
        link.style.textDecoration = "underline";

		content_block
			.querySelector(".element-form")
			.after(get_wrapped_(link, this.id));
	}

	get_element_data_from_form() {
		let fields = content_block.querySelectorAll(".form-control");
		return {
			link_text: fields[0].value,
			link_url: fields[1].value,
		};
	}

	get_form_for_getting_element_data(value = ["", ""]) {
		return get_form_for_getting_element_data_with_(
			this.id,
			get_block_with_fields(
				[
					{
						tag: "input",
						placeholder: "Link text",
						value: value[0],
						is_float_left: false,
					},
					{
						tag: "input",
						placeholder: "Link url",
						value: value[1],
						is_float_left: false,
					},
				],
				document.createElement("span")
			)
		);
	}
}

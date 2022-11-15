import {
	get_element_form_block,
	get_input_area_,
} from "../functions/_getting.js";

import {
	get_wrapped_,
	get_apply_and_cancel_btns_wrapped_in_,
} from "../functions/_improving.js";

import { content_block } from "../_global_variables.js";

export class Code {
	id = "code";
	tag = "code";
	placeholder = "Code block";

	add_element_block() {
		let code = document.createElement(this.tag);
		code.classList += "my-1";
		code.innerText = this.get_element_data_from_form().replace(/	/g, '  ');

		let pre = document.createElement("pre");
		pre.classList = "p-2 rounded-4 text-white text-start my-form-bg-color";
		pre.appendChild(code);

		content_block
			.querySelector(".element-form")
			.after(get_wrapped_(pre, this.id));
	}

	get_element_data_from_form() {
		return content_block.querySelector(".form-control").value;
	}

	get_form_for_getting_element_data(value = "") {
		let block = get_element_form_block();
		block.id = this.id;

		block.appendChild(get_input_area_("textarea", "Code block", value));
		return get_apply_and_cancel_btns_wrapped_in_(block);
	}
}

import {
	set_click_event_for_apply_btn,
	set_click_event_for_cancel_btn,
} from "../functions/_events.js";

import {
	get_apply_btn,
	get_cancel_btn,
	get_input_area_,
	get_element_form_block,
} from "../functions/_getting.js";

import { content_block } from "../_global_variables.js";
import { get_wrapped_ } from "../functions/_improving.js";

export class Code {
	id = "code";
	tag = "code";
	placeholder = "Code block";

	add_element_block() {
		let code = document.createElement(this.tag);
		code.classList += "my-1";
		code.innerText = this.get_element_data_from_form();

		let pre = document.createElement("pre");
		pre.classList = "p-2 rounded-4 text-white my-form-bg-color";
		pre.appendChild(code);

		content_block.appendChild(get_wrapped_(pre));
	}

	get_element_data_from_form() {
		return content_block.querySelector(".form-control").value;
	}

	add_form_for_getting_element_data() {
		let block = get_element_form_block();
		block.id = this.id;

		block.appendChild(get_input_area_("textarea", this.placeholder));
		block.appendChild(get_apply_btn());
		block.appendChild(get_cancel_btn());

		content_block.appendChild(block);
		set_click_event_for_apply_btn();
		set_click_event_for_cancel_btn();
	}
}

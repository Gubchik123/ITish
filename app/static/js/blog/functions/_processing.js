import { content_block } from "../_global_variables";

export function warning(target) {
	target.style.border = "2px solid red";
}

export function set_for_(area, placeholder) {
	area.placeholder = placeholder;
}

export function check_filling_of_(element_form) {
	let check = true;
	for (let field of element_form.querySelectorAll(".form-control")) {
		if (field.value == "") {
			warning(field);
			check = false;
		}
	}
	return check;
}

export function check_is_there_element_form() {
	let element_form = content_block.querySelector(".element-form");

	if (!element_form) return false;

	check_filling_of_(element_form);
	return true;
}

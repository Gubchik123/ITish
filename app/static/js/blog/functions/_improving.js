import {
	get_edit_btn,
	get_left_btn,
	get_apply_btn,
	get_right_btn,
	get_div_block,
	get_close_btn,
	get_cancel_btn,
	get_center_btn,
	get_element_form_block,
} from "./_getting.js";

import {
	add_mouse_over_and_leave_event_for_,
	set_click_event_for_apply_btn,
	set_click_event_for_cancel_btn,
} from "./_events.js";

import { content_block } from "../_global_variables.js";

export function get_wrapped_(element) {
	let block = _get_result_element_block_with_(element);

	block = add_mouse_over_and_leave_event_for_(block);

	return block;
}

export function add_apply_and_cancel_btns_wrapped_in_(block) {
	block.appendChild(get_apply_btn());
	block.appendChild(get_cancel_btn());

	content_block.appendChild(block);
	set_click_event_for_apply_btn();
	set_click_event_for_cancel_btn();
}

export function add_form_for_getting_element_data_with_(id, fields) {
	let block = get_element_form_block();
	block.id = id;

	block.appendChild(fields);

	add_apply_and_cancel_btns_wrapped_in_(block);
}

function _get_result_element_block_with_(element) {
	let element_block = get_div_block();
	element_block.classList = "element my-1 px-2";

	element_block.appendChild(_get_element_content(element));
	element_block.appendChild(_get_block_with_element_btns());

	return element_block;
}

export function _get_element_content(element) {
	let element_content = get_div_block();
	element_content.appendChild(element);
	element_content.classList =
		"element-content d-flex justify-content-start text-start";
	return element_content;
}

function _get_block_with_element_btns() {
	let block_with_element_btns = get_div_block();

	block_with_element_btns.classList = "element-btns justify-content-between";
	block_with_element_btns.style.display = "none";
	block_with_element_btns.appendChild(_get_align_btns_block());
	block_with_element_btns.appendChild(_get_processing_btns());

	return block_with_element_btns;
}

function _get_processing_btns() {
	let block_with_processing_btns = get_div_block();
	block_with_processing_btns.classList = "processing_btns";

	block_with_processing_btns.appendChild(get_edit_btn());
	block_with_processing_btns.appendChild(get_close_btn());

	return block_with_processing_btns;
}

function _get_align_btns_block() {
	let align_btns_block = get_div_block();
	align_btns_block.classList = "align_btns";

	align_btns_block.appendChild(get_left_btn());
	align_btns_block.appendChild(get_center_btn());
	align_btns_block.appendChild(get_right_btn());

	return align_btns_block;
}

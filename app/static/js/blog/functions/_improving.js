import {
    get_up_btn,
    get_down_btn,
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

import { add_mouse_over_and_leave_event_for_ } from "./_events.js";

let block_id;

export function get_wrapped_(element, id, adding=true) {
	block_id = id;
	let block = _get_result_element_block_with_(element, adding);

	block = add_mouse_over_and_leave_event_for_(block);

	return block;
}

export function get_apply_and_cancel_btns_wrapped_in_(block) {
	block.appendChild(get_apply_btn());
	block.appendChild(get_cancel_btn());

	return block;
}

export function get_form_for_getting_element_data_with_(id, fields) {
	let block = get_element_form_block();
	block.id = id;

	block.appendChild(fields);

	return get_apply_and_cancel_btns_wrapped_in_(block);
}

function _get_result_element_block_with_(element, adding) {
	let element_block = get_div_block();
	element_block.classList = "element my-1 px-2";

    if (adding) element_block.appendChild(_get_element_content(element));
    else element_block.appendChild(element)

	element_block.appendChild(_get_block_with_element_btns());

	return element_block;
}

export function _get_element_content(element) {
	let element_content = get_div_block();
	element_content.appendChild(element);
	element_content.classList = `element-content ${block_id} d-flex justify-content-start text-start`;
	return element_content;
}

function _get_block_with_element_btns() {
	let block_with_element_btns = get_div_block();

	block_with_element_btns.classList = "element-btns justify-content-between mt-3";
	block_with_element_btns.style.display = "none";
	block_with_element_btns.appendChild(_get_align_btns_block());
	block_with_element_btns.appendChild(_get_position_btns_block());
	block_with_element_btns.appendChild(_get_processing_btns());

	return block_with_element_btns;
}

function _get_align_btns_block() {
	let align_btns_block = get_div_block();
	align_btns_block.classList = "align_btns";

	align_btns_block.appendChild(get_left_btn());
	align_btns_block.appendChild(get_center_btn());
	align_btns_block.appendChild(get_right_btn());

	return align_btns_block;
}

function _get_position_btns_block() {
    let position_btns_block = get_div_block();
	position_btns_block.classList = "position_btns";

	position_btns_block.appendChild(get_up_btn());
	position_btns_block.appendChild(get_down_btn());

	return position_btns_block;
}

function _get_processing_btns() {
    let block_with_processing_btns = get_div_block();
    block_with_processing_btns.classList = "processing_btns";

    block_with_processing_btns.appendChild(get_edit_btn());
    block_with_processing_btns.appendChild(get_close_btn());

    return block_with_processing_btns;
}
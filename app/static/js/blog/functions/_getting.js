import {
	get_click_event_on_close_btn,
	get_click_event_on_align_btn,
} from "./_events.js";
import { set_for_ } from "./_processing.js";

export function get_input_area_(tag, placeholder, float_left = true) {
	let input_area = document.createElement(tag);
	input_area.classList = "form-control me-2 mb-2";
	if (float_left) input_area.classList += " float_left";

	set_for_(input_area, placeholder);

	return input_area;
}

export function get_div_block() {
	return document.createElement("div");
}

export function get_element_form_block() {
	let block = get_div_block();
	block.classList = "element-form my-3";
	return block;
}

export function get_btn_with_(inner_html, classList) {
	let button = document.createElement("button");
	button.innerHTML = inner_html;
	button.classList = classList;

	return button;
}

function _get_btn_with_icon(icon_name, color_name, type = "") {
	let classes = `btn ${type} btn-${color_name} btn-sm mb-2 me-2 `;
	classes += `float_left d-flex justify-content-center align-items-center`;

	return get_btn_with_(`<ion-icon name='${icon_name}'></ion-icon>`, classes);
}

export function get_apply_btn() {
	return _get_btn_with_icon("checkmark", "success", "apply");
}

export function get_cancel_btn() {
	return _get_btn_with_icon("close", "danger", "cancel");
}

export function get_edit_btn() {
	return _get_btn_with_icon("pencil", "primary", "none");
}

export function get_left_btn() {
	let button = _get_btn_with_icon("chevron-back-circle-outline", "info");
	button.addEventListener("click", function (e) {
		get_click_event_on_align_btn(e, "start");
	});
	return button;
}

export function get_center_btn() {
	let button = _get_btn_with_icon(
		"ellipsis-horizontal-circle-outline",
		"info"
	);
	button.addEventListener("click", function (e) {
		get_click_event_on_align_btn(e, "center");
	});
	return button;
}

export function get_right_btn() {
	let button = _get_btn_with_icon("chevron-forward-circle-outline", "info");
	button.addEventListener("click", function (e) {
		get_click_event_on_align_btn(e, "end");
	});
	return button;
}

export function get_close_btn() {
	let close_btn = _get_btn_with_icon("trash-outline", "danger");
	close_btn.addEventListener("click", get_click_event_on_close_btn);
	return close_btn;
}

export function get_color_input() {
	let color_field = document.createElement("input");
	color_field.type = "color";
	color_field.style.width = "50px";
	color_field.title = "Choose future text color";
	color_field.classList =
		"form-control form-control-color mb-2 me-2 float_left";

	return color_field;
}

export function get_range_input_with_label_(label) {
	let range_input_label = document.createElement("span");
    range_input_label.innerHTML = `${label} <br>`;

	let range_input = document.createElement("input");
	range_input.type = "range";
	range_input.classList = "form-range";
	range_input.min = "1";
	range_input.max = "100";

    let range_block = get_div_block()
    range_block.appendChild(range_input_label);
    range_block.appendChild(range_input);

	return range_block;
}

export function get_select_color_block() {
    let select = document.createElement("select");
    select.classList = "form-select";
    select.innerHTML = `
        <option value="secondary" selected>Secondary (gray)</option>
        <option value="primary">Primary (blue)</option>
        <option value="success">Success (green)</option>
        <option value="info">Info (lightblue)</option>
        <option value="warning">Warning (yellow)</option>
        <option value="danger">Danger (red)</option>
    `;
    return select;
}

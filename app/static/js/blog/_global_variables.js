import { get_click_event_on_create_post_btn } from "./functions/_events.js";

export const content_block = document.querySelector(".content");

export const hidden_post_title_field = document.getElementById("post_title");
export const hidden_post_body_field = document.getElementById("post_body");

export const post_tags_field = document.getElementById("post_tags");

export const create_post_btn = document.getElementById("post_submit");
create_post_btn.addEventListener("click", get_click_event_on_create_post_btn);

export let apply_btn, cancel_btn;

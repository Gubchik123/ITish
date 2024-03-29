import { content_block, hidden_post_title_field } from "./_global_variables.js";
import { get_wrapped_ as get_wrapped_title_ } from "./element_classes/_title.js";
import { get_wrapped_ as get_wrapped_element_ } from "./functions/_improving.js";

let title = document.querySelector("#title");
title.remove();

let title_block = get_wrapped_title_(title);
title_block.id = "title";

content_block.before(title_block);
hidden_post_title_field.value = title.innerText;

for (let element_content of content_block.querySelectorAll(
	".element-content"
)) {
	element_content.remove();
	content_block.appendChild(get_wrapped_element_(element_content, "", false));
}
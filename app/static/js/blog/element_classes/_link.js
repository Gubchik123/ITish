import{get_block_with_fields as e,get_select_color_block as t,get_element_data_from_form_control_and_ as l}from"../functions/_getting.js";import{get_wrapped_ as r,get_form_for_getting_element_data_with_ as n}from"../functions/_improving.js";import{content_block as i}from"../_global_variables.js";export class Link{id="link";tag="a";add_element_block(){let e=this.get_element_data_from_form(),t=document.createElement(this.tag);t.target="_blank",t.href=e.link_url,t.innerText=e.link_text,t.classList="my-text-color",t.style.textDecoration="underline",i.querySelector(".element-form").after(r(t,this.id))}get_element_data_from_form(){let e=i.querySelectorAll(".form-control");return{link_text:e[0].value,link_url:e[1].value}}get_form_for_getting_element_data(t=["",""]){return n(this.id,e([{tag:"input",placeholder:"Link text",value:t[0]},{tag:"input",placeholder:"Link url",value:t[1]},],document.createElement("span")))}}
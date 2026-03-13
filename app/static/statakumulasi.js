import { ajax_get, ajax_post } from "./ajx.js";
import { set_tanggal } from "./format.js";

$(document).ready(function() {

    let jawab = ajax_get("/statakumulasi/getalldata", {}, "");

    

});

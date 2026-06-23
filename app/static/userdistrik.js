import { ajax_get, ajax_post } from "./ajx.js";
import { set_tanggal } from "./format.js";

$(document).ready(function() {


});

$(document).on("click", ".btn-tambah-userdistrik", function() {

    $("#opUserDistrik").html("Tambah User Distrik");
    $("#AddEditUserDistrik").modal("show");
    $("#txtJenisOpUserDistrik").val("tambah");

});

$(document).on("click", "#btnOKUserDistrik", function() {

    if ($("#txtUsername").val()=='') {
        alert("Masukkan username!");
        return false;
    }
    
    if ($("#txtPassword").val()=='') {
        alert("Masukkan password!");
        return false;
    }

    

});


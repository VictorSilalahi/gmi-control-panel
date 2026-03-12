import { ajax_get, ajax_post } from "./ajx.js";
import { set_tanggal } from "./format.js";

$(document).ready(function() {


});

$(".btn-tambah-server").on("click", function() {

    $("#opServer").text("Tambah Server");
    $("#txtJenisOpServer").val("tambah");
    $("#AddEditServer").modal("show");

});

$(document).on("click",".btn-lihat-distrik", function() {
    let distrik = $("#slcDistrik").val();
    load_redis(distrik);

});


$(document).on("click", ".btn-hapus", function() {

    if (confirm("Hapus data gereja ini?")==true) {

        let jawab = ajax_post("/pengaturanmenu/del", {"nama_gereja": nama_gereja, "link_server": link_server, "distrik": distrik, "aplikasi": aplikasi}, "");

        
    }    

});


function load_redis(distrik) {

    let jawab = ajax_get("/pengaturanmenu/getredis", {"distrik": distrik}, "daftar_server");

    if (jawab.status=='ok') {


        let data = jawab.data;
        let isi = '';
        let no = 1;

        // console.log(data);

        for (let i=0; i<data.length; i++) {
            if (data[i]['distrik']==distrik) {
                isi = isi + "<tr><td>"+no+"</td><td>"+data[i]['nama']+"</td><td>"+data[i]['link']+"</td>";

                if (data[i]['aplikasi']['jemaat']==true) {
                    isi = isi + "<td><div class='form-check form-switch'><input class='form-check-input chkJemaat' type='checkbox' checked></div></td>";
                } else {
                    isi = isi + "<td><div class='form-check form-switch'><input class='form-check-input chkJemaat' type='checkbox'></div></td>";
                }

                if (data[i]['aplikasi']['keuangan']==true) {
                    isi = isi + "<td><div class='form-check form-switch'><input class='form-check-input chkKeuangan' type='checkbox' checked></div></td>";
                } else {
                    isi = isi + "<td><div class='form-check form-switch'><input class='form-check-input chkKeuangan' type='checkbox'></div></td>";
                }

                if (data[i]['aplikasi']['asset']==true) {
                    isi = isi + "<td><div class='form-check form-switch'><input class='form-check-input chkAsset' type='checkbox' checked></div></td>";
                } else {
                    isi = isi + "<td><div class='form-check form-switch'><input class='form-check-input chkAsset' type='checkbox'></div></td>";
                }
                isi = isi + "<td><button class='btn btn-danger btn-hapus'>Hapus</button></td>";

                no++;
            }

        }
        isi = isi + "</tr>";
        $("#tblServer tbody").html(isi); 

    } else {

        $("#daftar_server").html("Error!!!");
    }
}
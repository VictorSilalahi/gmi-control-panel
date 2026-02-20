import { ajax_get, ajax_post } from "./ajx.js";
import { set_tanggal } from "./format.js";

$(document).ready(function() {

    load_redis();

    $(".btn-tambah-server").on("click", function() {

        $("#AddEditServer").modal("show");

    });

});

$(document).on("click", ".chkJemaat", function() {
    // alert($(this).is(":checked"));
    let nilai = $(this).is(":checked");
    let nama_gereja = $(this).parent().parent().prev().prev().text();
    let menu = "jemaat";

    let jawab = ajax_post("/pengaturanmenu/ubahmenu", {"nama_gereja": nama_gereja, "menu": menu, "nilai": nilai}, "");

    if (jawab.status=='ok') {
        alert("Menu "+menu+" pada gereja "+nama_gereja+" berhasil diubah!");
    } else {
        alert("Menu "+menu+" pada gereja "+nama_gereja+" gagal diubah!");
    }
});

$(document).on("click", ".chkKeuangan", function() {
    let nilai = $(this).is(":checked");
    let nama_gereja = $(this).parent().parent().prev().prev().prev().text();
    let menu = "keuangan";

    let jawab = ajax_post("/pengaturanmenu/ubahmenu", {"nama_gereja": nama_gereja, "menu": menu, "nilai": nilai}, "");

    if (jawab.status=='ok') {
        alert("Menu "+menu+" pada gereja "+nama_gereja+" berhasil diubah!");
    } else {
        alert("Menu "+menu+" pada gereja "+nama_gereja+" gagal diubah!");
    }
});

$(document).on("click", ".chkAsset", function() {
    let nilai = $(this).is(":checked");
    let nama_gereja = $(this).parent().parent().prev().prev().prev().prev().text();
    let menu = "asset";

    let jawab = ajax_post("/pengaturanmenu/ubahmenu", {"nama_gereja": nama_gereja, "menu": menu, "nilai": nilai}, "");

    if (jawab.status=='ok') {
        alert("Menu "+menu+" pada gereja "+nama_gereja+" berhasil diubah!");
    } else {
        alert("Menu "+menu+" pada gereja "+nama_gereja+" gagal diubah!");
    }
});


function load_redis() {

    let jawab = ajax_get("/pengaturanmenu/getredis", {}, "daftar_server");

    if (jawab.status=='ok') {


        let data = jawab.data;
        let isi = '';
        let no = 1;

        for (let i=0; i<data.length; i++) {
            isi = isi + "<tr><td>"+no+"</td><td>"+data[i]['nama']+"</td><td></td>";

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
        isi = isi + "</tr>";
        $("#tblServer tbody").html(isi); 

    } else {

        $("#daftar_server").html("Error!!!");
    }
}
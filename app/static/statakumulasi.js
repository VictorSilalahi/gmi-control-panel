import { ajax_get, ajax_post } from "./ajx.js";
import { set_tanggal } from "./format.js";

$(document).ready(function() {

    // $("#modalWait").modal("show");

    let jawab = ajax_get("/statakumulasi/getalldata", {}, "");

    console.log(jawab);

    let data = jawab.data;

    $("#jlhDistrik").html("");
    $("#jlhDistrik").html("<h1>"+data[0]['distrik']+"</h1");
    $("#jlhGereja").html("");
    $("#jlhGereja").html("<h1>"+data[0]['gereja']+"</h1");
    $("#jlhJiwa").html("");
    $("#jlhJiwa").html("<h1>"+data[0]['jiwa']+"</h1");
    $("#jlhKK").html("");
    $("#jlhKK").html("<h1>"+data[0]['kk']+"</h1");

    let data_jenis_keanggotaan = [{
        values: [data[0]['keanggotaan']['aktif'], data[0]['keanggotaan']['tidak aktif']],
        labels: ['Aktif', 'Tidak Aktif'],
        type: 'pie'
    }];

    var layout = {
        height: 450,
        width: 500
    };
    $("#grJenisKeanggotan").html("");
    Plotly.newPlot('grJenisKeanggotan', data_jenis_keanggotaan, layout);
    


    let data_kelompok_umur = [{
        values: [
            data[0]['kelompok_umur']['Anak-anak'], 
            data[0]['kelompok_umur']['Remaja'], 
            data[0]['kelompok_umur']['Pemuda'],
            data[0]['kelompok_umur']['Dewasa'],
            data[0]['kelompok_umur']['Lansia']
        ],
        labels: ['Anak-anak', 'Remaja', 'Pemuda', 'Dewasa', 'Lansia'],
        type: 'pie'
    }];

    var layout = {
        height: 450,
        width: 500
    };
    $("#grKelompokUmur").html("");
    Plotly.newPlot('grKelompokUmur', data_kelompok_umur, layout);

    let data_tipe = [{
        values: [
            data[0]['tipe']['penuh'], 
            data[0]['tipe']['persiapan']
        ],
        labels: ['Penuh', 'Persiapan'],
        type: 'pie'
    }];

    var layout = {
        height: 450,
        width: 500
    };
    $("#grSifatKeanggotan").html("");
    Plotly.newPlot('grSifatKeanggotan', data_tipe, layout);


    // $("#modalWait").modal("hide");
});

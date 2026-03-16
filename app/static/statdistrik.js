import { ajax_get, ajax_post } from "./ajx.js";
import { set_tanggal } from "./format.js";

$(document).ready(function() {

    $(".wait-sign").hide();

    $("#slcDistrik").on("change", function() {


        let distrik = $(this).val();

        get_data(distrik);

    });


});

async function get_data(distrik) {


    // $(".wait-sign").show();
    show_wait()

    try {


            let jawab = await fetch("/statdistrik/getdistrikdata?distrik="+distrik);

            let temp = await jawab.json();

            let data = temp.data;
            console.log(data);

            $("#namaDistrik").html("");
            $("#namaDistrik").html("<h1>"+distrik+"</h1");
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

            let list_gereja = data[0]['list_gereja'];
            let no=1;
            var str = ""
            for (let i=0; i<list_gereja.length; i++) {
                str = str + "<tr><td>"+no+"</td><td>"+list_gereja[i]['link']+"</td><td>"+list_gereja[i]['nama']+"</td></tr>";
                no++;
            }
            $("#tblGereja tbody").html(str);


    } catch(error) {

        alert("Error ")

    } finally {

    }

}

function show_wait() {
    
    let wait = "<div class='spinner-border wait-sign' role='status'><span class='visually-hidden'>...</span></div>";

    $("#namaDistrik").html(wait);
    $("#jlhGereja").html(wait);
    $("#jlhKK").html(wait);
    $("#jlhJiwa").html(wait);
    $("#grJenisKeanggotan").html(wait);
    $("#grKelompokUmur").html(wait);
    $("#grSifatKeanggotan").html(wait);
    $("#tblGereja tbody").html("");

}

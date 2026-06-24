import { ajax_get, ajax_post } from "./ajx.js";
import { set_tanggal } from "./format.js";

$(document).ready(function() {

    const fullUri  = window.location.href;     // "https://example.com"
    const pathOnly = window.location.pathname; // "/shop/products"


    const temp = pathOnly.split("/");

    get_data(temp[3]);
    
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
            $("#jlhGereja").html("<h1>"+data[0]['gereja']+"</h1>");
            $("#jlhJiwa").html("");
            $("#jlhJiwa").html("<h1>"+data[0]['jiwa']+"</h1");
            $("#jlhKK").html("");
            $("#jlhKK").html("<h1>"+data[0]['kk']+"</h1");


           

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
                width: 600
            };
            $("#grKelompokUmur").html("");
            Plotly.newPlot('grKelompokUmur', data_kelompok_umur, layout);


            let list_gereja = data[0]['list_gereja'];
            let no=1;
            var str = ""
            for (let i=0; i<list_gereja.length; i++) {
                str = str + "<tr><td>"+no+"</td><td>"+list_gereja[i]['link']+"</td><td>"+list_gereja[i]['nama']+"</td><td><button class='btn btn-info btn-data-jemaat'>Data</button></tr>";
                no++;
            }
            $("#tblGereja tbody").html(str);


    } catch(error) {

        alert("Error ")

    } finally {

    }

}

$(document).on("click", ".btn-data-jemaat", function() {

    let url = $(this).parent().prev().prev().text()+"api/v1/sektor/jemaat";

    data_jemaat(url);

});

function show_wait() {
    
    let wait = "<div class='spinner-border wait-sign' role='status'><span class='visually-hidden'>...</span></div>";

    $("#jlhGereja").html(wait);
    $("#jlhKK").html(wait);
    $("#jlhJiwa").html(wait);
    $("#grKelompokUmur").html(wait);
    $("#tblGereja tbody").html("");

}

async function data_jemaat(url) {

    
    let jawab = await fetch("/statgereja/getjemaat?link_gereja="+url);

    let temp = await jawab.json();

    let data = temp.data_jiwa.data;
    
    console.log(data);

    let str = "";

    let no = 1;

    for (let i=0; i<data.length; i++) {

        str = str + "<tr style='background-color:#FF0000'><td colspan='4'>Nama Sektor : "+data[i]['nama sektor']+" | No Sektor : "+data[i]['no sektor']+"</td></tr>";

        let jemaat = data[i]['jemaat'];

        for (let j=0; j<jemaat.length; j++) {

            str = str +"<tr><td colspan='2'>Alamat : "+jemaat[j]['alamat']+"</td><td colspan='2'>Mobile Phone :"+jemaat[j]['mobile phone']+"</td></tr>";
        
            let keluarga = jemaat[j]['anggota keluarga'];

            for (let k=0; k<keluarga.length; k++) {
                str = str + "<tr><td>"+no+"</td><td>"+keluarga[k]['nama']+"</td><td>"+keluarga[k]['posisi']+"</td><td>"+keluarga[k]['tgl lahir']+"</td></tr>";

                no++;
            }
        }


    }

    str = str + "<tr><td colspan='2'> T O T A L </td><td><h3>"+(no-1)+"</h3></td><td></td></tr>";

    $("#tblJemaat tbody").html(str);

    $(".modal-jemaat").modal("show");

}

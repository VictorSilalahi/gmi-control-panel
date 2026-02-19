export function ajax_get(url, data) {

    var data_to_show;

    $.ajax({
        type: "GET",
        url: url,
        data: data,
        dataType: "json",
        async: false,
        beforeSend: function() {

        },
        success: function(data) {
            data_to_show = data;
        }
    
    });

    return data_to_show;

}

export function ajax_post(url, data) {

    var data_to_show;

    $.ajax({
        type: "POST",
        headers: { 
            'Accept': 'application/json',
            'Content-Type': 'application/json' 
        },        
        url: url,
        data: JSON.stringify(data),
        dataType: "json",
        async: false,
        beforeSend: function() {

        },
        success: function(data) {
            data_to_show = data;
        }
    
    });

    return data_to_show;

}

export function ajaxTaSemTanggal() {
    var tgl = new Date();
    var tgl_sekarang = tgl.getDate() + "-" + (tgl.getMonth() + 1).toString() + "-" + tgl.getFullYear();

    var temp = ajax_get("tasem");
    var to_send = {"tanggal": tgl_sekarang, "tasem": temp}
    return to_send;
}



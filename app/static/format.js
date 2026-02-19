export function set_tanggal(tanggal_asli) {
    let temp = tanggal_asli.split("-");
    let tgl_tampil = temp[2]+"-"+temp[1]+"-"+temp[0];
    return tgl_tampil;

}

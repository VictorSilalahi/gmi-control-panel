from flask import Blueprint, render_template, redirect, request, session
from ..utils.redisconn import connect_to_redis
from ..utils.link import check_link

import os
import json
import uuid
import requests



# route statistik jemaat
statdistrik_bp = Blueprint("statdistrik", __name__, template_folder="../templates")

@statdistrik_bp.route("/statdistrik")
def get_statjemaat():
    return render_template("statdistrik.html")


@statdistrik_bp.route("/statdistrik/getdistrikdata", methods=['GET'])
def get_all_data():

    distrik = request.args.get('distrik')
    # print(distrik)
    temp = connect_to_redis()
    if temp['status']=='ok':
        
        r = temp['data']
        data = []
        for key in r.scan_iter():
            # print(key)
            temp = r.json().get(key)
            data.append(temp)
    
        # print(data)
        temp = []

        list_link_gereja = []
        unique_distrik = 0
        unique_churces = 0
        
        kk = 0
        jiwa = 0
        
        anak_anak = 0
        remaja = 0
        pemuda = 0
        dewasa = 0
        lansia = 0

        keanggotaan_aktif = 0
        keanggotaan_tidak_aktif = 0

        keanggotaan_penuh = 0
        keanggotaan_persiapan = 0

        server_error = 0

        server_error_list = []
        
        for d in data:
            if d['distrik']==distrik:
                # ambil data distrik yg dipilih
                # ambil jumlah gereja 
                list_link_gereja.append({"link": d['link'], "nama": d['nama']})
                link = d['link']
                di_check = check_link(link)
                if di_check["status"] == "good":
                    unique_churces = unique_churces + 1
                    jemaat = requests.get(link+"api/v1/sektor", timeout=(5, 15))
                    data_jiwa = jemaat.json()
                    # print(data_jiwa['data'])
                    # ambil jumlah kk di tiap gereja
                    for dj in data_jiwa['data']:
                        jiwa = jiwa + int(dj['jiwa'])
                        kk = kk + int(dj['kk'])

                    # kelompok umur
                    kelompok_umur = requests.get(link+"api/v1/kelompokumur", timeout=(5, 15))
                    data_kelompok_umur = kelompok_umur.json()
                    # print(data_kelompok_umur['data'][0]['Anak-anak'])
                    anak_anak = anak_anak + int(data_kelompok_umur['data'][0]['Anak-anak'])
                    remaja = remaja + int(data_kelompok_umur['data'][0]['Remaja'])
                    pemuda = pemuda + int(data_kelompok_umur['data'][0]['Pemuda'])
                    dewasa = dewasa + int(data_kelompok_umur['data'][0]['Dewasa'])
                    lansia = lansia + int(data_kelompok_umur['data'][0]['Lansia'])
                    
                    # aktifitas keanggotaan
                    keanggotaan = requests.get(link+"api/v1/keanggotaan", timeout=(5, 15))               
                    data_keanggotaan = keanggotaan.json()
                    # print(data_keanggotaan)
                    keanggotaan_aktif = keanggotaan_aktif + int(data_keanggotaan['data'][0]['jumlah jiwa keanggotaan aktif'])
                    keanggotaan_tidak_aktif = keanggotaan_tidak_aktif + int(data_keanggotaan['data'][0]['jumlah jiwa keanggotaan tidak aktif'])

                    # tipe keanggotaan
                    tipe = requests.get(link+"api/v1/tipe", timeout=(5, 15))               
                    data_tipe = tipe.json()
                    # print(data_tipe)
                    keanggotaan_penuh = keanggotaan_penuh + data_tipe['data']['penuh']
                    keanggotaan_persiapan = keanggotaan_persiapan + data_tipe['data']['persiapan']

                else:
                    # error
                    server_error_list.append({"link": link})
                    server_error = server_error + 1
                

            # unique_distrik = len(list(set(temp_distrik)))

        temp.append({
                # "distrik": unique_distrik, 
                "gereja": unique_churces, 
                "jiwa": jiwa, 
                "kk": kk, 
                "kelompok_umur": {
                    "Anak-anak": anak_anak,
                    "Remaja": remaja,
                    "Pemuda": pemuda,
                    "Dewasa": dewasa,
                    "Lansia": lansia
                }, 
                "keanggotaan": {
                    "aktif": keanggotaan_aktif,
                    "tidak aktif": keanggotaan_tidak_aktif
                },
                "tipe": {
                    "penuh": keanggotaan_penuh,
                    "persiapan": keanggotaan_persiapan
                },
                "list_gereja": list_link_gereja,
                "error": server_error
        })


        return {"status": "ok", "msg": "Koneksi ke Redis server baik!", "data":temp }, 200

    else:    
        return {"status": "error", "msg": {e}}, 400






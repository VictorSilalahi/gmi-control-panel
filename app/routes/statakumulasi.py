from flask import Blueprint, render_template, redirect, request, session
from ..utils.redisconn import connect_to_redis
from ..utils.link import check_link

import os
import json
import uuid
import requests



# route statistik jemaat
statakumulasi_bp = Blueprint("statakumulasi", __name__, template_folder="../templates")

@statakumulasi_bp.route("/statakumulasi")
def get_statjemaat():
    return render_template("statakumulasi.html")


@statakumulasi_bp.route("/statakumulasi/getalldata", methods=['GET'])
def get_all_data():

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

        temp_distrik = []
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
            # ambil jumlah distrik yg sudah masuk ke database
            temp_distrik.append(d['distrik'])
            # ambil jumlah gereja yg sudah masuk ke database
            unique_churces = unique_churces + 1

            link = d['link']
            di_check = check_link(link)
            if di_check["status"] == "good":
                jemaat = requests.get(link+"api/v1/sektor", timeout=(5, 15))
                data_jiwa = jemaat.json()
                # ambil jumlah kk di tiap gereja
                for dj in data_jiwa['data']:
                    jiwa = jiwa + int(dj['jiwa'])
                    kk = kk + int(dj['kk'])

                # kelompok umur
                kelompok_umur = requests.get(link+"api/v1/kelompokumur", timeout=(5, 15))
                data_kelompok_umur = kelompok_umur.json()
                for dku in data_kelompok_umur['data']:
                    anak_anak = anak_anak + int(dku['Anak-anak'])
                    remaja = remaja + int(dku['Remaja'])
                    pemuda = pemuda + int(dku['Pemuda'])
                    dewasa = dewasa + int(dku['Dewasa'])
                    lansia = lansia + int(dku['Lansia'])
                
                # aktifitas keanggotaan
                keanggotaan = requests.get(link+"api/v1/keanggotaan", timeout=(5, 15))               
                data_keanggotaan = keanggotaan.json()
                for dk in data_keanggotaan['data']:
                    keanggotaan_aktif = keanggotaan_aktif + int(dk['jumlah jiwa keanggotaan aktif'])
                    keanggotaan_tidak_aktif = keanggotaan_tidak_aktif + int(dk['jumlah jiwa keanggotaan tidak aktif'])

                # tipe keanggotaan
                tipe = requests.get(link+"api/v1/tipe", timeout=(5, 15))               
                data_tipe = tipe.json()
                print(data_tipe['data'])
                keanggotaan_penuh = keanggotaan_penuh + data_tipe['data']['penuh']
                keanggotaan_persiapan = keanggotaan_persiapan + data_tipe['data']['persiapan']

            else:
                # error
                server_error_list.append({"link": link})
                server_error = server_error + 1
            

        unique_distrik = len(list(set(temp_distrik)))

        temp.append({
            "distrik": unique_distrik, 
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
            "error": server_error
        })


        return {"status": "ok", "msg": "Koneksi ke Redis server baik!", "data":temp }, 200

    else:    
        return {"status": "error", "msg": {e}}, 400






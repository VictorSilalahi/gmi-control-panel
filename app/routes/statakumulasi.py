from flask import Blueprint, render_template, redirect, request, session
from ..utils.redisconn import connect_to_redis

import os
import json
import uuid


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
    
        print(data)


        temp = []

        unique_distrik = 0
        unique_churces = 0
        for d in data:
            # ambil jumlah distrik yg sudah masuk ke database
            temp.append(d['distrik'])
            unique_churces = unique_churces + 1

        unique_distrik = len(list(set(temp)))
        




        return {"status": "ok", "msg": "Koneksi ke Redis server baik!", "data": data}, 200

    else:    
        return {"status": "error", "msg": {e}}, 400








from flask import Blueprint, render_template, redirect, request, session
from ..utils.redisconn import connect_to_redis

import os
import json
import uuid


# route statistik jemaat
statjemaat_bp = Blueprint("statjemaat", __name__, template_folder="../templates")

@statjemaat_bp.route("/statjemaat")
def get_statjemaat():
    return render_template("statjemaat.html")


@statjemaat_bp.route("/statjemaat/getallchurch")
def get_all_church():

    temp = connect_to_redis()
    if temp['status']=='ok':
        
        r = temp['data']
        data = []
        for key in r.scan_iter():
            # print(key)
            temp = r.json().get(key)
            data.append(temp)
    
        print(data)
        return {"status": "ok", "msg": "Koneksi ke Redis server baik!", "data": data}, 200

    else:    
        return {"status": "error", "msg": {e}}, 400








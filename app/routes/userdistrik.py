from flask import Blueprint, render_template, redirect, request, session
from ..utils.redisconn import connect_to_redis

import redis
import os
import json
import uuid




# route menu
userdistrik_bp = Blueprint("userdistrik", __name__, template_folder="../templates")

@userdistrik_bp.route("/userdistrik")
def get_userdistrik():
    return render_template("userdistrik.html")


@userdistrik_bp.route("/userdistrik/getredis")
def get_redis():

    temp = connect_to_redis()
    if temp['status']=='ok':
        
        r = temp['data']
        data = []
        for key in r.scan_iter():
            # print(key)
            temp = r.json().get(key)
            data.append(temp)
    
        return {"status": "ok", "msg": "Koneksi ke Redis server baik!", "data": data}, 200

    else:    
        return {"status": "error", "msg": {e}}, 400


@userdistrik_bp.route("/userdistrik/ubahmenu", methods=['POST'])
def ubah_menu():
    temp = request.get_json()

    nama_gereja = temp['nama_gereja']
    menu = temp['menu']
    nilai = temp['nilai']

    temp = connect_to_redis()

    if temp['status']=='ok':    
        r = temp['data']

        for key in r.scan_iter():
            # print(key)
            temp = r.json().get(key)
            if temp['nama']==nama_gereja:
                r.json().set(key, "$.aplikasi."+menu, nilai)


        return {"status": "ok", "msg": "Menu Modul gereja berhasil diubah!", "data": {}}, 200

    else:    
        return {"status": "error", "msg": {e}}, 400


@userdistrik_bp.route("/userdistrik/add", methods=['POST'])
def add_userdistrik():

    temp = request.get_json()

    username = temp['username']
    password = temp['password']
    distrik = temp['distrik']

    new_userdistrik = {"username": username, "password": link_server, "distrik": distrik, "aplikasi": aplikasi}

    temp = connect_to_redis()

    if temp['status']=='ok':  
        r = temp['data']
        id = str(uuid.uuid4())
        r.json().set(id, Path.root_path(), new_gereja)
        return {"status": "ok", "msg": "Penambahan gereja berhasil!", "data": {}}, 200

    else:    
        return {"status": "error", "msg": {e}}, 400


@userdistrik_bp.route("/userdistrik/del", methods=['POST'])
def del_distrik():
    temp = request.get_json()

    temp = connect_to_redis()

    if temp['status']=='ok':  
        r = temp['data']
        r.json().set('gmi:4', Path.root_path(), new_gereja)
        return {"status": "ok", "msg": "Penambahan gereja berhasil!", "data": {}}, 200

    else:    
        return {"status": "error", "msg": {e}}, 400


def connect_to_redis():
    redist_host = os.getenv("REDIS_SERVER")
    redis_port = os.getenv("REDIS_PORT")
    redis_password = os.getenv("REDIS_PASSWORD")
    redis_username = os.getenv("REDIS_USERNAME") 
    # print(redist_host, redis_port, redis_username, redis_password)
    try:
        # Connect to the Redis server
        r = redis.Redis(
            host=redist_host,
            port=redis_port,
            password=redis_password,
            username=redis_username,
            db=0,
            decode_responses=True  # Optional: automatically decode responses to strings
        )

        # Test the connection
        if r.ping():
            return {"status": "ok", "msg": "koneksi ke redis berhasil", "data": r}

    except redis.exceptions.ConnectionError as e:
        print(f"Error connecting to Redis: {e}")    
    
        return {"status": "error", "msg": {e}}




from flask import Blueprint, render_template, redirect
import redis
import os
import json

# route menu
pengaturanmenu_bp = Blueprint("menu", __name__, template_folder="../templates")

@pengaturanmenu_bp.route("/pengaturanmenu")
def get_pengaturanmenu():
    return render_template("pengaturanmenu.html")


@pengaturanmenu_bp.route("/pengaturanmenu/getredis")
def get_redis():
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
            data = []
            for key in r.scan_iter():
                # print(key)
                temp = r.json().get(key)
                data.append(temp)
                # print(temp)
                # json_data = json.loads(r.get(key))
                # print(json_data)
    
            return {"status": "ok", "msg": "Koneksi ke Redis server baik!", "data": data}, 200


    except redis.exceptions.ConnectionError as e:
        print(f"Error connecting to Redis: {e}")    
    
        return {"status": "error", "msg": {e}}, 400

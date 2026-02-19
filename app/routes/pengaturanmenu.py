from flask import Blueprint, render_template, redirect
import redis

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

    try:
        # Connect to the Redis server
        r = redis.Redis(
            host=redist_host,
            port=redis_port,
            password=redis_password,
            username=redis_username,
            decode_responses=True  # Optional: automatically decode responses to strings
        )

        # Test the connection
        if r.ping():
            print("Successfully connected to Redis!")
            # Example usage: set and get a key
            # r.set('my_key', 'Hello, remote Redis!')
            # value = r.get('my_key')
            # print(f"Value of my_key: {value}")
    
            return {"status": "ok", "msg": "Koneksi ke Redis server baik!"}, 200


    except redis.exceptions.ConnectionError as e:
        print(f"Error connecting to Redis: {e}")    
    
        return {"status": "error", "msg": "Error!"}, 400

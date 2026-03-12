import redis
from redis.commands.json.path import Path

def connect_to_redis():
    redist_host = os.getenv("REDIS_SERVER")
    redis_port = os.getenv("REDIS_PORT")
    redis_password = os.getenv("REDIS_PASSWORD")
    redis_username = os.getenv("REDIS_USERNAME") 

    try:
        r = redis.Redis(
            host=redist_host,
            port=redis_port,
            password=redis_password,
            username=redis_username,
            db=0,
            decode_responses=True  # Optional: automatically decode responses to strings
        )

        if r.ping():
            return {"status": "ok", "msg": "koneksi ke redis berhasil", "data": r}

    except redis.exceptions.ConnectionError as e:
        print(f"Error connecting to Redis: {e}")    
    
        return {"status": "error", "msg": {e}}

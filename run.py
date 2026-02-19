from flask import Flask

import os
import redis
from dotenv import load_dotenv

load_dotenv()


def create_app():
    
    host = os.getenv("REDIS_SERVER")
    port = os.getenv("REDIS_PORT")
    password = os.getenv("REDIS_PASSWORD")
    username = os.getenv("REDIS_USERNAME") 

    # try:
    #     # Connect to the Redis server
    #     r = redis.Redis(
    #         host=host,
    #         port=port,
    #         password=password,
    #         username=username,
    #         decode_responses=True  # Optional: automatically decode responses to strings
    #     )

    #     # Test the connection
    #     if r.ping():
    #         print("Successfully connected to Redis!")
    #         # Example usage: set and get a key
    #         r.set('my_key', 'Hello, remote Redis!')
    #         value = r.get('my_key')
    #         print(f"Value of my_key: {value}")
    # except redis.exceptions.ConnectionError as e:
    #     print(f"Error connecting to Redis: {e}")

if __name__=="__main__":
    app = create_app()


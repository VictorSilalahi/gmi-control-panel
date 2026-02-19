from flask import Flask

import os

from dotenv import load_dotenv

load_dotenv()

from app.routes.pengaturanmenu import pengaturanmenu_bp


def create_app():
    app = Flask(__name__, static_folder="app/static")    
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basedir, "instance", "kasihkarunia.db")

    # routes
    app.register_blueprint(pengaturanmenu_bp)

    return app

if __name__=="__main__":
    app = create_app()
    app_mode = os.getenv("APP_MODE")
    app_host = os.getenv("APP_HOST")
    app_port = os.getenv("APP_PORT")

    if app_mode == "development":
        print("[dev mode]")
        app.run(host=app_host, port=app_port, debug=True)
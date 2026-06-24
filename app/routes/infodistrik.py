from flask import Blueprint, render_template, redirect, request, session
from ..utils.redisconn import connect_to_redis
from ..utils.link import check_link

import os
import json
import uuid
import requests



# route statistik jemaat
infodistrik_bp = Blueprint("infodistrik", __name__, template_folder="../templates")

@infodistrik_bp.route("/statdistrik/infodistrik/<distrik>")
def get_info_distrik(distrik):
    return render_template("infodistrik.html")

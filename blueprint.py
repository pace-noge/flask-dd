from ddtrace import Pin
from flask import abort, Blueprint
from flask import jsonify

bp = Blueprint("logs", __name__, url_prefix="/logs")

# override the blue print as new service
Pin.override(bp, service="flask-bp", app="flask", app_type="web")

@bp.route("/")
def index():
    return "Index page"


@bp.route("/company")
def company():
    return jsonify({"id": 679, "name": "talenta"})

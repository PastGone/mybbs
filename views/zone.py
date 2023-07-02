from flask import session, Blueprint

zone_blue = Blueprint("zone_blue", __name__)


@zone_blue.route("/zone/")
def zone():
    email = session.get("email")
    is_ok = session.get("is_ok")
    print(email, is_ok)
    return email, is_ok

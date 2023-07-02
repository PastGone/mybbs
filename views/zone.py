from flask import session, Blueprint,redirect,render_template

zone_blue = Blueprint("zone_blue", __name__)


@zone_blue.route("/zone/")
def zone():
    email = session.get("email")
    is_ok = session.get("is_ok")
    print(email, is_ok)
    if email:
        return redirect("/login/")
    else:
        return render_template("zone.html",email=email,is_ok=is_ok)
        # return email+is_ok+"fff"

from flask import session, Blueprint, redirect, render_template,flash

post_list_blue = Blueprint("post_list_blue", __name__)


@post_list_blue.route("/zone/")
def zone():
    email = session.get("email")
    is_ok = session.get("is_ok")
    print(email, is_ok)

    if email is None:
        return redirect("/login/")
    else:
        from app import zmt
        zone_list=zmt.get_zone()
        return render_template("zone.html", email=email, is_ok=is_ok,zone_list=zone_list)
        # return email+is_ok+"fff"

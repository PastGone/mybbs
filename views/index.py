from flask import Blueprint, render_template, session, redirect

index_blue = Blueprint("index_blue", __name__)


# 用于登录的路由
@index_blue.route('/')
def index():
    email = session.get("email")
    is_ok = session.get("is_ok")
    print(email, is_ok)

    # if email is None:
    #     return redirect("/login/")
    # else:
    from app import zmt
    zone_list = zmt.get_zone()
    return render_template("index.html", email=email, is_ok=is_ok, zone_list=zone_list)
# return render_template("index.html")

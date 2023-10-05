from flask import Blueprint,render_template

post_list_blue = Blueprint("post_list_blue", __name__)


@post_list_blue.route("/post_list/zone_id=<id>/")
def post_list(id):
    return id
    # return render_template("postlist.html")



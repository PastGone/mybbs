from flask import Blueprint

post_blue = Blueprint("post_blue", __name__)


@post_blue.route("/post/post_id=<id>")
def one_post(id):
    return id


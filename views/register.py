# 用于注册的路由
from flask import render_template, request, Blueprint

register_blue = Blueprint("register_blue", __name__)


@register_blue.route('/register/', methods=['GET'])
def register_get():
    # if request.method == 'POST':
    #   pass

    return render_template("register.html")


# 用于注册的路由，确切地说是接收注册参数的路由
@register_blue.route('/register/', methods=['POST'])
def register_post():
    from my_tools import generate_token, send_email
    from  app import app
    from  app import  mail
    email = request.form['email']
    from app import ldm
    if ldm.get_email(email):
        return "用户已注册"

    from app import remt
    g_t = remt.get_code_byEmail(email)

    if g_t == "":
        g_t = generate_token()
        remt.data_in(email, g_t)

    return send_email(email, g_t,app=app,mail=mail)

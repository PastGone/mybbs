# 用于注册的路由
from flask import render_template, request, Blueprint
from db_tools.login_data_master import Login_data_master
from db_tools.register_data_master import Register_data_master
from my_tools import generate_token

register_blue = Blueprint("register_blue", __name__)


@register_blue.route('/register/', methods=['GET'])
def register():
    # if request.method == 'POST':
    #   pass

    return render_template("register.html")


# 用于注册的路由，确切地说是接收注册参数的路由
@register_blue.route('/register/', methods=['POST'])
def text():
    email = request.form['email']
    ldm = Login_data_master("login.db")
    if ldm.get_email(email):
        return "用户已注册"

    remt = Register_data_master("register.db")
    g_t = remt.get_code_byEmail(email)

    if g_t == "":
        g_t = generate_token()
        remt.data_in(email, g_t)
    from app import send_email
    return send_email(email, g_t)

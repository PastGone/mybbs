# 用于 邮箱验证的路由函数
from flask import request, render_template, Blueprint

from db_tools.login_data_master import Login_data_master
from my_tools import is_register_code_right, creat_user

verify_blue = Blueprint("verify_blue", __name__)


@verify_blue.route('/token/<email>', methods=['GET', "POST"])
def token(email):
    if request.method == 'POST':
        authcode = request.form["Captcha"]
        password = request.form["password"]
        username = request.form["username"]
        ldm = Login_data_master("login.db")
        if ldm.get_email(email):
            return "用户已注册"

        if is_register_code_right(email, authcode):
            # flash('I am flash, who is looking for me?')
            creat_user(email, username, password)
            return render_template("register_success.html")
            # return redirect(url_for('token'))

    return render_template("authenticate.html")

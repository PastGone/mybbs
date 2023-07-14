from flask import Blueprint, request, session, render_template

from my_tools import is_password_right

login_blue = Blueprint("login_blue", __name__)


# 用于登录的路由
@login_blue.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('user_data.txt', 'a') as f:
            f.write('username: {}, password: {}\n'.format(username, password))
        if is_password_right(username, password):
            session["email"] = username
            session["is_ok"] = True
            return 'Login Successful!'

    return render_template("login.html")

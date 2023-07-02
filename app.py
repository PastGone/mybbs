# 导入该库用于多线程
# 导入该库用于生成验证码

from threading import Thread

# 导入Flask类库
from flask import Flask, render_template
# 导入该库用于发送邮件信息
from flask_mail import Mail
from flask_mail import Message

from my_tools import *
# 创建应用实例
from views import login,verify,register,zone

# 导入数据库管理软件包

app = Flask(__name__, template_folder="./templates")

# 导入配置文件
app.config.from_object("config.settings")

app.register_blueprint(login.login_blue)
app.register_blueprint(verify.verify_blue)
app.register_blueprint(register.register_blue)
app.register_blueprint(zone.zone_blue)

# 初始化Mail
mail = Mail(app)


# 该函数的作用是在另一个线程之中发送邮件
def send_async_email(myapp, msg):
    with myapp.app_context():
        mail.send(msg)


# 发送邮件的函数，如果开启多线程时或者发送邮件时出错可以尝试更换网络以解决问题
def send_email(email: str, mytoken: str):
    message = Message('来自繁星bbs的通知。', recipients=[email])
    # 注意下面调用了获取局域网IP地址的函数
    url = getHostname() + ":5000/token/" + email

    message.body = '''点击以下链接填写验证码以注册用户:{} 
    <a href="http://{}">账户激活</a>'''.format(mytoken, url)

    try:
        thread = Thread(target=send_async_email, args=[app, message])
        thread.start()
        return '验证码已发送到您的邮箱'
    except Exception as e:
        return str(e)


# 视图函数（路由）
@app.route('/')
def index():
    return render_template("index.html")
# 启动实施（只在当前模块运行）
if __name__ == '__main__':
    #    如果下面的程序跑起来没有用
    #    在pycharm面只开的一个服务的话
    #    可能需要在设置里面其他选项里增加--host=0.0.0.0
    app.run(host='0.0.0.0', debug=True)

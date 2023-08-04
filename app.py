# 导入Flask类库
from flask import Flask, render_template
# 导入该库用于发送邮件信息
from flask_mail import Mail
# 导入数据库管理软件包
from db_tools.login_data_master import Login_data_master
from db_tools.register_data_master import Register_data_master
from db_tools.zone_data_master import Zone_data_master
# 创建应用实例
from views import login, verify, register, zone,index

app = Flask(__name__, template_folder="./templates")
# 导入配置文件
app.config.from_object("config.settings")
# 设置蓝图
app.register_blueprint(login.login_blue)
app.register_blueprint(verify.verify_blue)
app.register_blueprint(register.register_blue)
app.register_blueprint(zone.zone_blue)
app.register_blueprint(index.index_blue)

# 初始化Mail
mail = Mail(app)
 # 初始化数据库
ldm = Login_data_master("./db/BBS.db", "login")
remt = Register_data_master("./db/BBS.db", "register")
zmt = Zone_data_master("./db/BBS.db", "zone")



# 启动实施（只在当前模块运行）
if __name__ == '__main__':
    #    如果下面的程序跑起来没有用
    #    在pycharm面只开的一个服务的话
    #    可能需要在设置里面其他选项里增加--host=0.0.0.0
    app.run(host='0.0.0.0', debug=True)

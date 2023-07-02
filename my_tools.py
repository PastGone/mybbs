# 注意这里有几个小点需要说明
# request.remote_addr			# 获取内网IP
# request.environ.get('HTTP_X_REAL_IP', request.remote_addr)		# 获取外网IP
#  有时或许不奏效所以在局域网内你应该可以这样
# import socket
# hostname = socket.gethostname()
# ip = socket.gethostbyname(hostname)
# print(ip)
# 下面是获取局网IP的方法


def getHostname():
    import socket
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip


# 该函数用于生成随机验证码
def generate_token():
    # 生成随机字符串作为令牌，长度为6
    import random
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))


# 用于创建账户的的函数
def creat_user(email, username, password):
    from db_tools.login_data_master import Login_data_master
    ldm = Login_data_master("login.db")
    ldm.data_in(email, username, password)
    return email + password + username


def is_password_right(email: str, pwd1: str) -> bool:
    from app import ldm
    pwd = ldm.get_password_by_email(email)
    if pwd == pwd1:
        return True
    return False


def is_register_code_right(email, Captcha):
    from app import remt
    g_t = remt.get_code_byEmail(email)
    if Captcha == g_t:
        remt.delete_by_email(email)
        return True
    return False

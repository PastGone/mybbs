# 导入简单的数据库的库
from db_tools.login_data_master import Login_data_master
from db_tools.register_data_master import Register_data_master

fist_table_name = "USER"


# temporary

def test1():
    # 下面的代码是测试注册数据库的
    remt = Register_data_master("../db/BBS.db", "register")
    remt.data_in("2085765742@qq.com", "520521")
    remt.get_table()
    remt.get_code_byEmail("208576574@qq.com")
    remt.close()


def test2():
    # 下面的代码是测试用来登录的数据库的
    ldm = Login_data_master("../db/BBS.db", "login")
    ldm.data_in("2085765742@qq.com", "大橘子", "qq123456")
    ldm.get_table()
    ldm.get_email("2085765744@qq.com")
    # ldm.delete_by_email("2085765742@qq.com")
    print(ldm.get_password_by_email("2735956898@qq.com"))


# 下面的部分用来测试用例保证 该类工具 的健全性
if __name__ == "__main__":
    test1()
    test2()
    #
    pass

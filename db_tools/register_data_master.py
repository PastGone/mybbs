# 数据管理大师子类，注册数据管理大师
from db_tools.data_master import Data_master
#
# fist_table_name = "USER"


class Register_data_master(Data_master):
    # 初始化方法，需要数据库名称
    def __init__(self, db_name, table_name='register'):
        self.db_name = db_name
        self.table_name = table_name
        self.continue_init()



    # 数据管理大师 独有的 gate函数 通过 email 参数得到验证码
    def get_code_byEmail(self, email: str):

        cursor = self.cur.execute(
            """select * from {} where EMAIL = '{}';""".format(self.table_name, email)
        )
        print("查询到以下数据")
        code = ''
        for row in cursor:
            print(row)
            code = row[1]
        print("返回的数据", code)
        print("返回数据类型 ", type(code))
        print("查询数据是否为空 ", code == "")

        return code

    # 对父类的三个未实现方法进行重写
    def creat_table(self):
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS {} 
                    (EMAIL CHAR(50) PRIMARY KEY     NOT NULL,
                    CODE   CHAR(6)   NOT NULL,
                    CreatedTime TimeStamp NOT NULL DEFAULT (datetime('now','localtime')));'''.format(self.table_name)
        )
        print("数据表创建成功")
        self.connection.commit()

    def data_in(self, email, code):
        try:
            self.cur.execute(
                """INSERT INTO {} (EMAIL,CODE) \
                      VALUES ('{}','{}')""".format(self.table_name, email, code)
            )
            self.connection.commit()
            print("数据插入成功")
        except Exception as e:
            print(e)

    def delete_by_email(self, email):
        a = self.cur.execute("DELETE from {} where EMAIL = '{}';".format(self.table_name, email))

        # 注意SQL Lite之中的列名大小写,似乎不区分
        self.connection.commit()

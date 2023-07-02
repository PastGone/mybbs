from db_tools.data_master import Data_master

fist_table_name = "USER"


class Login_data_master(Data_master):
    def get_email(self, email):
        # cursor = self.cur.execute(
        #     """select * from {} where email = '{}';""".format(self.table_name, email)
        # )
        print("{}".format(self.table_name)+"pppp")
        cursor = self.cur.execute("SELECT * FROM {} WHERE email = ?;".format(self.table_name), (email,))

        print("查询到以下数据")
        code = ''
        for row in cursor:
            print(row)
            code = row[0]
        print("返回的数据", code)
        print("返回数据类型 ", type(code))
        print("查询数据是否为空 ", code == "")

        return code

    def get_password_by_email(self, email):
        cursor = self.cur.execute(
            """select * from {} where email = '{}';""".format(self.table_name, email)
        )
        print("查询到以下数据")
        code = ''
        for row in cursor:
            print(row)
            code = row[2]

        if not code == "":
            print("返回的数据", code)
            print("返回数据类型 ", type(code))
        else:
            print("查询数据为空 ")
            return False

        return code

    def creat_table(self):
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS {} 
                    (Email CHAR(50) PRIMARY KEY     NOT NULL,
                    UserName   CHAR(32)   NOT NULL,
                    PassWord   CHAR(16)   NOT NULL,
                    CreatedTime TimeStamp NOT NULL DEFAULT (datetime('now','localtime')));'''.format(self.table_name)
        )
        print("数据表创建成功")
        self.connection.commit()

    def data_in(self, email, user_name, password):
        try:
            self.cur.execute(
                """INSERT INTO {} (Email,UserName,PassWord) \
                      VALUES ('{}','{}','{}')""".format(self.table_name, email, user_name, password)
            )

            self.connection.commit()
            print("数据插入成功")
        except Exception as e:
            if not self.is_table_live(self.table_name):
                self.creat_table()
                self.data_in(email, user_name, password)
                print("似乎好像出了点错 ")
            print(e)

    def delete_by_email(self, email):
        self.cur.execute("DELETE from {} where Email = '{}';".format(self.table_name, email))

        # 注意SQL Lite之中的列名大小写,似乎不区分
        self.connection.commit()

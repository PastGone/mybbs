import sqlite3

fist_table_name = "USER"


# 数据库管理的父类，名曰数据大师
class Data_master:
    # 初始化方法，需要数据库名称
    def __init__(self, db_name, table_name=fist_table_name):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.connection.cursor()
        self.db_name = db_name
        self.table_name = table_name

    # 作为字符串处理的代码
    def __str__(self):
        return self.db_name

    # 析构函数
    def __del__(self):
        self.close()

    # 管理工具关闭函数
    def close(self):
        self.connection.close()

    # 判断数据表是否存在
    def is_table_live(self, table_name=fist_table_name):
        cursor = self.cur.execute(
            '''select count(*)  from sqlite_master where type='table' and name = '{}';'''.format(table_name)
        )
        a = 0
        for row in cursor:
            a = row[0]

        if a > 0:
            return True
        else:
            return False

    def get_table(self, table_name=fist_table_name):
        cursor = self.cur.execute("SELECT *  from {}".format(table_name))
        for row in cursor:
            print(row)

    # 三个由子类实现的方法 创建表 插入数据
    def creat_table(self):
        pass

    # 注意这里的data in函数必须 对主键要求十分严格否则会报错
    def data_in(self):
        pass

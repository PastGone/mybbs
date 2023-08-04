import sqlite3


# 数据库管理的父类，名曰数据大师
class Data_master:
    instance = None  # 类属性做一个标识

    def __new__(cls, *args, **kwargs):
        if not cls.instance:  # 如果instance为假，则创建一个实例
            cls.instance = super().__new__(cls)

        return cls.instance


    # 初始化方法，需要数据库名称
    def __init__(self, db_name, table_name=''):
        if table_name == '':
            print("必须指定表的名称才能初始化类")
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cur = self.connection.cursor()
        self.db_name = db_name
        self.table_name = table_name
        if not self.is_table_live():
            self.creat_table()

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
    def is_table_live(self):
        cursor = self.cur.execute(
            '''select count(*)  from sqlite_master where type='table' and name = '{}';'''.format(self.table_name)
        )
        a = 0
        for row in cursor:
            a = row[0]

        if a > 0:
            return True
        else:
            return False

    def get_table(self):
        cursor = self.cur.execute("SELECT *  from {}".format(self.table_name))
        for row in cursor:
            print(row)

    # 三个由子类实现的方法 创建表 插入数据
    def creat_table(self):
        pass

    # 注意这里的data in函数必须 对主键要求十分严格否则会报错
    def data_in(self):
        pass

import uuid

from db_tools.data_master import Data_master


class Post_data_master(Data_master):
    # 初始化方法，需要数据库名称
    def __init__(self, db_name, table_name='post'):
        self.db_name = db_name
        self.table_name = table_name
        self.continue_init()
    def creat_table(self):
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS {} 
                    (PostId CHAR(32) PRIMARY KEY     NOT NULL,
                    PostName CHAR(128) NOT NULL ,
                    PostContent TXET NOT NULL ,
                    ofZoneId CHAR(3) NOT NULL ,
                    ofEmail EMAIL CHAR(50) NOT NULL ,
                    COUNT   MEDIUMINT   NOT NULL,
                    CreatedTime TimeStamp NOT NULL DEFAULT (datetime('now','localtime')));'''.format(self.table_name)
        )
        print("数据表创建成功")
        self.connection.commit()

    def get_reply(self):
        pass
        # lst = []
        # cursor = self.cur.execute("SELECT *  from {}".format(self.table_name))
        # # print(type(cursor))
        # for row in cursor:
        #     # print(type(row))
        #     # print(row)
        #     lst.append(row)
        # return lst

    def data_in(self, post_name, postContent, of_Zone_Id, email):
        post_id = str(uuid.uuid1())
        try:
            self.cur.execute(
                """INSERT INTO {} (PostId,PostName,PostContent,ofZoneId,ofEmail,COUNT) \
                      VALUES ('{}','{}','{}','{}','{}',0)""".format(self.table_name, post_id, post_name, postContent,
                                                               of_Zone_Id, email)
            )
            self.connection.commit()
            print("数据插入成功")
        except Exception as e:
            print(e)

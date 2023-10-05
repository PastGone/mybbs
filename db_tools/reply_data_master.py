from db_tools.data_master import Data_master
import uuid


class Reply_data_master(Data_master):
    # 初始化方法，需要数据库名称
    def __init__(self, db_name, table_name='reply'):
        self.db_name = db_name
        self.table_name = table_name
        self.continue_init()


    def creat_table(self):
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS {} 
                    (ReplyId CHAR(32) PRIMARY KEY NOT NULL, 
                    ofPostId CHAR(32) NOT NULL,
                    ofReplyId CHAR(32)  NOT NULL, 
                    ofEmail CHAR(3) NOT NULL ,
                    ReplyContent TXET NOT NULL ,
                    ReplyCount   MEDIUMINT   NOT NULL,
                    CreatedTime TimeStamp NOT NULL DEFAULT (datetime('now','localtime')));'''.format(self.table_name)
        )
        print("数据表创建成功")
        self.connection.commit()

    def get_zone(self):
        lst = []
        cursor = self.cur.execute("SELECT *  from {}".format(self.table_name))
        # print(type(cursor))
        for row in cursor:
            # print(type(row))
            # print(row)
            lst.append(row)
        return lst

    def data_in(self, ofPostId, ofReplyId, ofEmail, ReplyContent, ReplyCount):
        reply_id = str(uuid.uuid1())
        try:
            self.cur.execute(
                """INSERT INTO {} (ReplyId,ofPostId,ofReplyId,ofEmail,ReplyContent,ReplyCount) \
                      VALUES ('{}','{}','{}','{}','{}',0)""".format(self.table_name, reply_id, ofPostId, ofReplyId, ofEmail,
                                                               ReplyContent)
            )
            self.connection.commit()
            print("数据插入成功")
        except Exception as e:
            print(e)

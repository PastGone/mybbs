from db_tools.data_master import Data_master


class Zone_data_master(Data_master):
    def creat_table(self):
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS {} 
                    (ZoneName CHAR(16) PRIMARY KEY     NOT NULL,
                    ZoneId CHAR(3) NOT NULL ,
                    COUNT   MEDIUMINT   NOT NULL,
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

    def data_in(self, zone_name, zone_id):

        try:
            self.cur.execute(
                """INSERT INTO {} (ZoneName,ZoneId,COUNT) \
                      VALUES ('{}','{}',0)""".format(self.table_name, zone_name, zone_id)
            )
            self.connection.commit()
            print("数据插入成功")
        except Exception as e:
            print(e)

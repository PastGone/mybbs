# 导入简单的数据库的库
from db_tools.login_data_master import Login_data_master
from db_tools.register_data_master import Register_data_master
from db_tools.zone_data_master import Zone_data_master
from db_tools.reply_data_master import Reply_data_master
from db_tools.post_data_master import Post_data_master


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
    ldm = Login_data_master("../db/BBS.db", "account")
    ldm.data_in("2735956898@qq.com", "大橘子", "qq123456")
    ldm.get_table()
    ldm.get_email("2735956898@qq.com")
    # ldm.delete_by_email("2085765742@qq.com")
    print(ldm.get_password_by_email("2735956898@qq.com"))


def test3():
    zdm = Zone_data_master("../db/BBS.db", "zone")
    zdm.data_in(zone_name="旅途————测试", zone_id=666)
    zdm.get_zone()


def test4():
    pdm = Post_data_master("../db/BBS.db", "post")
    pdm.data_in(post_name="本论坛的一个帖子",
                postContent="""旅途的第一步，
                当你重新踏上旅途之后，一定要记得旅途本身的意义。
                提瓦特的飞鸟、诗和城邦，女皇、愚人和怪物……都是你旅途的一部分。
                终点并不意味着一切，在抵达终点之前，
                用你的眼睛，多多观察这个世界吧……""",
                of_Zone_Id=666, email="2735956898@qq.com")


def test5():
    rdm = Reply_data_master("../db/BBS.db", "reply")
    rdm.data_in(ofEmail="2735956898@qq.com", ofReplyId=0, ofPostId="45195b13-24ac-11ee-9998-b48c9d70ae61", ReplyCount=0,
                ReplyContent="""是你沿途所见的风景，遇到的人，解决的事……
                 切记初次在风龙废墟面对遮天蔽日的特瓦林的身影； 
                 初次面对跋掣时，八个巨大蛇头，天空如同被破开的旋转云层； 
                 初次登上庆云顶，俯视着绝云涧的云雾缭绕之美景； 初次登上龙脊雪山，看着萦绕在山顶的旋转的暴风雪云层；
                初次去摘星崖，面对大海与起始海滩的感叹； 初次来到稻妻，为将军阁的壮美，为天云垰的空中平台，为海祁岛的如梦似幻，为渊下宫的绝景…… 
                  游戏中后期你会感到腻味，但是你初次面对这些景色，即使它是假的，是0与1的堆砌，但是那一瞬间的感情，不是虚假的，旅途所见才是关键。""")


# 下面的部分用来测试用例保证 该类工具 的健全性
if __name__ == "__main__":
    # test1()
    # test2()
    # #
    test3()
    pass

    # test4()
    pass
    # test5()
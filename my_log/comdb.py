import pymysql

table_name = "logs"


class MysqlDb(object):
    """

    """
    def __init__(self, config):
        # print(config)
        try:
            self.conn = pymysql.connect(**config)
            self.conn.autocommit(1)
            self.cursor = self.conn.cursor()
        except:
            return "数据库连接失败"
        try:
            my_add_table = "CREATE TABLE %s(id int  AUTO_INCREMENT primary key,project varchar(30)," \
                           "level int,detail TEXT,principal varchar(30),ip varchar(30),time varchar(30))" % table_name
            # print(my_add_table)
            self.cursor.execute(my_add_table)
        except:
            pass

    def add(self, my_dict):
        project = my_dict.get("project")
        level = int(my_dict.get("level"))
        detail = my_dict.get("detail")
        principal = my_dict.get("principal")
        ip = my_dict.get("ip")
        time = my_dict.get("time")
        my_sql_add = "insert into %s(project,level,detail,principal,ip,time) " \
                     "values('%s',%d,'%s','%s','%s','%s');" \
                     % (table_name, project, level, detail, principal, ip, time)
        # print(my_sql_add)
        self.cursor.execute(my_sql_add)

    def delsql(self):
        pass

    def updata(self):
        pass

    def check(self):
        pass

    def end(self):
        # 关闭游标连接
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()


def mysql(config, my_dict):
    # print(config, my_dict)
    my_db = MysqlDb(config)
    my_db.add(my_dict)
    my_db.end()

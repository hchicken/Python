# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2019/11/16 15:50


import pymysql


class SessionDb():
    """封装好连接DB的类
    """

    def __init__(
            self,
            host: str,
            user: str,
            password: str,
            database: str,
            port=3306,
            charset="utf8") -> None:
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            database=database,
            charset=charset)
        self.__session = self.conn.cursor()

    def __enter__(self):
        return self.__execute

    def __exit__(self, *args, **kwargs):
        self.conn.commit()
        return self.__session.close()

    def __execute(self, cmd):
        self.__session.execute(cmd)
        return self.__session.fetchall()


if __name__ == "__main__":
    host = "xxx.xxx.xxx.xxx"
    user = "xxx"
    password = "xxx"
    database = "xxx"
    cmd = "select * from xxx"
    with SessionDb(host, user, password, database) as s:
        s(cmd)

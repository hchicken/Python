# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2019/11/16 15:56


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import datetime


class DbBase(object):
    def __init__(self):
        self.engine = create_engine(
            'mysql+pymysql://tan:tan@10.1.14.167:3306/ck',
            max_overflow=0,  # 超过连接池外最多创建的连接
            pool_size=5,  # 连接池大小
            pool_timeout=30,  # 池中没有线程最多等待时间，否则报错
            pool_recycle=-1,  # 多久之后对线程池中的线程进行连接回收（重置）
            encoding='utf-8',
            echo=True, )

        session = sessionmaker(bind=self.engine)
        # 实例化类

        con = scoped_session(session)


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), index=True, nullable=True)

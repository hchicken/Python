#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/30 16:00
# @Author  : Greens

class List:

    def __init__(self):
        self.list = []

    def put(self, t):
        """
        插进入数据
        """
        self.list.append(t)

    def insert(self, index: int, t):
        """
        指定位置插入
        """
        self.list.insert(index, t)

    def __str__(self):
        """
        打印时转换
        """
        return str(self.list)

    def remove(self, t):
        """
        移除元素
        """
        return self.list.remove(t)

    def size(self):
        """
        获取大小
        """
        return len(self.list)

    def isEmpty(self):
        """
        置空
        """
        return self.list == []


if __name__ == "__main__":
    my_list = List()
    my_list.put("test")
    my_list.insert(0, "test1")
    my_list.remove("test")
    print(my_list)

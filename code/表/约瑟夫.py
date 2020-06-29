#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 20:12
# @Author  : Greens


class Node:
    """
    定义一个节点
    """

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Joseph:
    """
    约瑟夫问题
    """

    def __init__(self):
        self.__first = None  # 第一个节点
        self.__pre = None  # 记录前一个节点

    def get(self, num):
        """
        获取一个循环链表
        """
        for i in range(1, num + 1):
            if i == 1:
                self.__first = Node(item=i)
                self.__pre = self.__first
            else:
                new_node = Node(item=i)
                self.__pre.next = new_node
                self.__pre = new_node

            if i == num:
                self.__pre.next = self.__first
        return self.__first

    def deal(self):
        """
        处理
        """
        count = 0
        n = self.__first
        before = None
        while n != n.next:
            count += 1
            if count == 3:
                before.next = n.next
                n = n.next
                count = 0

            else:
                before = n
                n = n.next
        print(n.item)


if __name__ == "__main__":
    my_list = Joseph()
    xunhuan = my_list.get(41)
    my_list.deal()

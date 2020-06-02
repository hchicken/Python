#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 08:38
# @Author  : Greens


class Node:
    """
    定义一个节点
    """

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class LinkedList:
    def __init__(self, item=None):
        """
        初始化一个链表
        """
        self.__size = 0
        self.__head = Node(item)

    def is_empty(self):
        """
        判断列表为空
        """
        return self.__size == 0

    def put(self, item):
        """
        在头部插入一个数据
        """
        node = Node(item, self.__head.next)

        self.__head.next = node
        self.__size += 1

    def append(self, item):
        """
        在最后一个节点插入
        """
        node = Node(item)
        n = self.__head

        for i in range(self.__size):
            n = n.next
        n.next = node
        self.__size += 1

    def insert(self, index: int, item):
        """
        指定位子添加
        """
        # 相应索引处添加
        if index <= self.__size:
            n = self.__head
            # 获取对应索引的节点
            for i in range(index):
                n = n.next
            # 获取后面节点
            r_next = n.next
            node = Node(item, r_next)
            n.next = node
            self.__size += 1
        else:
            print("插入失败")

    def get(self, index):
        """
        获取索引处的节点
        """
        if index <= self.__size:
            node = self.__head
            for i in range(index):
                node = node.next
            return node.item

    def remove(self, index: int):
        """
        删除指定位置的节点
        """
        if index < self.__size:
            n = self.__head.next
            for i in range(index):
                n = n.next
            # 需要删除的节点
            d_next = n.next
            # 删除节点
            n.next = n.next.next
            self.__size -= 1
            return d_next.item
        return

    def size(self):
        """
        返回链表的长度
        """
        return self.__size

    def clear(self):
        """
        链表置空
        """
        self.__head = Node()
        self.__size = 0

    def __str__(self):
        """
        打印链表是输出
        """
        p = self.__head
        ret_lit = []
        while p:
            ret_lit.append(p.item)
            p = p.next
        return str(ret_lit)

    def reverse(self):
        """
        反转链表
        """
        if self.is_empty():
            return
        else:
            self.__reverse(self.__head.next)

    def __reverse(self, node):
        """
        反转
        """
        # 当最后一个节点时next为null
        if node.next == None:
            self.__head.next = node
            return node
        pre = self.__reverse(node.next)
        pre.next = node
        node.next = None
        return node


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.put("1")
    my_list.put("2")


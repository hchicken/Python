#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/4 08:49
# @Author  : Greens


class Node:
    """
    节点
    """

    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next


class SymbolTable():
    """
    符号表
    """

    def __init__(self):
        self.__head = Node()
        self.__size = 0

    def put(self, key, val):
        """
        插入：插入双节点中间
        """
        pre = self.__head
        curr = self.__head.next

        while curr and key < curr.key:
            pre = curr
            curr = curr.next
        # 存在时不插入
        if curr and key == curr.key:
            curr.val = val
            return
        new_node = Node(key, val, curr)
        pre.next = new_node
        self.__size += 1

    def delete(self, key):
        """
        删除
        """
        n = self.__head
        # 是否存在key
        for i in range(self.__size):
            n = n.next
            if n.next.key == key:
                n.next = n.next.next
                self.__size -= 1
                return

    def get(self, key):
        """
        查询
        """
        n = self.__head
        # 是否存在key
        for i in range(self.__size):
            n = n.next
            if n.key == key:
                return n.val

    def size(self):
        """
        符号表
        """
        return self.__size

    def __str__(self):
        """
        打印
        """
        ret = {}
        n = self.__head.next
        while n != None:
            ret[n.key] = n.val
            n = n.next
        return str(ret)


if __name__ == "__main__":
    my_list = SymbolTable()
    my_list.put(1, "t1")
    my_list.put(10, "t2")
    my_list.put(3, "t2")
    print(my_list.size())
    print(my_list)
    print(my_list.get((1)))
    my_list.delete(1)
    print(my_list)
    print(my_list.size())

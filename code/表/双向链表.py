#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/31 09:49
# @Author  : Greens


class Node:
    """
    定义一个双向链表节点
    """

    def __init__(self, item=None, pre=None, next=None):
        """
        pre: 上一个节点
        item: 值
        next: 下一个节点
        """
        self.pre = pre
        self.item = item
        self.next = next


class TowWayLinkList:
    """
    定义一个双喜是
    """

    def __init__(self):
        self.__head = Node()
        self.__size = 0

    def is_empty(self):
        """
        判断列表为空
        """
        return self.__size == 0

    def clear(self):
        """
        清空
        """

        self.__head.next = None
        self.__size = 0

    def put(self, item):
        """
        头部添加
        """
        # 链表是否为空
        if self.is_empty():
            # 为空时添加
            new_node = Node(item=item)
            self.__head = new_node
        else:
            node = self.__head
            new_node = Node(item=item, next=node)
            node.pre = new_node
            self.__head = new_node

    def appent(self, item):
        """
        在最后一个节点插入
        """
        # 链表是否为空
        if self.is_empty():
            # 为空时添加
            new_node = Node(item=item)
            self.__head = new_node
        else:
            node = self.__head
            for i in range(self.__size):
                node = node.next
            new_node = Node(pre=node, item=item)
            node.next = new_node
        self.__size += 1

    def insert(self, index, item):
        """
        在指定位置插入节点
        """
        if index <= self.__size:
            node = self.__head
            for i in range(index):
                node = node.next
            new_node = Node(pre=node.pre, item=item, next=node)

            node.pre.next = new_node
            node.pre = new_node
            self.__size += 1

    def get(self, index):
        """
        获取节点数据
        """
        if index <= self.__size:
            node = self.__head
            for i in range(index):
                node = node.next
            return node.item

    def remove(self, index):
        """
        删除指定索引的节点
        """
        if index <= self.__size:
            node = self.__head
            for i in range(index):
                node = node.next
            item = node.item
            # 当删除第一个节点时
            if node.pre != None:
                node.pre.next = node.next
                # 当删除最后一个节点时为空
                if node.next != None:
                    node.next.pre = node.pre

            else:
                node = node.next
                node.pre = None
                self.__head = node
            self.__size -= 1
            return item

    def items(self):
        ret = []
        p = self.__head
        while p:
            ret.append(p.item)
            p = p.next
        return ret

    def __str__(self):
        """
        打印的时候出现
        """
        ret = []
        p = self.__head
        while p:
            ret.append(p.item)
            p = p.next
        return str(ret)


if __name__ == "__main__":
    my_list = TowWayLinkList()
    my_list.appent("1")
    my_list.put("1")
    my_list.insert(1, 2)
    my_list.appent("3")
    my_list.appent("4")
    # my_list.remove(0)
    print(my_list)
    print(my_list.remove(1))
    print(my_list)
    print(my_list.get(2))

    for i in my_list.items():
        print(i)

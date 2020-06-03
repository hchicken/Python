#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 21:57
# @Author  : Greens


class Node():
    """
    定义一个节点
    """

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Queue():
    """
    队列
    """

    def __init__(self):
        self.__head = Node(None)
        self.__last = None
        self.__size = 0

    def en_queue(self, item):
        """
        进队列
        """
        new_node = Node(item)
        if not self.__last:

            self.__last = new_node
            self.__head.next = self.__last
        else:
            old_last = self.__last
            self.__last = new_node
            old_last.next = self.__last
        self.__size += 1

    def is_empty(self):
        """
        判断队列是否为空
        """
        return self.__size == 0

    def de_queue(self):
        """
        出队列
        """
        # 判断队列是否为空
        if self.is_empty():
            return None
        # 需要出的节点
        old_node = self.__head.next
        self.__head.next = old_node.next
        self.__size -= 1
        return old_node.item

    def size(self):
        """
        获取队列的大小
        """
        return self.__size

    def __str__(self):
        """
        打印的时候触发
        """
        q = self.__head.next
        ret = []
        while q:
            ret.append(q.item)
            q = q.next
        return str(ret)


if __name__ == "__main__":
    my_queue = Queue()
    my_queue.en_queue(1)
    my_queue.en_queue(2)
    my_queue.en_queue(3)
    a = my_queue.de_queue()
    print(a)
    print(my_queue)
    size = my_queue.size()
    print(size)

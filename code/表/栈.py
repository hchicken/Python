#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/2 20:59
# @Author  : Greens


class Node:
    """
    定义一个节点
    """

    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class Stack:
    """
    栈
    """

    def __init__(self):
        self.__head = Node()
        self.__size = 0

    def push(self, item):
        """
        压栈
        """
        old_node = self.__head.next
        new_node = Node(item=item)
        new_node.next = old_node
        self.__head.next = new_node
        self.__size += 1

    def pop(self):
        """
        弹栈
        """
        item = None
        if self.__size != 0:
            item = self.__head.next.item
            self.__head.next = self.__head.next.next
            self.__size -= 1
        return item

    def size(self):
        """
        栈的元素大小
        """
        return self.__size

    def __str__(self):
        """
        自定义的响应
        """
        p = self.__head.next
        ret = []
        while p != None:
            ret.append(p.item)
            p = p.next
        return str(ret)


def deal():
    my_strs = "((tanzhihao))"

    my_dict = {
        "}": "{",
        ")": "(",
        "]": "["
    }
    my_stack = Stack()
    for my_str in my_strs:
        if my_str in ["(", "[", "{"]:
            my_stack.push(my_str)
        if my_str in [")", "]", "}"]:
            if my_dict[my_str] != my_stack.pop():
                return False

    return my_stack.size() == 0


if __name__ == "__main__":
    a = deal()
    print(a)

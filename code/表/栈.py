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
        # 久节点
        old_node = self.__head.next
        # 需要进栈的节点
        new_node = Node(item=item)
        # new next 为 old
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


def parentheses():
    """
    括号匹配
    """
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


def count(my_str):
    pass


def polish(my_list: list) -> int:
    """
    逆波兰
    """
    my_stack = Stack()
    sum = 0
    for i in my_list:
        if isinstance(i, int):
            my_stack.push(i)
        else:
            num1 = my_stack.pop()
            num2 = my_stack.pop()
            if i == "+":
                sum = num2 + num1
            if i == "-":
                sum = num2 - num1
            if i == "*":
                sum = num2 * num1
            if i == "/":
                sum = num2 / num1
            my_stack.push(sum)
    return my_stack.pop()


if __name__ == "__main__":
    ret = property()
    print(ret)
    my_list = [4, 1, 2, 8, "+", "-", "*"]
    ret1 = polish(my_list)
    print(ret1)

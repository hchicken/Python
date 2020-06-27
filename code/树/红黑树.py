#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/27 17:57
# @Author  : Greens


Red = "red"
Black = "black"


class Node:
    def __init__(self, key=None, value=None, left=None, right=None, color="black"):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.root = None
        self.__size = 0

    def is_red(self, node):
        """
        判断节点是不是红链接
        """
        if node:
            return node.color == Red
        else:
            return False

    def rotateLeft(self, h):
        """
        左旋
        """

        # 获取h的右子节点为x节点
        x = h.right
        # 让x的左子节点为h的右子节点
        h.right = x.left
        # 让h为x的左子节点
        x.left = h
        # 让x的color属性等于h节点的color属性
        x.color = h.color
        # 让h节点的color属性变为red
        h.color = "red"
        return x

    def rotateRight(self, h):
        """
        右旋
        """
        # 获取h的节点的左子节点为x
        x = h.left
        # 让x的右子节点为h的左子节点
        h.left = x.right
        # 让h节点为x节点的右子节点
        x.right = h
        # x的color为h的color
        x.color = h.color
        # 让h的color为红
        h.color = "red"
        return x

    def flip_color(self, h):
        """
        颜色反转
        """
        # h 节点color 为红
        h.color = Red
        # h的左右节点颜色均为黑
        h.left.color = Black
        h.right.color = Black
        return h

    def put(self, key, value):
        """
        插入
        """
        self.root = self.__put(self.root, key, value)
        self.root.color = Black

    def __put(self, node, key, value):
        if not node:
            self.__size += 1
            return Node(key, value, None, None, Red)

        if key > node.key:
            # 往右
            node.right = self.__put(node.right, key, value)
        elif key < node.key:
            # 往左
            node.left = self.__put(node.left, key, value)
        else:
            # 值替换
            node.value = value

        # 左旋判断,左子节点为黑，有节点为红
        if self.is_red(node.right) and not self.is_red(node.left):
            node = self.rotateLeft(node)

        # 右旋判断，左子节点为红，左子节点的左子节点为红
        if self.is_red(node.left) and self.is_red(node.left.left):
            node = self.rotateRight(node)

        if self.is_red(node.left) and self.is_red(node.right):
            node = self.flip_color(node)
        return node

    def get(self, key):
        root = self.root
        val = self.__get(root, key)
        return val

    def __get(self, node, key):
        """
        私有化获取
        """
        if not node:
            return None

        if key > node.key:
            # 往右
            return self.__get(node.right, key)
        elif key < node.key:
            # 往左
            return self.__get(node.left, key)
        else:
            return node.value


if __name__ == '__main__':
    my_tree = RedBlackTree()
    my_tree.put("1", "test1")
    my_tree.put("2", "test2")
    my_tree.put("3", "test3")
    my_tree.put("4", "test4")
    a1 = my_tree.get("3")
    print(a1)
    a1 = my_tree.get("2")
    print(a1)
    a1 = my_tree.get("3")
    print(a1)

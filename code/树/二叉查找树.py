#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/7 16:32
# @Author  : Greens


class Node:
    def __init__(self, key=None, value=None, left=None, right=None):
        """
        树的节点
        """
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        """

        """
        self.__root = None
        self.__size = 0

    def put(self, key, val):
        """
        插入 key value
        """

        root = self.__put(self.__root, key, val)
        self.__root = root

    def __put(self, node, key, val):
        """
        pass
        """
        # 子树为空
        if not node:
            self.__size += 1
            return Node(key=key, value=val)
        if key > node.key:
            node.right = self.__put(node.right, key, val)
        elif key < node.key:
            node.left = self.__put(node.left, key, val)
        else:
            node.value = val
        return node

    def get(self, key):
        """
        查询val
        """
        val = self.__get(self.__root, key)
        return val

    def __get(self, node, key):
        """
        私有查询
        """
        if not node:
            return None
        if key > node.key:
            val = self.__get(node.right, key)
        elif key < node.key:
            val = self.__get(node.left, key)
        else:
            val = node.value
        return val

    def delete(self, key):
        """
        删除
        """
        node = self.__del(self.__root, key)
        self.__root = node
        self.__size -= 1

    def __del(self, node, key):
        """
        删除
        """
        if not node:
            return None
        if key > node.key:
            node.right = self.__del(node.right, key)
        elif key < node.key:
            node.right = self.__del(node.left, key)
        else:
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            right = node.right  # 右子树
            # 查找右子树的左子树
            while right.left:
                right = right.left
            n = node.right
            # 断开有子树的左子树
            while n.left:
                if n.left.left:
                    n = n.left
                else:
                    n.left = None
            right.left = node.left
            right.right = node.right
            node = right
        return node

    def size(self):
        """
        查询大小
        """
        return self.__size


if __name__ == "__main__":
    my_tree = Tree()
    my_tree.put(1, "test1")
    my_tree.put(2, "test2")
    my_tree.put(3, "test3")
    my_tree.delete(2)
    print(my_tree.get(3))
    print(my_tree.size())

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

    def get_min(self):
        """
        查找最小值
        """
        node = self.__root
        while node.left:
            node = node.left
        return node.value

    def get_max(self):
        """
        查询最小值
        """
        node = self.__root
        while node.right:
            node = node.right
        return node.value

    def pre_ergodic(self):
        """
        前序遍历
        """
        my_keys = []
        self.__pre_ergodic(self.__root, my_keys)
        return my_keys

    def __pre_ergodic(self, node, keys):
        """
        私有化方法 前序遍历
        """
        if not node:
            return
        keys.append(node.key)
        if node.left:
            self.__pre_ergodic(node.left, keys)
        if node.right:
            self.__pre_ergodic(node.right, keys)

    def mid_ergodic(self):
        """
        中序遍历
        """
        my_keys = []
        self.__mid_ergodic(self.__root, my_keys)
        return my_keys

    def __mid_ergodic(self, node, keys):
        """
        私有化
        """
        if not node:
            return
        if node.left:
            self.__mid_ergodic(node.left, keys)
        keys.append(node.key)
        if node.right:
            self.__mid_ergodic(node.right, keys)

    def last_ergodic(self):
        """
        后序排序
        """
        my_keys = []
        self.__last_ergodic(self.__root, my_keys)
        return my_keys

    def __last_ergodic(self, node, keys):
        """
        私有化后序遍历
        """
        if not node:
            return
        if node.left:
            self.__last_ergodic(node.left, keys)
        if node.right:
            self.__last_ergodic(node.right, keys)
        keys.append(node.key)

    def layer_ergodic(self):
        """
        层序遍历
        """
        nodes = [self.__root]
        keys = []
        while nodes:
            node = nodes.pop(0)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            keys.append(node.key)

        return keys

    def max_depth(self):
        """
        获取整个数的最大深度
        """
        ret = self.__max_depth(self.__root)
        return ret

    def __max_depth(self, node):
        """
        获取指定数的最大深度
        """
        if not node:
            return 0

        max_l = 0  # 左子树的最大深度
        max_r = 0  # 右子树的最大深度
        # 左子树的最大深度
        if node.left:
            max_l = self.__max_depth(node.left)

        # 右子树的最大深度
        if node.right:
            max_r = self.__max_depth(node.right)

        max = max_r if max_r > max_l else max_l

        return max + 1

    def size(self):
        """
        查询大小
        """
        return self.__size


if __name__ == "__main__":
    my_tree = Tree()
    my_tree.put(2, 2)
    my_tree.put(3, 3)
    my_tree.put(8, 8)
    my_tree.put(9, 9)
    my_tree.put(4, 4)
    my_tree.put(5, 5)
    my_tree.put(1, 1)
    my_tree.put(7, 7)
    print(my_tree.max_depth())
    print(my_tree.get_min())
    print(my_tree.get_max())
    print(my_tree.pre_ergodic())
    print(my_tree.mid_ergodic())
    print(my_tree.last_ergodic())
    print(my_tree.layer_ergodic())
    print(my_tree.max_depth())

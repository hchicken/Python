#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 17:57
# @Author  : Greens


class Heap:
    """
    堆
    """

    def __init__(self):
        """
        初始化
        """
        self.items = []
        self.__size = 0

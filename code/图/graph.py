#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 11:19
# @Author  : Greens


class Graph():

    def __init__(self, V: int):
        self.V = V
        self.E = 0
        self.adj = self.makeAdj()

    def makeAdj(self):
        """
        生成adj
        """
        my_dict = {}
        for i in range(self.V):
            my_dict.setdefault(i, [])

        return my_dict

    def addEdge(self, v, w):
        """
        添加边
        """
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1

    def get_v(self):
        """
        获取点的数量
        """
        return self.V

    def get_e(self):
        """
        获取边的数量
        """
        return self.E



if __name__ == '__main__':
    g = Graph(13)
    g.addEdge(0, 5)
    print(g)

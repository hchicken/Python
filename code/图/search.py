#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 11:30
# @Author  : Greens


from graph import Graph


class Depth:
    """
    深度优先
    """

    def __init__(self, g):
        self.graph = g
        self.__marked = {}
        self.__count = 0
        self.edgeTo = {}

    def search(self, v):
        self.__marked[v] = True
        for w in self.graph.adj[v]:
            if not self.__marked.setdefault(w, False):
                self.search(w)
        self.__count += 1

    def paths(self, v):
        """
        路径
        """
        self.__marked[v] = True
        for w in self.graph.adj[v]:
            if not self.__marked.setdefault(w, False):
                self.edgeTo[w] = v
                self.paths(w)

    def count(self):
        return self.__count

    def marked(self, v):
        return self.__marked.setdefault(v, False)

    def get_path(self, v):
        my_list = []
        while v:
            my_list.insert(0, str(v))
            v = self.edgeTo.setdefault(v, False)
        my_list.insert(0, str(v))

        return "-->".join(my_list)


class Breadth:
    """
    广度优先
    """

    def __init__(self, g):
        self.__graph = g
        self.__marked = {}
        self.__count = 0
        self.__waitSearch = []

    def search(self, v):
        self.__marked[v] = True
        self.__waitSearch.append(v)
        while self.__waitSearch:
            wait = self.__waitSearch.pop()
            for w in self.__graph.adj[wait]:
                if not self.__marked.setdefault(w, False):
                    self.search(w)

        self.__count += 1

    def count(self):
        return self.__count

    def marked(self, v):
        return self.__marked.setdefault(v, False)


def dept_search():
    g = Graph(13)
    g.addEdge(0, 5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 6)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.addEdge(3, 4)
    g.addEdge(4, 6)

    g.addEdge(7, 8)

    g.addEdge(9, 11)
    g.addEdge(9, 10)
    g.addEdge(9, 12)
    g.addEdge(11, 12)

    my_dept = Depth(g)
    my_dept.search(0)

    print(my_dept.count())
    print(my_dept.marked(5))
    print(my_dept.marked(7))


def breadth_search():
    g = Graph(13)
    g.addEdge(0, 5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 6)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.addEdge(3, 4)
    g.addEdge(4, 6)

    g.addEdge(7, 8)

    g.addEdge(9, 11)
    g.addEdge(9, 10)
    g.addEdge(9, 12)
    g.addEdge(11, 12)

    my_dept = Breadth(g)
    my_dept.search(0)

    print(my_dept.count())
    print(my_dept.marked(5))
    print(my_dept.marked(7))


def paths():
    g = Graph(13)
    g.addEdge(0, 5)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 6)
    g.addEdge(5, 3)
    g.addEdge(5, 4)
    g.addEdge(3, 4)
    g.addEdge(4, 6)

    g.addEdge(7, 8)

    g.addEdge(9, 11)
    g.addEdge(9, 10)
    g.addEdge(9, 12)
    g.addEdge(11, 12)

    my_dept = Depth(g)
    my_dept.paths(0)
    print(my_dept.get_path(6))


if __name__ == '__main__':
    dept_search()
    breadth_search()
    paths()

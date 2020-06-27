#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/14 17:57
# @Author  : Greens


class Heap:
    """
    堆
    """

    def __init__(self, items: list):
        """
        初始化
        """
        self.items = items
        self.items.insert(0, 0)
        self.__size = len(self.items) - 1

    def insert(self, val):
        """
        插入一个元素
        """
        # 当节点为0是添加堆
        self.items.append(val)
        self.__size += 1
        # size = self.__size
        # while size > 1:
        #     if val > self.items[size // 2]:
        #         self.items[size], self.items[size // 2] = self.items[size // 2], self.items[size]
        #         size = size // 2
        #     else:
        #         break
        self.swim()

    def swim(self):
        """
        上浮
        """
        size = self.__size
        val = self.items[size]
        while size > 1:
            if val > self.items[size // 2]:
                self.items[size], self.items[size // 2] = self.items[size // 2], self.items[size]
                size = size // 2
            else:
                break

    def sink(self, size):
        """
        下沉
        size:需要下沉的元素Index
        """
        if self.__size < 1:
            return
        val = self.items[size]
        while 2 * size <= self.__size:
            # 判断出左右节点中的最大值
            r = self.items[2 * size]
            if 2 * size + 1 > self.__size:
                max_num = r
            else:
                l = self.items[2 * size + 1]
                max_num = max(r, l)
            # 比较节点与子节点的最大
            if val < max_num:
                index = 2 * size if r == max_num else 2 * size + 1
                self.items[size], self.items[index] = self.items[index], self.items[size]
                # 如果Index为单说明是节点与右子节点替换
                size = 2 * size + index % 2
            else:
                break

    def delMax(self):
        """
        删除堆的最大值
        """
        val = self.items[1]
        # 替换堆顶
        self.items[self.__size], self.items[1] = self.items[1], self.items[self.__size]
        # 删除最大值
        self.__size -= 1
        self.items.pop()
        self.sink(1)
        return val

    def get_heap(self):

        index = self.__size // 2
        for i in range(index, 0, -1):
            self.sink(i)

    def sort(self):
        my_list = []
        for i in range(1,self.__size+1):
            my_list.append(self.delMax())
        return my_list

    def __str__(self):
        return str(self.items)


if __name__ == '__main__':
    # my_heap = Heap()
    # my_heap.insert(1)
    # my_heap.insert(3)
    # my_heap.insert(2)
    # my_heap.insert(4)
    # my_heap.insert(5)
    # my_heap.insert(1)
    # my_heap.insert(9)
    # my_heap.insert(7)
    # my_heap.delMax()
    # # my_heap.delMax()
    # print(my_heap)

    my_heap = Heap([1, 2, 3, 4, 5, 6, 7, 8])
    my_heap.get_heap()
    print(my_heap.sort())

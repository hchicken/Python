# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : Chicken dishes
# Created Time : 2020/1/3 20:54

"""
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
1.     1
2.     11
3.     21
4.     1211
5.     111221
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        num = self.countAndSay(n - 1) + "*"
        temp = list(num)
        count = 1
        strBulider = ''
        # print(len(temp))
        for i in range(len(temp) - 1):
            if temp[i] == temp[i + 1]:
                count += 1
            else:
                strBulider += str(count) + temp[i]
                count = 1
        return strBulider


if __name__ == "__main__":
    my_class = Solution()
    my_def = my_class.countAndSay(5)
    print(my_def)

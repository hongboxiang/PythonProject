#http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317852443934a86aa5bb5ea47fbbd5f35282b331335000#0
# map/reduce练习


# -*- coding: utf-8 -*-
from functools import reduce

# #1
# def normalize(name):
#     # return name[0].upper() + name[1:].lower()
#     return name.capitalize()
#
#
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)
#
# #2
# def prod(L):
#     return reduce(lambda x, y: x * y, L)
#
#
# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
#
# #3
# def str2float(s):
#     s.strip()
#     l = s.split('.')
#     if l.__len__() > 1:
#         n1 = reduce(fn, map(char2num, l[0]))
#         n2 = reduce(fn, map(char2num, l[1])) / (10 ** len(l[1]))
#         return n1 + n2
#     else:
#         return reduce(fn, map(char2num, s))
#
#
# def fn(x, y):
#     return x * 10 + y
#
#
# def char2num(s):
#     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
#
# print('str2float(\'123.456\') =', str2float('123.456'))

#-------------------------------filter
# def is_palindrome(n):
#     s = str(n)
#     i = 0
#     while(i<s.__len__()/2):
#         if s[i] != s[-i-1]:
#             return False
#         i += 1
#     return True

# def is_palindrome(n):
#     if str(n) == str(n)[::-1]:
#         return n
#
# # 测试:
# output = filter(is_palindrome, range(1, 1000))
# print(list(output))


#-------------------------------@property
# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        self.__height = value

    @property
    def resolution(self):
        return self.__width * self.__height
# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
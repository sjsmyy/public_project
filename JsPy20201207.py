# coding=utf-8
# JsPy20201207
# This is First Py
# 科学计算库存1
# 构建函数求平方&立方
# 常规方法求的二、三次方的列表和平方的列表的合集
def CreateList(n, num):
    lista = list(range(n))
    for i in lista:
        lista[i] = i ** num
    return lista

# 构建函数求和
def pySum(n):
    a = CreateList(n, 2)
    b = CreateList(n, 3)
    c = []
    print(a)
    print(b)
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c
c = pySum(10)
print(c)

# NumPy方法求的二、三次方的列表和平方的列表的合集
import numpy as np
def NumSumPy(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c
c = NumSumPy(10)
print(c)

# 创建一维数组
d = np.array([1, 2, 3, 4])
print(d[2])
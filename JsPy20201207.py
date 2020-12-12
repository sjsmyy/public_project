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
   # print(a)
   # print(b)
    for i in range(len(a)):
        c.append(a[i]+b[i])
    return c
c = pySum(10)
# print(c)

# NumPy方法求的二、三次方的列表和平方的列表的合集
import numpy as np
def NumSumPy(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c
c = NumSumPy(10)
# print(c)

# 创建一维数组
d = np.array([1, 2, 3, 4])
# print(d[2])

# 创建多维数组
d = np.array([np.array([1, 2, 3, 4]), np.array([5, 6, 7, 8])])
# print(d.shape)

# 作业：
# 创建类Restaurant()
class Restaurant():
    def __init__(self,c_name, c_type):
        self.restaurant_name = c_name
        self.cuisine_type = c_type
    def describe_restaurant(self):
        print("餐馆的名称是：", self.restaurant_name)
        print("餐馆的种类是：", self.cuisine_type)
    def open_status(self):
        print("餐馆正在营业")
# 创建对象
restaurant1 = Restaurant("海底捞", "火锅")
print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
restaurant1.open_status()
restaurant1.describe_restaurant()
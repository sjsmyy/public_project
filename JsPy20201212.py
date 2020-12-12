# coding=utf-8
# 多维数组
# zeros数组
import numpy as np
arr1 = np.zeros((4, 3))
print(arr1)
# ones数组
arr2 = np.ones((4, 3))
print(arr2)
# full数组
arr3 = np.full((3, 3), 9, dtype=np.int8)
print(arr3)
# random数组
arr4 = np.random.random((4, 4))
print(arr4)
# eye数组
arr5 = np.eye(7, k=-2)
print(arr5)

# NumPy数据类型和python的数据类型互相转换
# import numpy as np
a = 44
print(type(a))  # python中的数据类型
print(type(np.int8(a))) # numpy中的数据类型

# 设定好数组之后，获取数组的元素
# 一维数组索引
a1 = np.arange(10)
print(a1)
# 二维数组索引
a2 = np.array([np.arange(3), np.arange(3), np.arange(3)])
print(a2)
print(a2[0][1])
# 三维数组索引
a3 = np.random.randint(1, 100, 27)  # 创建一个一维的27位的从1到100的数组
b3 = a3.reshape([3, 3, 3])  # 使用reshape更改数组的维度，该实例更改一维为三维
print(b3) # 使用reshape更改数组的维度时，要注意前后数组的原属要一致，即数组的元素能整除要更改的维度：27/3=9
print(b3[2, 2, 2])
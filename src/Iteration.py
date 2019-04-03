# 迭代(Iteration) 对于一个集合，循环去遍历的过程，就称为迭代
# 只要是任何可迭代对象，都可以使用for...in迭代 可以通过ollections模块的Iterable类型判断对象是否可迭代
from collections import Iterable
print(isinstance('abc', Iterable))  # 返回True
print(isinstance(123, Iterable))  # 返回False
# 也可以做类似.Net和java中的下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 实际原理就是同时引用两个变量
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
# 示例 使用迭代查找一个list中最小和最大值，并返回一个tuple
min = 0
max = 0
newL = [52, 12, 23, 44, 55, 66, 17, 28, 9]
for i, num in enumerate(newL):
    if i == 0:
        min = num
        max = num
    else:
        if num > max:
            max = num
        elif num < min:
            min = num
print((min, max))
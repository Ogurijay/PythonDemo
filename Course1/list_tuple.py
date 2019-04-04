# 数据类型 列表list和tuple

# list 元素可变 可通过索引取值 len函数计算长度 当索引为负数时 可反向取值 例如：L[-1][-1] 输出 'Lisa'
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# tuple 元素是不可变的 更加安全，但也可通过在tuple中声明可变列表list
print(L[0][0])
print(L[1][1])
print(L[2][2])
L = ('A', 'B', ['a', 'b'])
print(L)
# 当tuple中只定义一个元素 由于小括号既科代表运算也可代表tuple 单个元素的tuple应写为 L('1',) 用逗号隔开
L1 = (1,)  # 结果为(1,)
L2 = (1)  # 结果为1
print(L1)
print(L2)

# 切片 通常取一个list或tuple的前几个元素，我们会使用循环去获取，但在python中提供了切片(Slice)操作符:
# 例如 取前三个元素，使用:操作符则表示为arr[0:3] 也可以简写成arr[:3]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(arr[:3])  # 返回 [1,2,3]
# 也支持倒数切片，倒数第一个元素是-1
print(arr[-3:])  # 返回[8,9,0]
# 拓展用法 可在切片内再次切片
print(arr[:8:2])  # 取出前八个，并每两个取一个，返回[1, 3, 5, 7]
print(arr[::5])  # 所有数，每五个取一个，返回[1，6]
# tuple也可以执行切片操作，但切片结果仍为tuple
print((1, 2, 3, 4, 5)[:2])  # 返回(1,2)
# 同理字符串也可以做切片操作，结果仍为字符串
print(('ABCDEFG')[:4])  # 返回ABCD

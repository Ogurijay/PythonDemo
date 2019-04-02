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

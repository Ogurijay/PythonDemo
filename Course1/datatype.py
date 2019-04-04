# 数据类型及变量（字符串部分的基础知识较长，所以请看str.py文件）

# 布尔值 只有True和False 可通过运算符进行计算 and or not（与或非）
print(True and True)  # and下都为True 输出 True
print(True and False)  # and下有一个为False 输出False
print(5 > 1 and 3 < 2)
print(5 > 1 or 3 < 2)  # or下有一个为Ture 输出True
print(not 5 > 1)  # not 下True与False互换 结果为True时输出False

# 空值 在python中用none表示 none不等于0
print(None)

# 变量 在python中必须是大小写字母、数组和_的组合 且不能以数字开头(与Java和C#、C、C++中相同) 通过=赋值
a = 1
a = '1'  # 在变量中 不固定类型的语言为动态语言 反之则是静态语言

# 常量 是不能变的变量通常用全大写字符来表示
A = 15
B = 7  # 虽然常亮意义上是不可变 但实际上要通过常量做计算也是可以的
print(A+B)
print(A-B)
print(A*B)
print(A/B)
print(A//B)  # 地板除 使两个数字相除之后得出的值为整数
print(A % B)  # 求余

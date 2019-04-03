# 函数

# 函数的参数
# 位置参数 即正常表示的参数，示例如下
def testparam(x, y):
    return x+y
# 默认参数 为了简化函数的调用难度，在一定程度上可以为参数设置默认值。需要注意的是默认参数尽量指向变化小的参数，且一定要是定值，否则随着方法调用次数增加每次返回结果都不同
def testparam1(x, y=1):
    return x+y
print(testparam1(4))  # 返回5
print(testparam1(4, 5))  # 返回9
# 错误示例
def badtest(a=[]):
    a.append('1')
    return a
print(badtest())  # 返回['1']
print(badtest())  # 返回['1','1']
print(badtest())  # 返回['1','1','1']
# 可以通过none来修正上面的函数，使得结果是我们想要的
def goodtest(a=None):
    if a is None:
        a = []
    a.append('1')
    return a
print(goodtest())  # 返回['1']
print(goodtest())  # 返回['1']
print(goodtest())  # 返回['1']
# 可变参数 当在函数中不确定要使用多少个参数时，可以使用可变参数，在变量前加上*
# 可变参数的原理是相当于把list或者tuple当做参数传入函数，但在常规方式中在传入参数前必须要将多个参数封装在列表中。
# 但在函数的定义中可通过在变量前加上*来代表该参数是可变参数，且无需封装。
# 当你要把一个list和tuple作为参数传入时，原方法可能需要你用序列的形式去取出每个元素再传入函数，但通过在列表前加上*，可以简化这个过程,直接传入*list或*tuple即可
def cal(*number):
    return sum(number)
print(cal(*[1, 2, 3]))  # 返回6
# 关键字参数 关键字参数允许你传入0个或任意个含参数名的参数，并且这些关键字在函数内会自动组装成一个dict,关键字参数用**定义
def person(**param):
    return print('person:%s' % param)
person(name='张三', age=14, sex='男')
# 关键字参数也可以使用和可变参数相同的简化写法
dist = {'name': '张三', 'age': 14, 'sex': '男'}
person(**dist)
# 命名关键字参数 需要用特殊分隔符*隔开，可过滤掉无意义的参数，只接收被命名的参数
def sign(name, age, *, tel, email):
    return print('name:', name, 'age:', age, 'tel:', tel, 'eamil', email)
sign('张三', 12, tel='13233112313', email='1324564@qq.com')
# 命名参数也可以在声明时放入默认值，以简化调用，且在有可变参数时，可省略输入分隔符*
def simple(name, age, *arr, tel='1334423123'):
    return print('name:', name, 'age:', age, 'other:', arr, 'tel:', tel)
simple('张三', 20, *['teacher', 'male'])
# 参数组合 参数组合的顺序从左到右必须是必选参数->默认参数->可变参数->命名关键字参数->关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2, *[3, 4, 5], number='123')
f2(1, 2, 3, d=5, **{'type': 'test', 'num': '1'})


# 函数的调用 函数其实就是指向一个函数对象的引用。当把函数赋值给一个变量时，该变量也拥有调用函数的功能，相当于起了一个别名
# 以下是一些常用函数
# help函数 通过help(函数名)可查看函数的帮助信息
help(abs)
# abs函数 返回绝对值 当参数类型不正确时会报异常
print(abs(-20))
# max函数 可接收任意参数 返回其中最大值 也可传入一个数组
print(max(1, 2, 3, 4, 5))
print(max([3, 4, 5]))
# 数值转换函数 常见的数据类型转换
print(int('132'))  # 返回132
print(str(123))  # 返回'123'

# 函数的定义
# 通过def关键字定义一个函数，可通过return关键字设置返回值
def my_abs(x):
    if x >= 0:
        return '输入值是正数'
    else:
        return '输入值是负数'
print(my_abs(12))  # 返回'输入值是正数' 若不设置return关键字，则只执行方法，返回值为none
# 若是想定义什么也不做的函数 则使用pass语句。pass语句也可以在流程语句中使用
def nothing():
    pass
# 返回多个值 实际上返回值还是只有一个，以tuple的形式按顺序输出
def test(x):
    return x+1, x-1
a, b = test(1)
print(a)  # 返回2
print(b)  # 返回0

# 递归函数 指在一个函数内调用自身，那这个函数称为递归函数
# 例如!n=1*2*3*4*...*n-1*n 实际f(n)=!(n-1)*n,只有当n=1时属于特殊情况，n等于任意数时!n的值都等于!(n-1)*n
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


print(fact(3))  # 返回6
# 所有的递归函数都可以写成循环的形式，但循环的逻辑不如递归清晰。
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
# 实例 汉诺塔 参数n表示3个柱子中，第一根柱子上的盘子量，然后打印出所有由A借助B移动到C的方法
def move(n, a, b, c):
    if n == 1:
        print(a, '---->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)
move(4, 'A', 'B', 'C')

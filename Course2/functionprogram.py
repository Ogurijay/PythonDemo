# 函数式编程

# 高阶函数 已知变量是可以指向函数的，所以当函数可以接受另一个函数作为变量时，这个函数称为高阶函数
def add(x, y, f):
    return print(f(x)+f(y))
add(5, -10, abs)  # 返回结果为15
# map 该函数接收两个参数，一个是函数，另一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
def cal(x):
    return x*x
r = list(map(cal, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(r)  # 返回[1, 4, 9, 16, 25, 36, 49, 64, 81]
# reduce reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def cal1(x, y):
    return x+y
r = reduce(cal1, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)  # 返回45
# fliter fliter函数把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def noodd(x):
    return x % 2 == 0
r = list(filter(noodd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(r)  # 返回[2, 4, 6, 8]，这个函数实现了过滤奇数
# 利用filter实现计算素数的埃氏筛法
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)
        yield n # 把每个输出的数字都加入过滤器的条件，每次循环到next时判断是否为以输出的数的倍数
        it = filter(_not_divisible(n), it)
for n in primes():  # 打印出100以内的质数
    if n < 100:
        print(n)
    else:
        break
# 示例 利用filter实现输出10000以内的回数
def is_palindrome(n):
    s = str(n)
    r = s[::-1]
    return s == r
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
#sorted 排序算法
#对int型数组排序
L=[5,31,1,-26,13,-6,10]
print(sorted(L)) # 返回[-26, -6, 1, 5, 10, 13, 31]
# 也可以传入一个key，按照一定的规则排序
print(sorted(L,key=abs)) #返回[1, 5, -6, 10, 13, -26, 31] 类似于过滤器的原理，将iteration的每个元素都进行abs处理
# 处理字符串排序
D = ['bob', 'about', 'Zoo', 'Credit'] # 对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
print(sorted(D))

# 返回函数 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回
# 当不需要马上返回函数结果时，可以将函数作为结果返回，再次调用时才进行计算
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f=lazy_sum(1,2,3,4,5)
print(f())
# 闭包 
# 在刚才的例子中，我们在函数lazy_sum中又定义了函数sum，并且内部函数sum可以引用外部函数的参数和变量。当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种情况称为闭包(Closure)
# 且当我们每次调用这个函数，即使传入的参数相同，都是返回一个新的函数，且不相等
f1=lazy_sum(1,2,3,4,5)
f2=lazy_sum(1,2,3,4,5)
print(f1==f2) # 返回False
# 需要注意的是，返回的函数并不是立刻执行的，而是直到调用了f之后才会执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print('f1:',f1(),'f2:',f2(),'f3:',f3()) # f1,f2,f3的返回值都为9
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9
# 所以，如果必须要引用循环变量，方法是再次创建一个函数，用该函数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变
def newcount():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = newcount()
print('f1:',f1(),'f2:',f2(),'f3:',f3()) # 此时f1,f2,f3的返回值分别为1,4,9
# 示例 利用闭包创建一个递增计数器
def createCounter():
    base=[0]
    def counter():
        base[0]+=1
        return base[0]
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
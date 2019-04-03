# 生成器(generator) 由于受到内存限制，列表容量是有限的。若创建一个100万个元素的列表，如果我们仅需前几个元素，那后面的元素都浪费了。
# 而我们可以在循环的过程中不断的推算后续元素，而达到不用一次性一个很大的列表，这个机制称为生成器
# 假设我们要创建包含所有从1-20个数字平方根的列表
g = (x*x for x in range(20))  # 通过循环去访问列表的每个值
for n in g:
    print(n)  # 也可以通过next()函数来访问，但这样相对繁琐，且你并不知道哪个元素是最后一个元素，容易溢出
# 实现斐波拉契数列 除了前两个元素，后面的每个元素都可以通过前两个元素相加得到
# 假设要得到一个长度为20的斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 在函数中定义yield，则视为是一个generator
        a, b = b, a + b
        n += 1
    return '完成'
fib(20)
# 此时会发现，最后的完成字符并没有输出。因为当函数中包含yield关键字时，每次在next()时执行，遇到yield则语句返回，再次执行时会从上次的yield处继续执行
# 如果一定要拿到geneator的返回值，则需要捕获StopIteration错误，返回值包含在StopIteration的value中
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('生成器返回值:', e.value)
        break

# 示例 实现一个杨辉三角
def triangles():
    z = [1]
    while 1:
        yield z
        x = [z[i] + z[i+1] for i in range(len(z)-1)]# 返回每个长度前两个元素相加的值，个数等于len(z)-1
        z = [1] + x + [1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break

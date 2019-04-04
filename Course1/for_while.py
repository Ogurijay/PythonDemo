# for while循环

# for...in循环 需要一个集合作为目标
# 字符串遍历示例
names = ['kourtney', 'kim', 'Khloe', 'kendall', 'kylie']
for name in names:
    print(name)  # 遍历集合内的每个元素并打印
# 整型遍历示例
sum = 0
key = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in key:
    sum += num  # 返回结果应为0-9的和
print(sum)  # 通过遍历达到计算集合内元素总和的示例
# 也可以这么写
sum = 0
for num in range(10):  # python提供了一个range函数 可以代表0-(n-1)个整数的集合
    sum += num  # 返回结果应为0-9的和
print(sum)

# while循环 只要条件满足，则循环不中断，直到条件不满足为止
sum = 0
n = 9
while n > 0:
    sum += n
    n = n-1
print(sum)  # 返回结果应为0-9的和

# break和continue
# 在循环中可以通过break打断当前循环，也可使用continue直接跳跃到下一次循环进行操作
sum = 0
for num in range(101):
    if num == 50:  # 当循环到50时，跳出循环
        break
    if num % 2 == 0:  # 当前数值为偶数时，直接进行下一次循环
        continue
    sum += num
print(sum)  # 返回结果应为0-49中奇数的总和

# 列表生成式 即List Comprehensions，例如要生成[1,2,3]可写成list(range(1,4))
print(list(range(1, 4)))
# 复杂列表的情况 假设要输出[1*1,2*2,3*3]
print([x*x for x in range(1, 4)])  # 写列表生成式时，把要生成的元素x*x放在最前面，后面加上for循环
# 也可以加上if条件判断，假设仅要输出偶数的平方
print([x*x for x in range(1, 4) if x % 2 == 0])
# 运用两层循环，达到全排列的效果
print([x+y for x in 'ABC' for y in 'XYZ']) # 返回['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
# 配合函数，可以把一个列表中的字符串全部转换为大写
print([name.upper() for name in names]) # 返回['KOURTNEY', 'KIM', 'KHLOE', 'KENDALL', 'KYLIE']
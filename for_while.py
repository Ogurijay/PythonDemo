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

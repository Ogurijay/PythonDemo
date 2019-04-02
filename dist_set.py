# 字典dist和集合set

# dist使用键值对存储,具有极快的查询速度，但比较消耗内存。dist的key是不可变的，若将变量设置为key则会报错。
# dist的排列顺序与插入顺序无关
name = {'kourtney': 40, 'kim': 39, 'Khloe': 35, 'kendall': 24, 'kylie': 22}
print(name['kylie'])  # 对比于list dist就像字典 通过索引直接查找效率更高，而list的元素越多，查找越慢
# dist的值也可以通过赋值改变,且多次对同一个key赋值，只会存在最后一次赋值的数据
name['kylie'] = 20
name['kylie'] = 19
name['kylie'] = 23
print(name['kylie'])  # 返回23
# 当key不存在时 则会报错(建议在异常捕获里操作),所以可以通过in来判断key是否存在于dist内
'kylie' in name  # 返回True
# 也可以通过dist的get()方法获取对应key的value值。当key不存在时，返回值是-1
name.get('kylie')  # 返回20
name.get('bob')  # 返回-1
# 通过pop()方法删除字典值
name.pop('kourtney')
print(name)

# set 类似于dist，但只是一组key的集合，不包含value。在set中的key不可重复，set会自动过滤重复可以值。
# set很适合用来过滤list集合内的重复值
s = set([1, 2, 3, 3])
print(s)  # 返回{1,2,3}
# 通过add(key)方法来为set新增元素
s.add(4)
print(s)  # 返回{1,2,3,4}
# 通过remove(key)方法删除元素
s.remove(3)
print(s)  # 返回{1,2,4}
# set可以看成数学意义上的无序和无重复元素的集合，因此两个set可以做数学意义上的交集、并集等操作
s1 = set([1,2,3])
s2 = set([3,4,5])
print(s1 | s2)#返回并集
print(s1 & s2)#返回交集
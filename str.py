# 字符串
text = '123'  # 常规字符串声明方式
text1 = '这是\'123\''  # 在python中\可表示转义字符
text2 = r'\\123\\'  # 用r关键字可表示''内的字符串默认不转义
text3 = '''line1
... line2
... line3'''  # 可通过'''...'''的形式声明多行内容 可替代\n换行符
# 还有\n代表换行等特殊处理方式 此处不一一列举
print(text)
print(text1)
print(text2)
print(text3)

# 字符串在计算机中还有一个很头疼的问题 就是编码问题
# 通常用的是ASCII Unicode Utf-8
# ASCII中不包含中文 只能表示符号或字母
# Unicode集合所有语言，任意字符都可以用不同长度的数字都能表示
# Utf-8则是可变长编码 在Unicode的基础上更加节约空间
# 对于单个字符，python中可通过ord()函数获取字符相对应的整数表示
print(ord('中'))  # 输出20013
# chr()函数则相反，可把整数表示为对应字符
print(chr(20013))
# 若是知道整数编码 也可直接输出Unicode得到对应字符串
print('\u4e2d\u6587')  # 输出中文

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
# 在字符前以b'字符串'表示bytes
print(b'abc')
print(b'\xe4\xb8\xad\xe6\x96\x87')
# 以Unicode表示的字符串也可以通过encode()方法编码为制定的bytes
print('A'.encode('ascii'))
print('中文'.encode('utf-8'))
# 当在网络中读取了字节流想要转化为对应字符的时候 就要用decode()方法
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode())
# 如果当bytes中有一小部分无法解码的字节，则会报错 可以通过传入error='ignore'忽略
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))

# 可用len()函数计算出字符串的长度(单位字符)
print(len('中文长度'))
# 当数值类型为bytes时，则计算出字节长度
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))
# 由于Python源代码也是一个文本文件，所以当你的源码中包含中文的时候，保存时就需要指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# python中的格式化方式与C语言中一致，用%实现。也可以用format函数
print('这是字符串占位，%s' % '这里是字符串')
print('这是整型占位，%d' % 123)
print('这是浮点型占位，%f' % 12.3)
print('这是十六进制整数类型占位，%x' % 16)
# 浮点型和整型都可以指定是否补足0以及小数的位数
print('这是整型前补0，%03d' % 1)
print('这是浮点型保留1位小数，%.1f' % 123.351)  # 会自动四舍五入
# 当不一定确定用什么类型时，%s永远起作用，可把任何数据类型转换为字符串
print('年龄: %s，分数: %s' % (25, True))
# 当字符中本身就含有%，此时需要转义 以%%表示%
print('输出百分比: %d%%' % 7)

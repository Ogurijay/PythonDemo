# 条件语句

# ifelse
x = 1
if x > 0:
    print('if输出')
else:
    print('else输出')

if x < 0:
    print('if输出')
else:
    print('else输出')

if x < 0:
    print('if输出')
elif x == 1:
    print('elif输出')
else:
    print('else输出')

# 实例演示
# 请根据BMI公式（体重除以身高的平方）计算BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
w = input('请输入体重(kg)：')
h = input('请输入身高(cm)：')
#此处用到了异常捕获，请查看try_except.py教程
try:
    w = float(w)
    h = float(h)/100
except:
    print('请输入正确的数字格式！')
bmi = w/h/h
if bmi < 18.5:
    print('您的BMI指数是%f' % bmi+',参考指标：过轻')
elif bmi <= 25:
    print('您的BMI指数是%f' % bmi+',参考指标：正常')
elif bmi <= 28:
    print('您的BMI指数是%f' % bmi+',参考指标：过重')
elif bmi <= 32:
    print('您的BMI指数是%f' % bmi+',参考指标：肥胖')
else:
    print('您的BMI指数是%f' % bmi+',严重肥胖')

import re

# 查找数字
# compile 将表示正则的字符串编译为一个pattern对象

p = re.compile(r'\d')

# 在字符串里面查找
m = re.match(r'1','aaa111bbb222ccc333ddd444')

print(m)





p = re.compile(r'\d+')

# 在字符串里面查找，查找起始位置，终止位置
m = p.match('123456789',2,26)

print(m)

# match值
print(m[0])

# 开始、结束 位置
print(m.start(0))
print(m.end(0))



print('——————————————————')

# I 表示忽略大小写
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = p.match('I am is LiuChang')
print(m)

print(m.group(0))
print(m.group(2))
print(m.groups())


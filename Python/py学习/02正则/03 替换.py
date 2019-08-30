import re

# —————————替换—————————

def add(a):
    num1 = a.group()
    num2 = int(num1) + 1
    return str(num2)


p = re.compile(r'(\w+) (\w+)')
s = 'I 456 love manman,7788 hehe'
r = p.sub(r'替换替换', s)
print(r)

p = re.sub(r'\d+', add, 'abcd1')
print(p)




print('—————————查找中文—————————')
# 查找中文
t = u'大家好，我叫刘畅，hello everybody'
p = re.compile(r'[\u4e00-\u9fa5]+')
r = p.findall(t)
print(r)




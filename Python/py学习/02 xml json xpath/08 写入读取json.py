import json


data = {"name":"hahah", "age":12}


# 写入
with open("t.json", 'w') as f:
    json.dump(data, f)


# 读取
with open("t.json", 'r') as f:
    d = json.load(f)
    print(d)


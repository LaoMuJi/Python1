import requests
baseurl = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'girl'
}

headers = {
    'Content-Length':str(len(data))
}

# 加入代理
proxy = {'http': 'XXXXXXX',
         'https': 'XXXXXXX'}

# 代理验证 格式为  用户名：密码@代理地址：端口
proxy = {'http': 'china:123456@192.168.1.1:8888'}

# web客户端验证，网页需要登录，用户名密码
auth = ('test', '123456')



##  加入代理 proxies=proxy  加入授权信息 auth=auth
rsp = requests.request('post', baseurl, data=data,  headers=headers)

print(rsp.text)
print(rsp.json())

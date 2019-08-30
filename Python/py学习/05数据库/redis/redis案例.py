import redis



if __name__ == '__main__':

    sr = redis.StrictRedis(host='10.0.0.10',port=6379, db=0)
    # sr = redis.StrictRedis() # 默认127.0.0.1

    # 创建修改
    res = sr.set('k','dhjashd111111')
    print(res)

    # 获取
    res = sr.get('k')
    print(res)

    # 删除
    res = sr.delete('k')
    print(res) # 返回的数字代表成功几个

    # 获取全部键
    res = sr.keys()
    print(res)
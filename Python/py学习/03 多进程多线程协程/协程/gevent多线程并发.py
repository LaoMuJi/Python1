import gevent
from gevent import monkey # 必须！
import time



# 此代码检查需要等待替换
monkey.patch_all()

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i) # 打印内存地址
        time.sleep(1)
        # gevent.sleep(1)



# 开始线程并等待结束
gevent.joinall([
    gevent.spawn(f ,5),
    gevent.spawn(f ,5),
    gevent.spawn(f ,5)
])
import threading
import time

a,b = 0,5

lock1 = threading.Lock()
lock2 = threading.Lock()


# 参数定义3个线程同时使用资源
semaphore = threading.Semaphore(3)


def jia():
    global a,b

    if semaphore.acquire():
        for i in range(1,b):
            print("上锁1")

            # 上锁
            lock1.acquire()
            a+=1
            print("开锁1")
            time.sleep(0.5)

            # 去锁
            lock1.release()

def jib():
    global a,b
    for i in range(1,b):
        print("上锁2")
        lock2.acquire()

        # 锁等待时间
        rst = lock1.acquire(timeout=2)
        if rst:
            print("超时开锁1")
            lock1.release()
        a-=1
        print("开锁1")
        lock2.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=jia,args=())
    t2 = threading.Thread(target=jib,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()



# 可以被一个线程多次申请，主要解决递归调用的时候，需要重复申请锁的情况
mutex = threading.RLock()
# 上锁
mutex.acquire()
# 开锁1
mutex.release()

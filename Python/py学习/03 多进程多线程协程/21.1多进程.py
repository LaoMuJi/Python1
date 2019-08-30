import multiprocessing
import time


def b(aa):
    while True:
        print(time.ctime())
        time.sleep(aa)



if __name__ == '__main__':
    p = multiprocessing.Process(target=b, args=(1,))
    p.start()

    while True:
        time.sleep(2)
        print('.....')
import multiprocessing
import time



class Y1(multiprocessing.Process):

    def __init__(self,aa):
        super().__init__()
        self.aa = aa

    def run(self):  # run才能执行。要指定target=  未知
        while True:
            print(time.ctime())
            time.sleep(self.aa)


if __name__ == '__main__':
    p = Y1(1)
    p.start()
    while True:
        time.sleep(2)
        print('.....')

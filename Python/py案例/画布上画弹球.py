import random
import tkinter

class RandomBall:
    '''
    定义球的类
    '''

    def __init__(self, canvas, scrnwidth, scrnheight):
        '''
        csnvas:画布
        '''
        self.canvas = canvas
        #随机球的颜色，
        # 球初始随机
        # xpos是x坐标，Y坐标
        self.xpos = random.randint(10, 1000)
        self.ypos = random.randint(10, 1000)

        # 定义球的速度，模拟运动 X Y
        self.xvelocity = random.randint(4,20)
        self.yvelocity = random.randint(4,20)

        #定义屏幕大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight

        #随机球的大小，半径
        self.radius = random.randint(20, 150)
        c = lambda :random.randint(0,255)
        self.color = '#%02x%02x%02x' % (c(),c(),c())

    def create_ball(self):
        '''
        用构造函数定义的变量值，在canvas上画一个球
        '''
        #求圆坐标，点1
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        #点2
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius

        #有两个对角坐标画圆
        self.item = self.canvas.create_oval(x1,y1,x2,y2,fill=self.color, outline=self.color)

    def move_ball(self):
        #控制图画移动方向
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity

        #判断撞墙，上下左右
        if self.xpos + self.radius >= self.scrnwidth:
            self.xvelocity = -self.xvelocity
        if self.xpos + self.radius <= 0:
            self.xvelocity *= -1
        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = -self.yvelocity
        if self.ypos + self.radius <= 0:
            self.yvelocity = -self.yvelocity

        #在画布上挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver:

    balls = []

    def __init__(self):
        #每次随机球的数量
        self.num_balls = random.randint(6, 20)
        self.root = tkinter.Tk()
        #取消边框
        self.root.overrideredirect(1)
        #移动鼠标停止
        self.root.bind('<Motion>', self.myquit)
        #按键停止
        self.root.bind('<Key>', self.myquit)
        #获取屏幕大小
        w,h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        # w,h = 800,600

        #创建画布，包括画布的归属，规格
        self.canvas = tkinter.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        #在屏幕上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnwidth=w, scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()


    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        #after是50毫秒后启动函数
        self.canvas.after(50, self.run_screen_saver)

    def myquit(self, e):
        #
        self.root.destroy()



if __name__ == '__main__':
    #启动
    ScreenSaver()


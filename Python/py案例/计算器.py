from tkinter import *

root = Tk()

#定义面板的大小
root.geometry('250x380')

root.title('杀熊')

#定义面板 bg是背景色
frame_show = Frame(width=300,height=150,bg='#dddddd')

frame_show.pack()

#定义顶部区域
sv = StringVar()
sv.set('0')

# anchor:定义控件的锚点，e代表右边，font代表字体
show_label = Label(frame_show, textvariable=sv, bg = 'green', width=12, height=1,\
                   font=('黑体',20,'bold'), justify=LEFT, anchor='e')
show_label.pack(padx=10, pady=10)


num1 = 0
num2 = 0
operator = None


def delete():
    print('del')

#按键区域
frame_bord = Frame(width=400, height=350, bg="#cccccc")
b_del = Button(frame_bord, text='←', width=5, height=1,\
               command=delete)
b_del.grid(row=0,column=0)


def change(num):

    global num1,num2

    if operator:
        num2 = num2 + int(num)
        # 如果是第二个操作数 ，则应该显示完整的计算式子
        sv.set(num1+operator+num2)
    else:
        num1 = num1 + int(num)
        # 如果是第一个操作数，则只显示第一个操作数
        sv.set(num1)


def operation(op):
    if op in ['+','-','*','/']:
        operator = op
    else:
        if op == '+':
            rst = int(num1)+ int(num2)
        sv.set(str(rst))

b_1 = Button(frame_bord, text='1', width=5, height=2, \
             command=lambda: change("1"))
b_1.grid(row=1, column=0)



b_jia = Button(frame_bord, text='+',width=5, height=2,\
               command=lambda:operation("+"))
b_jia.grid(row=2, column=0)

frame_bord.pack(padx=10,pady=10)

root.mainloop()


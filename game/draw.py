#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import threading
from Tkinter import *           # 导入 Tkinter 库
root = Tk()                     # 创建窗口对象的背景色
                               
#创建画布
cvs = Canvas(root, bg="#ffffff")

# 画吊人的架子
cvs.create_line(50, 200, 250, 200, width=5)
cvs.create_line(150, 200, 150, 50, width=3)
cvs.create_line(150, 50, 100, 50, width=3)
cvs.create_line(100, 50, 100, 100, width=3)
# 画头
def head():
    cvs.create_oval(90, 100, 110, 120, width=3)
# 画身体
def body():
    cvs.create_line(100, 120, 100, 150, width=3)
#画手
def hand():
    cvs.create_line(100, 120, 80, 140, width=3)
    cvs.create_line(100, 120, 120, 140, width=3)
#画腿
def leg():
    cvs.create_line(100, 150, 80, 200, width=3)
    cvs.create_line(100, 150, 120, 200, width=3)
#开始画小人
def draw():
    timer = threading.Timer(0.5, head)
    timer0 = threading.Timer(1, body)
    timer1 = threading.Timer(1.5, hand)
    timer2 = threading.Timer(2, leg)
    timer.start()
    timer0.start()
    timer1.start()
    timer2.start()
#再玩一次
def again():
    cvs.create_rectangle(75,99,125,197,outline='#ffffff',fill='#ffffff')
    draw()
# 创建按钮病添加事件
begin = Button(root, bg="#00FF66", text="开始游戏", command=draw)
again = Button(root, bg="#6633CC", text="再玩一次", command=again)
over = Button(root, bg="#FF0033", text="结束游戏", command=exit)

begin.pack()
again.pack()
over.pack()
cvs.pack(side=TOP, fill=X)

root.mainloop()                 # 进入消息循环
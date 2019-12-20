# Python Tkinter Scale和LabeledScale用法 http://c.biancheng.net/view/2509.html
# python tkinter可以使用的颜色 - wjcaiyf的专栏 - CSDN博客 https://blog.csdn.net/wjciayf/article/details/79261005

import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')

import tkinter as tk
from tkinter import Frame
from robot import Armbot
import config

class GUI(Frame):
    
    def __init__(self, master, **kw):
        Frame.__init__(self, master, **kw)
        frame = Frame(master, 
                      height=692+30, 
                      width=803+20, 
                      bg="orange")
        frame.place(x=(720-692-10)/2, y=(840-803-10)/2)
        
        # 串口设置相关变量
        self.armbot = Armbot()

        # 创建画布，放置机械臂背景图
        self.ca = tk.Canvas(frame, 
                            background='white',
                            width=803,
                            height=692)
        self.bm = tk.PhotoImage(file="hand-control/images/bg_hand.gif")
        self.ca.place(x=(720-692-10)/2, y=(840-803-10)/2, width=803, height=692)
        self.ca.create_image(803/2 + 1, 692/2 + 1, image=self.bm)

        # 创建滑动条，舵机1
        self.servo1_v = tk.StringVar() #config.INIT_POS[1]
        self.sc1 = tk.Scale(frame, 
                            label='little finger',            # 设置标签内容
                            from_=500,                        # 设置最大值
                            to=2000,                          # 设置最小值
                            orient=tk.HORIZONTAL,             # 设置水平方向
                            length=200,                       # 设置轨道的长度
                            width=10,                         # 设置轨道的宽度
                            showvalue=True,                   # 设置显示当前值
                            troughcolor='orange',             # 设置轨道的背景色
                            variable=self.servo1_v,           # 设置绑定变量
                            sliderlength=12,                  # 设置滑块的长度
                            sliderrelief=tk.FLAT,             # 设置滑块的立体样式
                            tickinterval=500,                 # 设置指示刻度细分
                            resolution=1,                     # 设置步长
                            bg='lemonchiffon',                # 设置背景颜色
                            command=self.servo1_to_pos)       # 设置绑定事件处理，函数或方法
        self.sc1.place(x=30, y=310)
        # self.sc1.pack()
        self.sc1.set(1200)

        # 创建滑动条，舵机2
        self.servo2_v = tk.StringVar()#config.INIT_POS[2]
        self.sc2 = tk.Scale(frame, 
                            label='ring finger',              # 设置标签内容
                            from_=500,                        # 设置最大值
                            to=2000,                          # 设置最小值
                            orient=tk.HORIZONTAL,             # 设置水平方向
                            length=200,                       # 设置轨道的长度
                            width=10,                         # 设置轨道的宽度
                            showvalue=True,                   # 设置显示当前值
                            troughcolor='orange',             # 设置轨道的背景色
                            variable=self.servo2_v,           # 设置绑定变量
                            sliderlength=12,                  # 设置滑块的长度
                            sliderrelief=tk.FLAT,             # 设置滑块的立体样式
                            tickinterval=500,                 # 设置指示刻度细分
                            resolution=1,                     # 设置步长
                            bg='lemonchiffon',                # 设置背景颜色
                            command=self.servo2_to_pos)       # 设置绑定事件处理，函数或方法
        self.sc2.place(x=60, y=150)
        # self.sc2.pack()
        self.sc2.set(1200)
        
        # https://blog.csdn.net/tianmuha/article/details/80958802
        # 创建滑动条，舵机3
        self.servo3_v = tk.StringVar()#config.INIT_POS[3]
        self.sc3 = tk.Scale(frame, 
                            label='middle finger',            # 设置标签内容
                            from_=500,                        # 设置最大值
                            to=2000,                          # 设置最小值
                            orient=tk.HORIZONTAL,             # 设置水平方向
                            length=200,                       # 设置轨道的长度
                            width=10,                         # 设置轨道的宽度
                            showvalue=True,                   # 设置显示当前值
                            troughcolor='orange',             # 设置轨道的背景色
                            variable=self.servo3_v,           # 设置绑定变量
                            sliderlength=12,                  # 设置滑块的长度
                            sliderrelief=tk.FLAT,             # 设置滑块的立体样式
                            tickinterval=900/3,               # 设置指示刻度细分
                            resolution=1,                     # 设置步长
                            bg='lemonchiffon',                # 设置背景颜色
                            command=self.servo3_to_pos)       # 设置绑定事件处理，函数或方法
        self.sc3.place(x=320, y=20)
        # self.sc3.pack()
        self.sc3.set(1500)

        # 创建滑动条，舵机4
        self.servo4_v = tk.StringVar()#config.INIT_POS[3]
        self.sc4 = tk.Scale(frame, 
                            label='index finger',             # 设置标签内容
                            from_=500,                        # 设置最大值
                            to=2000,                          # 设置最小值
                            orient=tk.HORIZONTAL,             # 设置水平方向
                            length=200,                       # 设置轨道的长度
                            width=10,                         # 设置轨道的宽度
                            showvalue=True,                   # 设置显示当前值
                            troughcolor='orange',             # 设置轨道的背景色
                            variable=self.servo4_v,           # 设置绑定变量
                            sliderlength=12,                  # 设置滑块的长度
                            sliderrelief=tk.FLAT,             # 设置滑块的立体样式
                            tickinterval=900/3,               # 设置指示刻度细分
                            resolution=1,                     # 设置步长
                            bg='lemonchiffon',                # 设置背景颜色
                            command=self.servo4_to_pos)       # 设置绑定事件处理，函数或方法
        self.sc4.place(x=500, y=200)
        # self.sc4.pack()
        self.sc4.set(1500)

        # 创建滑动条，舵机5
        self.servo5_v = tk.StringVar()#config.INIT_POS[3]
        self.sc5 = tk.Scale(frame, 
                            label='thumb',                    # 设置标签内容
                            from_=500,                        # 设置最大值
                            to=2000,                          # 设置最小值
                            orient=tk.HORIZONTAL,             # 设置水平方向
                            length=200,                       # 设置轨道的长度
                            width=10,                         # 设置轨道的宽度
                            showvalue=True,                   # 设置显示当前值
                            troughcolor='orange',             # 设置轨道的背景色
                            variable=self.servo5_v,           # 设置绑定变量
                            sliderlength=12,                  # 设置滑块的长度
                            sliderrelief=tk.FLAT,             # 设置滑块的立体样式
                            tickinterval=900/3,               # 设置指示刻度细分
                            resolution=1,                     # 设置步长
                            bg='lemonchiffon',                # 设置背景颜色
                            command=self.servo5_to_pos)       # 设置绑定事件处理，函数或方法
        self.sc5.place(x=550, y=400)
        # self.sc5.pack()
        self.sc5.set(1500)

        # 创建滑动条，舵机6
        self.servo6_v = tk.StringVar()
        self.sc6 = tk.Scale(frame, 
                            label='wrist',                    # 设置标签内容
                            from_=500,                        # 设置最大值
                            to=2000,                          # 设置最小值
                            orient=tk.HORIZONTAL,             # 设置水平方向
                            length=200,                       # 设置轨道的长度
                            width=10,                         # 设置轨道的宽度
                            showvalue=True,                   # 设置显示当前值
                            troughcolor='orange',             # 设置轨道的背景色
                            variable=self.servo6_v,           # 设置绑定变量
                            sliderlength=12,                  # 设置滑块的长度
                            sliderrelief=tk.FLAT,             # 设置滑块的立体样式
                            tickinterval=300,                 # 设置指示刻度细分
                            resolution=1,                     # 设置步长
                            bg='lemonchiffon',                # 设置背景颜色
                            command=self.servo6_to_pos)       # 设置绑定事件处理，函数或方法
        self.sc6.place(x=300, y=600)
        self.sc6.set(1200)

        # # 创建单选钮，气泵
        # self.var = tk.StringVar()
        # self.var.set('Stop')
        # self.label = tk.Label(frame, text="AIR PUMP: "+self.var.get(), bg='palegreen', font=('Arial', 10), width=25, height=2)
        # self.label2 = tk.Label(frame, text=" ", bg='palegreen', font=('Arial', 10), width=25, height=2)
        # self.label.place(x=550, y=545)
        # self.label2.place(x=550, y=545+35)
        
        # self.r1 = tk.Radiobutton(frame, text='Suck', variable=self.var, value='Suck', bg='forestgreen', command=self.airpump)
        # self.r2 = tk.Radiobutton(frame, text='Blow', variable=self.var, value='Blow', bg='forestgreen', command=self.airpump)
        # self.r3 = tk.Radiobutton(frame, text='Stop', variable=self.var, value='Stop', bg='forestgreen', command=self.airpump)
        # self.r1.place(x=555, y=580)
        # self.r2.place(x=625, y=580)
        # self.r3.place(x=695, y=580)


        # 添加菜单
        menubar = tk.Menu(master)
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade (label='File', menu=filemenu)

        filemenu.add_separator ()
        filemenu.add_command (label='Exit', command=master.quit)
        master.config (menu=menubar)

    # def airpump(self):
    #     self.label.config(text="AIR PUMP: "+self.var.get())
    #     if self.var.get() == "Suck":
    #         # print("Suck")
    #         self.armbot.go_air_pump(signal=config.PUMP_SUCK)
    #     elif self.var.get() == "Blow":
    #         self.armbot.go_air_pump(signal=config.PUMP_BLOW)
    #     elif self.var.get() == "Stop":
    #         self.armbot.go_air_pump(signal=config.PUMP_STOP)

    def motion1(self):
        # print("hit")
        # five
        adict = {1:1200, 2:1050, 3:750, 4:1100, 5:1100}
        # adict = {1:600, 2:600, 3:600, 4:600, 5:600}
        self.armbot.servos_to_pos(adict)
        self.sc1.set(adict[1])
        self.sc2.set(adict[2])
        self.sc3.set(adict[3])
        self.sc4.set(adict[4])
        self.sc5.set(adict[5])

    def set_speed(self, v):
        print("speed set ", v)
        self.armbot.speed = v

    def servo1_to_pos(self, value1):
        print("servo1 to ", value1)
        self.servo1_v = value1
        print(type(self.servo1_v))
        # print("@@@@@@@@@", self.servo1_v)
        # print("@@@@@@@@@", self.servo2_v)
        # print("@@@@@@@@@", self.servo3_v)
        self.armbot.one_servo_to_pos(servo_id=1, servo_pos=int(value1))

    def servo2_to_pos(self, value2):
        self.servo2_v = value2
        print("servo2 to ", value2)
        self.armbot.one_servo_to_pos(servo_id=2, servo_pos=int(value2))

    def servo3_to_pos(self, value3):
        self.servo13_v = value3
        print("servo3 to ", value3)
        self.armbot.one_servo_to_pos(servo_id=3, servo_pos=int(value3))
    
    
    def servo4_to_pos(self, value4):
        self.servo14_v = value4
        print("servo4 to ", value4)
        self.armbot.one_servo_to_pos(servo_id=4, servo_pos=int(value4))

    def servo5_to_pos(self, value5):
        self.servo15_v = value5
        print("servo5 to ", value5)
        self.armbot.one_servo_to_pos(servo_id=5, servo_pos=int(value5))
    
    def servo6_to_pos(self, value6):
        self.servo16_v = value6
        print("servo6 to ", value6)
        self.armbot.one_servo_to_pos(servo_id=6, servo_pos=int(value6))




if __name__ == "__main__":
    root = tk.Tk()
    root.title(" Handling Robot Automatic Control System ")
    root.geometry("1600x760")
    app = GUI(root)
    # frame = tk.Frame(root, *)
    # Frame.pack()
    root.mainloop()




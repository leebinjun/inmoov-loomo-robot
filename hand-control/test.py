import tkinter as tk


windows = tk.Tk()
windows.title('hello')
windows.geometry('200x400')

var = tk.StringVar("")
var.set("lskadjhklgajfh")
lable = tk.Label(windows, textvariable=var, bg='green', font=('Arial', 15), width=15, height=2)
lable.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        var.set('u hit me')
        on_hit = True
    else:
        on_hit = False
        var.set('')

button = tk.Button(windows, text='hit me', command=hit_me, width=15, height=2)
button.pack()


def func(v1):
    print(f"servor {v1}")
# 创建滑动条，舵机3
v = 1000
sc = tk.Scale(windows, 
            label='servo3',                   # 设置标签内容
            from_=700,                        # 设置最大值
            to=1600,                          # 设置最小值
            orient=tk.HORIZONTAL,             # 设置水平方向
            length=200,                       # 设置轨道的长度
            width=10,                         # 设置轨道的宽度
            showvalue=True,                   # 设置显示当前值
            troughcolor='orangeRed',          # 设置轨道的背景色
            variable=v,           # 设置绑定变量
            sliderlength=12,                  # 设置滑块的长度
            sliderrelief=tk.FLAT,             # 设置滑块的立体样式
            tickinterval=900/3,               # 设置指示刻度细分
            resolution=1,                     # 设置步长
            bg='LavenderBlush',               # 设置背景颜色
            command=func)       # 设置绑定事件处理，函数或方法

sc.pack()
sc.set(v)
windows.mainloop()













import tkinter
from tkinter import *
from tkinter import ttk

class StartPage(object):
    def __init__(self):
        self.root=Tk()
        self.root.wm_title(' Option Price Calculator')
        Label(self.root, text='Please select the model and the Option type').pack()
        Label(self.root, text=',click "Continue"  to  parameters setting').pack()
        Label(self.root, text='by Yifu,Junjian and Junyi, MQF @RBS').pack()
        comvalue = StringVar()  # initialize the value
        self.comboxlist = ttk.Combobox(self.root, textvariable=comvalue)  # initialize
        self.comboxlist["values"] = ("Black Scholes Model", "Monte Carlo", "Binary tree", "Trigeminal tree")
        #self.comboxlist.grid(column=1, row=6)
        self.comboxlist.current(0)  # select the first one to show
        self.comboxlist.pack()
        comvalue2 = StringVar()
        self.comboxlist2 = ttk.Combobox(self.root, textvariable=comvalue2)  # initialize
        self.comboxlist2["values"] = ("Call Option","Put Option")
        #self.comboxlist2.grid(column=1, row=7)
        self.comboxlist2.current(0)  # select the first one to show
        self.comboxlist2.pack()
        Button(self.root, text="Parameters Setting", command=self.go_calculator).pack()
        self.root.mainloop()
    def go_calculator(self):
        modelType=self.comboxlist.get()
        optionType=self.comboxlist2.get()
        print(modelType,optionType)
        self.root.destroy()
        CalculatorPage(modelType,optionType)

class CalculatorPage(object):
    def __init__(self,modelType,optionType):
        self.modelType=modelType
        self.optionType=optionType
        self.vlist=[]
        self.root = Tk() # Create an object
        self.root.wm_title(' Option Price Calculator')
        Label(self.root, text='Model type : '+self.modelType+'    Option type: '+self.optionType).grid(row=0, column=0, columnspan=3)
        Label(self.root, text='Please input relevant parameters, '
                         'then click "Calculate" button.').grid(row=1, column=0, columnspan=3)
        Label(self.root, text='by Yifu,Junyi and Junjian MQF @RBS').grid(columnspan=3)
        self.cp = self.optionType
        Label(self.root, text='Input parameters').grid(row=4, column=0, sticky=W)
        # Radiobutton(self.root, text='Call', variable=self.cp, value='c').grid(row=2, column=1)
        # Radiobutton(self.root, text='Put', variable=self.cp, value='p').grid(row=2, column=2)
        if self.modelType=="Black Scholes Model":
            self.plist = ['Current Price', 'Strike Price', 'Days to Maturity',
                     'Risk-free Rate', 'Volatility', 'Continuous Dividend Rate']
            self.elist = [] # for parameters
            r = 5 # r start from 0 and now is 3
            for param in self.plist:
                Label(self.root, text=param).grid(column=0, sticky=W)
                e = Entry(self.root)
                e.grid(row=r, column=1, columnspan=2, sticky=W+E)
                self.elist.append(e)
                r += 1
            Button(self.root, text='Calculate',command = self.get_parameter_BS).grid(row=r)
            r += 1
            self.answ = Label(self.root, text='The result is as follows:')
            self.answ.grid(row=r, columnspan=3)
            r += 1
            self.bs = Label(self.root)
            #self.mc = Label(self.root)
            self.bs.grid(row=r, columnspan=2, sticky=E)
            #self.mc.grid(row=r+1, columnspan=2, sticky=E)
            Label(self.root, text='Use BS Model: ').grid(row=r, sticky=W)
            #Label(self.root, text='Use Monte Carlo: ').grid(row=r+1, sticky=W)
        elif self.modelType=="Monte Carlo":
            self.plist = ['Current Price', 'Strike Price', 'Days to Maturity',
                     'Risk-free Rate', 'Volatility', 'Continuous Dividend Rate','num_of_path']
            self.elist = [] # for parameters
            r = 5 # r start from 0 and now is 3
            for param in self.plist:
                Label(self.root, text=param).grid(column=0, sticky=W)
                e = Entry(self.root)
                e.grid(row=r, column=1, columnspan=2, sticky=W+E)
                self.elist.append(e)
                r += 1
            Button(self.root, text='Calculate',command = self.get_parameter_BS).grid(row=r)
            r += 1
            self.answ = Label(self.root, text='The result is as follows:')
            self.answ.grid(row=r, columnspan=3)
            r += 1
            self.MC = Label(self.root)
            #self.mc = Label(self.root)
            self.MC.grid(row=r, columnspan=2, sticky=E)
            #self.mc.grid(row=r+1, columnspan=2, sticky=E)
            Label(self.root, text='Use Monte Carlo: ').grid(row=r, sticky=W)
            #Label(self.root, text='Use Monte Carlo: ').grid(row=r+1, sticky=W)

    def get_parameter_BS(self):
        vlist = []
        for e in self.elist:
            try:
                p = float(e.get())
                vlist.append(p)
            except:
                answ.config(text='Invalid Input(s). Please input correct parameter(s)', fg='red')
                e.delete(0, len(e.get()))
                return 0
        optionPrice = vlist[0] + vlist[1] + vlist[2] + vlist[3] + vlist[4]
        print(optionPrice)
        self.answ.config(text='The result is as follows:', fg='black')
        self.bs.config(text=str("%.8f" % (optionPrice/10)))
        #self.mc.config(text=str("%.8f" % (optionPrice*10)))
    def get_parameter_MC(self):
        vlist = []
        for e in self.elist:
            try:
                p = float(e.get())
                vlist.append(p)
            except:
                answ.config(text='Invalid Input(s). Please input correct parameter(s)', fg='red')
                e.delete(0, len(e.get()))
                return 0
        optionPrice = vlist[0] + vlist[1] + vlist[2] + vlist[3] + vlist[4]
        print(optionPrice)
        self.answ.config(text='The result is as follows:', fg='black')
        self.bs.config(text=str("%.8f" % (optionPrice/10)))
        #self.mc.config(text=str("%.8f" % (optionPrice*10)))


if __name__ == '__main__':
    StartPage()


# class Window():
#     def __init__(self,root):
#         selt
#
#
#
#
#
# def main():
#     root=tkinter.TK()
#     root.title("Option Price Calculator")
#     window=Window(root)
#     root.minsize(600, 500)
#     root.maxsize(600, 500)
#     root.mainloop()


# root = tkinter.Tk() # Create an object
# root.wm_title('European Option Price Calculator')
# tkinter.Label(root, text='Please input relevant parameters, '
#                  'then click "Calculate" button.').grid(row=0, column=0, columnspan=3)
# tkinter.Label(root, text='by Junyi, MQF @RBS').grid(columnspan=3)
# cp = tkinter.StringVar()
# Label(root, text='Option Type').grid(row=2, column=0, sticky=W)
# Radiobutton(root, text='Call', variable=cp, value='c').grid(row=2, column=1)
# Radiobutton(root, text='Put', variable=cp, value='p').grid(row=2, column=2)
#
# plist = ['Current Price', 'Strike Price', 'Days to Maturity',
#          'Risk-free Rate', 'Volatility', 'Continuous Dividend Rate', 'MC Iteration']
# elist = []
# r = 3 # r start from 0 and now is 3
# for param in plist:
#     Label(root, text=param).grid(column=0, sticky=W)
#     e = Entry(root)
#     e.grid(row=r, column=1, columnspan=2, sticky=W+E)
#     elist.append(e)
#     r += 1
# Button(root, text='Calculate').grid(row=r)
# r += 1
#
# answ = Label(root, text='The result is as follows:')
# answ.grid(row=r, columnspan=3)
# r += 1
# bs = Label(root)
# mc = Label(root)
# bs.grid(row=r, columnspan=2, sticky=E)
# mc.grid(row=r+1, columnspan=2, sticky=E)
# Label(root, text='Use BS formula: ').grid(row=r, sticky=W)
# Label(root, text='Use Monte Carlo: ').grid(row=r+1, sticky=W)
# root.mainloop()

# def go(*args):  # 处理事件，*args表示可变参数
#     print(comboxlist.get())  # 打印选中的值
#
#
# win = tkinter.Tk()  # 构造窗体
# comvalue = tkinter.StringVar()  # 窗体自带的文本，新建一个值
# comboxlist = ttk.Combobox(win, textvariable=comvalue)  # 初始化
# comboxlist["values"] = ("1", "2", "3", "4")
# comboxlist.current(0)  # 选择第一个
# comboxlist.bind("<<ComboboxSelected>>", go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
# comboxlist.pack()
#
# win.mainloop()  # 进入消息循环

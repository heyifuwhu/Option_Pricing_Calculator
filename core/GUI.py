import tkinter
from tkinter import *
from tkinter import ttk
from core.Tree_Model_Base import tree_model
from core.Black_Schcoles_Models_concrete import *
from core.MonteCarlo import *
class StartPage(object):
    def __init__(self):
        self.root=Tk()
        self.root.wm_title(' Option Price Calculator')
        Label(self.root, text='Please select the model and the Option type').pack()
        Label(self.root, text=',click "Continue"  to  parameters setting').pack()
        Label(self.root, text='by Yifu,Junjian and Junyi, MQF @RBS').pack()
        comvalue = StringVar()  # initialize the value
        self.comboxlist = ttk.Combobox(self.root, textvariable=comvalue)  # initialize
        self.comboxlist["values"] = ("Black Scholes Model", "Monte Carlo", "Binomial tree", "Trinomial tree")
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
        self.root.resizable(0, 0)
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
            self.plist = ['Current Price', 'Strike Price', 'Time to Maturity',
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
            self.BS = Label(self.root)
            #self.mc = Label(self.root)
            self.BS.grid(row=r, columnspan=2, sticky=E)
            #self.mc.grid(row=r+1, columnspan=2, sticky=E)
            Label(self.root, text='European Option: ').grid(row=r, sticky=W)
            #Label(self.root, text='Use Monte Carlo: ').grid(row=r+1, sticky=W)
            Button(self.root, text='Go Back', command=self.go_startPage).grid(row=r + 1)
            self.root.resizable(0, 0)
            #Button(self.root, text='Go Back', command=self.go_startPage).pack()
        elif self.modelType=="Monte Carlo":
            self.plist = ['Current Price', 'Strike Price', 'Time to Maturity',
                     'Risk-free Rate', 'Volatility', 'Continuous Dividend Rate','num_of_path']
            self.elist = [] # for parameters
            r = 5 # r start from 0 and now is 3
            for param in self.plist:
                Label(self.root, text=param).grid(column=0, sticky=W)
                e = Entry(self.root)
                e.grid(row=r, column=1, columnspan=2, sticky=W+E)
                self.elist.append(e)
                r += 1
            Button(self.root, text='Calculate',command = self.get_parameter_MC).grid(row=r)
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
            Button(self.root, text='Go Back', command=self.go_startPage).grid(row=r+1)
            self.root.resizable(0, 0)
        elif self.modelType=="Binomial tree":
            self.plist = ['Current Price', 'Strike Price', 'Time to Maturity',
                     'Risk-free Rate', 'Volatility','Number_of_step']
            self.elist = [] # for parameters
            r = 5 # r start from 0 and now is 3
            for param in self.plist:
                Label(self.root, text=param).grid(column=0, sticky=W)
                e = Entry(self.root)
                e.grid(row=r, column=1, columnspan=2, sticky=W+E)
                self.elist.append(e)
                r += 1
            Button(self.root, text='Calculate',command = self.get_parameter_BT).grid(row=r)
            r += 1
            self.answ = Label(self.root, text='The result is as follows:')
            self.answ.grid(row=r, columnspan=3)
            r += 1
            self.EU = Label(self.root)
            self.AM = Label(self.root)
            #self.mc = Label(self.root)
            self.EU.grid(row=r, columnspan=2, sticky=E)
            self.AM.grid(row=r+1, columnspan=2, sticky=E)
            Label(self.root, text='European Option : ').grid(row=r, sticky=W)
            Label(self.root, text='American Option : ').grid(row=r+1, sticky=W)
            Button(self.root, text='Go Back', command=self.go_startPage).grid(row=r+2)
            self.root.resizable(0, 0)
        elif self.modelType=="Trinomial tree":
            self.plist = ['Current Price', 'Strike Price', 'Time to Maturity',
                     'Risk-free Rate', 'Volatility','Number_of_step']
            self.elist = [] # for parameters
            r = 5 # r start from 0 and now is 3
            for param in self.plist:
                Label(self.root, text=param).grid(column=0, sticky=W)
                e = Entry(self.root)
                e.grid(row=r, column=1, columnspan=2, sticky=W+E)
                self.elist.append(e)
                r += 1
            Button(self.root, text='Calculate',command = self.get_parameter_TT).grid(row=r)
            r += 1
            self.answ = Label(self.root, text='The result is as follows:')
            self.answ.grid(row=r, columnspan=3)
            r += 1
            self.EU = Label(self.root)
            self.AM = Label(self.root)
            #self.mc = Label(self.root)
            self.EU.grid(row=r, columnspan=2, sticky=E)
            self.AM.grid(row=r+1, columnspan=2, sticky=E)
            Label(self.root, text='European Option : ').grid(row=r, sticky=W)
            Label(self.root, text='American Option : ').grid(row=r+1, sticky=W)
            Button(self.root, text='Go Back', command=self.go_startPage).grid(row=r+2)
            self.root.resizable(0, 0)

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

        self.answ.config(text='The result is as follows:', fg='black')
        if self.optionType=="Call Option":
            option=European_Call_BS(vlist[0], vlist[1], vlist[2], vlist[3], vlist[4])
            self.BS.config(text=str("%.8f" % (option.get_Option_Price())))
        else:
            option = European_Put_BS(vlist[0], vlist[1], vlist[2], vlist[3], vlist[4])
            self.BS.config(text=str("%.8f" % (option.get_Option_Price())))
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
        self.answ.config(text='The result is as follows:', fg='black')
        if self.optionType=="Call Option":
            European_call = Pay_Off_Vanilla.European_Pay_Off("call", int(vlist[1]))
            optionPrice = MonteCarlo(European_call, vlist[0], vlist[2], vlist[3], vlist[4]).get_MonteCarlo_Price(int(vlist[6]))
            self.MC.config(text=str("%.8f" % (optionPrice)))

        else:
            European_put = Pay_Off_Vanilla.European_Pay_Off("put", int(vlist[1]))
            optionPrice = MonteCarlo(European_put, vlist[1], vlist[2], vlist[3], vlist[4]).get_MonteCarlo_Price(int(vlist[6]))
            self.MC.config(text=str("%.8f" % (optionPrice)))
    def get_parameter_BT(self):
        vlist = []
        for e in self.elist:
            try:
                p = float(e.get())
                vlist.append(p)
            except:
                answ.config(text='Invalid Input(s). Please input correct parameter(s)', fg='red')
                e.delete(0, len(e.get()))
                return 0
        option=tree_model(vlist[0],vlist[1],vlist[2],vlist[3],vlist[4])
        self.answ.config(text='The result is as follows:', fg='black')
        if self.optionType=="Call Option":
            self.EU.config(text=str("%.8f" % (option.European_Binomial_Multiplicative('call', int(vlist[5]), 1.1, 1 / 1.1))))
            self.AM.config(text=str("%.8f" % (option.American_Binomial_Multiplicative('call', int(vlist[5]), 1.1, 1 / 1.1))))
        else:
            self.EU.config(text=str("%.8f" % (option.European_Binomial_Multiplicative('put', int(vlist[5]), 1.1, 1 / 1.1))))
            self.AM.config(text=str("%.8f" % (option.American_Binomial_Multiplicative('put', int(vlist[5]), 1.1, 1 / 1.1))))
    def get_parameter_TT(self):
        vlist = []
        for e in self.elist:
            try:
                p = float(e.get())
                vlist.append(p)
            except:
                answ.config(text='Invalid Input(s). Please input correct parameter(s)', fg='red')
                e.delete(0, len(e.get()))
                return 0
        option=tree_model(vlist[0],vlist[1],vlist[2],vlist[3],vlist[4])
        self.answ.config(text='The result is as follows:', fg='black')
        if self.optionType=="Call Option":
            self.EU.config(text=str("%.8f" % (option.European_Trinomial('call', int(vlist[5]), 0.2))))
            self.AM.config(text=str("%.8f" % (option.American_Trinomial('call', int(vlist[5]), 0.2))))
        else:
            self.EU.config(text=str("%.8f" % (option.European_Trinomial('put', int(vlist[5]), 0.2))))
            self.AM.config(text=str("%.8f" % (option.American_Trinomial('put', int(vlist[5]), 0.2))))
    def go_startPage(self):
        self.root.destroy()
        StartPage()


if __name__ == '__main__':
    StartPage()


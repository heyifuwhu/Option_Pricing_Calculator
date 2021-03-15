import tkinter
from tkinter import *
from tkinter import ttk
from core.Tree_Model_Base import tree_model
from core.Black_Schcoles_Models_concrete import *
from core.MonteCarlo import *

# the first page
class StartPage(object):
    def __init__(self):
        self.root = Tk()
        self.root.wm_title('Option Price Calculator')
        Label(self.root, text='Please select the model and the option type').pack()
        Label(self.root, text=',click "Continue"  to  parameters setting').pack()
        Label(self.root, text='Implemented by Yifu Jason He from MQF @RBS').pack()

        # initialize the value for models
        model_comvalue = StringVar()
        self.comboxlist = ttk.Combobox(self.root, textvariable=model_comvalue)  # initialize
        self.comboxlist["values"] = ("Black Scholes Model", "Monte Carlo", "Binomial tree", "Trinomial tree")
        self.comboxlist.current(0)  # select the first one to show
        self.comboxlist.pack()  # put the widget in the window

        # initialize the value for option types
        type_comvalue = StringVar()
        self.comboxlist2 = ttk.Combobox(self.root, textvariable=type_comvalue)  # initialize
        self.comboxlist2["values"] = ("Call Option","Put Option")
        self.comboxlist2.current(0)  # select the first one to show
        self.comboxlist2.pack() # put the widget in the window

        # Set a button to continue
        Button(self.root, text="Continue", command=self.go_calculator).pack()

        self.root.resizable(height=False, width=False)
        self.root.mainloop()

    # go to the calculation
    def go_calculator(self):
        modelType = self.comboxlist.get()
        optionType = self.comboxlist2.get()
        print(modelType, optionType)
        self.root.destroy()
        CalculatorPage(modelType, optionType)


# the calculation page
class CalculatorPage(object):
    def __init__(self, modelType, optionType):
        self.modelType = modelType
        self.optionType = optionType
        self.vlist = []

        # Create an object
        self.root = Tk()
        self.root.wm_title('Option Price Calculator')
        Label(self.root, text=f'Model type: {self.modelType}').grid(row=0, column=0, columnspan=3)
        Label(self.root, text=f'Option type: {self.optionType}').grid(row=1, column=0, columnspan=3)
        Label(self.root, text='Implemented by Yifu Jason He from MQF @RBS').grid(columnspan=4)
        Label(self.root, text='Input parameters: ').grid(row=4, column=0, sticky=W)

        if self.modelType == "Black Scholes Model":
            self.plist = ['Spot Price', 'Strike Price', 'Time to Maturity',
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
            self.delta = Label(self.root)
            self.gamma = Label(self.root)
            self.theta = Label(self.root)
            self.rho = Label(self.root)
            self.vega = Label(self.root)

            self.BS.grid(row=r, columnspan=2, sticky=E)
            self.delta.grid(row=r + 1, columnspan=2, sticky=E)
            self.gamma.grid(row=r + 2, columnspan=2, sticky=E)
            self.theta.grid(row=r + 3, columnspan=2, sticky=E)
            self.rho.grid(row=r + 4, columnspan=2, sticky=E)
            self.vega.grid(row=r + 5, columnspan=2, sticky=E)

            Label(self.root, text=f'European {self.optionType}: ').grid(row=r, sticky=W)
            r += 1
            Label(self.root, text='delta: ').grid(row=r, sticky=W)
            r += 1
            Label(self.root, text='gamma: ').grid(row=r, sticky=W)
            r += 1
            Label(self.root, text='theta: ').grid(row=r, sticky=W)
            r += 1
            Label(self.root, text='rho: ').grid(row=r, sticky=W)
            r += 1
            Label(self.root, text='vega: ').grid(row=r, sticky=W)
            r += 1

            Button(self.root, text='Go Back', command=self.go_startPage).grid(row=r)
            self.root.resizable(height=False, width=False)

        elif self.modelType=="Monte Carlo":
            self.plist = ['Spot Price', 'Strike Price', 'Time to Maturity',
                          'Risk-free Rate', 'Volatility', 'Continuous Dividend Rate', 'num_of_path']
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
            self.MC.grid(row=r, columnspan=2, sticky=E)
            Label(self.root, text='Use Monte Carlo: ').grid(row=r, sticky=W)
            Button(self.root, text='Go Back', command=self.go_startPage).grid(row=r+1)
            self.root.resizable(height=False, width=False)
        elif self.modelType=="Binomial tree":
            self.plist = ['Spot Price', 'Strike Price', 'Time to Maturity',
                     'Risk-free Rate', 'Volatility','Continuous Dividend Rate','Number_of_step']
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
            self.EU.grid(row=r, columnspan=2, sticky=E)
            self.AM.grid(row=r+1, columnspan=2, sticky=E)
            Label(self.root, text=f'European {self.optionType} : ').grid(row=r, sticky=W)
            Label(self.root, text=f'American {self.optionType} : ').grid(row=r+1, sticky=W)
            Button(self.root, text='Go Back', command=self.go_startPage).grid(row=r+2)
            self.root.resizable(height=False, width=False)
        elif self.modelType=="Trinomial tree":
            self.plist = ['Spot Price', 'Strike Price', 'Time to Maturity',
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
            Label(self.root, text=f'European {self.optionType} : ').grid(row=r, sticky=W)
            Label(self.root, text=f'American {self.optionType} : ').grid(row=r+1, sticky=W)
            Button(self.root, text='Go Back', command=self.go_startPage).grid(row=r+2)
            self.root.resizable(height=False, width=False)

    def get_parameter_BS(self):
        vlist = []
        for e in self.elist:
            try:
                p = float(e.get())
                vlist.append(p)
            except:
                self.answ.config(text='Invalid Input(s). Please input correct parameter(s)', fg='red')
                e.delete(0, len(e.get()))
                return 0

        self.answ.config(text='The result is as follows:', fg='black')
        if self.optionType=="Call Option":
            option = European_Call_BS(vlist[0], vlist[1], vlist[2], vlist[3], vlist[4], vlist[5])
            self.BS.config(text=str("%.8f" % (option.get_Option_Price())))
            self.delta.config(text=str("%.8f" % (option.get_delta())))
            self.gamma.config(text=str("%.8f" % (option.get_gamma())))
            self.theta.config(text=str("%.8f" % (option.get_theta())))
            self.rho.config(text=str("%.8f" % (option.get_rho())))
            self.vega.config(text=str("%.8f" % (option.get_vega())))
        else:
            option = European_Put_BS(vlist[0], vlist[1], vlist[2], vlist[3], vlist[4], vlist[5])
            self.BS.config(text=str("%.8f" % (option.get_Option_Price())))
            self.delta.config(text=str("%.8f" % (option.get_delta())))
            self.gamma.config(text=str("%.8f" % (option.get_gamma())))
            self.theta.config(text=str("%.8f" % (option.get_theta())))
            self.rho.config(text=str("%.8f" % (option.get_rho())))
            self.vega.config(text=str("%.8f" % (option.get_vega())))


    def get_parameter_MC(self):
        vlist = []
        for e in self.elist:
            try:
                p = float(e.get())
                vlist.append(p)
            except:
                self.answ.config(text='Invalid Input(s). Please input correct parameter(s)', fg='red')
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
                self.answ.config(text='Invalid Input(s). Please input correct parameter(s)', fg='red')
                e.delete(0, len(e.get()))
                return 0
        option=tree_model(vlist[0],vlist[1],vlist[2],vlist[3],vlist[4],vlist[5])
        self.answ.config(text='The result is as follows:', fg='black')
        if self.optionType=="Call Option":
            self.EU.config(text=str("%.8f" % (option.European_Binomial_Multiplicative('call', int(vlist[6])))))
            self.AM.config(text=str("%.8f" % (option.American_Binomial_Multiplicative('call', int(vlist[6])))))
        else:
            self.EU.config(text=str("%.8f" % (option.European_Binomial_Multiplicative('put', int(vlist[6])))))
            self.AM.config(text=str("%.8f" % (option.American_Binomial_Multiplicative('put', int(vlist[6])))))
    def get_parameter_TT(self):
        vlist = []
        for e in self.elist:
            try:
                p = float(e.get())
                vlist.append(p)
            except:
                self.answ.config(text='Invalid Input(s). Please input correct parameter(s)', fg='red')
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


from core import Pay_Off_Vanilla
from core.Pay_Off_Base import PayOffBaseClass
import numpy as np


class MonteCarlo(object):
    def __init__(self, Payoff_Obj_: PayOffBaseClass, S_, T_, r_, sigma_, div_=0):
        self.Payoff = Payoff_Obj_
        self.S = S_
        self.T = T_
        self.r = r_
        self.sigma = sigma_
        self.div = div_

    def get_MonteCarlo_Price(self,num_of_path=1000):
        variance = self.sigma * self.sigma * self.T
        rootVariance = np.sqrt(variance)
        itoCorrection = -0.5*variance

        moveSpot = self.S * np.exp(self.r * self.T + itoCorrection)
        runningSum = 0
        for i in range(num_of_path):
            thisGaussian = np.random.normal(0,1)
            thisSpot = moveSpot*np.exp(rootVariance*thisGaussian)
            thisPayoff = self.Payoff.get_payoff(thisSpot)
            runningSum += thisPayoff
        mean_value = runningSum/num_of_path
        mean_value *= np.exp(-1 * self.r * self.T)
        return mean_value

if __name__ == "__main__":
    S = 100
    K = 100
    T = 1
    r = 0.06
    sigma = 0.2
    European_call = Pay_Off_Vanilla.European_Pay_Off("call",K)
    European_put = Pay_Off_Vanilla.European_Pay_Off("put", K)
    Call_MC = MonteCarlo(European_call, S, T, r, sigma)
    Put_MC = MonteCarlo(European_put, S, T, r, sigma)
    print("Call_MC: ", Call_MC.get_MonteCarlo_Price(100))
    print("Call_MC: ", Put_MC.get_MonteCarlo_Price(100))
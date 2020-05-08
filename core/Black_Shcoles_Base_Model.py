import abc
import numpy as np
from scipy.stats import norm

class BSBaseModel(object):
    """
    Summary of Black Scholes Model:
        This is a base class of Black Schole Model.
    Attributes:
        S: Spot Price
        K: Strike Price
        T : Time to Maturity
        r: risk-free rate(TBD)
        sigma : Volatility
        div : dividend rate
    """
    def __init__(self, S_, K_, T_, r_, sigma_, div_=0):
        self.S = S_
        self.K = K_
        self.T = T_
        self.r = r_
        self.sigma = sigma_
        self.div = div_

    @abc.abstractmethod
    def get_Option_Price(self):
        pass


    @abc.abstractmethod
    def get_delta(self):
        pass

    @abc.abstractmethod
    def get_gamma(self):
        pass

    @abc.abstractmethod
    def get_theta(self):
        pass

    @abc.abstractmethod
    def get_rho(self):
        pass

    @abc.abstractmethod
    def get_vega(self):
        pass

    @abc.abstractmethod
    def get_delta_numerical(self):
        pass

    def get_gamma_numerical(self):
        pass

    def get_theta_numerical(self):
        pass

    def get_rho_numerical(self):
        pass

    def get_vega_numerical(self):
        pass

    # mutators and accessors
    def set_S(self, S_):
        self.S = S_
    def set_K(self, K_):
        self.K = K_
    def set_T(self, T_):
        self.T = T_
    def set_r(self, r_):
        self.r = r_
    def set_sigma(self,  sigma_):
        self.sigma = sigma_
    def sef_div(self,div_):
        self.div = div_


# def BSM(Option_type, S, K, vol, T, r):
#     d1 = (log(S / K) + (r + 0.5 * vol ** 2) * T) / (vol * sqrt(T))
#     d2 = d1 - vol * sqrt(T)
#     if Option_type == "call":
#         Option = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
#         return Option
#     elif Option_type == "put":
#         Option = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
#         return Option
#     else:
#         return "Error: parameter Option_type only takes in 'call or 'put'"
#
# def BSM(Option_type,K,T,S,sigma,r,div=0):
#     d1 = (np.log(S/K) + (r - div + 0.5* sigma**2)*T) / (sigma * np.sqrt(T))
#     d2 = d1 - sigma * np.sqrt(T)
#     if Option_type == "call":
#         return S * np.exp(-div * T) * norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
#     elif Option_type == "put":
        return K*np.exp(-r*T)*norm.cdf(-d2) - S * np.exp(-div * T)*norm.cdf(-d1)
if __name__ == "__main__":

    K=100
    T=1
    S=100
    sigma = 0.2
    r=0.06
    print(f'call: {BSM("call",K,T,S,sigma,r)}')
    print(f'put: {BSM("put",K,T,S,sigma,r)}')
    BSM("call",K,T,S,sigma,r)
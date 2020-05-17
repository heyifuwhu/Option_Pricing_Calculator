import abc
import numpy as np
from scipy.stats import norm

class BSBaseModel(object):
    """
    Summary of Black Scholes Model:
        This is a base class of Black Schole Model.
    Attributes:
        S: float - Spot Price
        K: float - Strike Price
        T : float - Time to Maturity
        r: float - risk-free rate(TBD)
        sigma : float - Volatility
        div : float - dividend rate
        d1: float
        d2: float
    """
    def __init__(self, S, K, T, r, sigma, div=0):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.div = div
        self.__compute_d1d2()

    # compute d1 and d2
    def __compute_d1d2(self):
        self.d1 = (np.log(self.S / self.K) + (self.r - self.div + 0.5 * self.sigma ** 2) * self.T) / (
                    self.sigma * np.sqrt(self.T))
        self.d2 = self.d1 - self.sigma * np.sqrt(self.T)

    # calculate the option price
    @abc.abstractmethod
    def get_Option_Price(self):
        pass

    # calculate greek letters
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

    # calculate greek letters with numerical methods
    def get_delta_numerical(self, dx=0.0001):
        # get price1
        S_temp = self.S
        self.set_S(self.S + dx)
        self.__compute_d1d2()
        price1 = self.get_Option_Price()

        self.set_S(S_temp)
        self.__compute_d1d2()
        delta = (price1 - self.get_Option_Price()) / dx
        return delta


    def get_gamma_numerical(self, dx=0.0001):
        pass


    def get_theta_numerical(self, dx=0.0001):
        # get price1
        T_temp = self.T
        self.set_T(self.T + dx)
        self.__compute_d1d2()
        price1 = self.get_Option_Price()

        self.set_T(T_temp)
        self.__compute_d1d2()
        theta = (price1 - self.get_Option_Price()) / dx
        return theta



    def get_rho_numerical(self, dx=0.0001):
        # get price1
        r_temp = self.r
        self.set_r(self.r + dx)
        self.__compute_d1d2()
        price1 = self.get_Option_Price()

        self.set_r(r_temp)
        self.__compute_d1d2()
        rho = (price1 - self.get_Option_Price()) / dx
        return rho


    def get_vega_numerical(self, dx=0.0001):
        # get price1
        sigma_temp = self.sigma
        self.set_sigma(self.sigma + dx)
        self.__compute_d1d2()
        price1 = self.get_Option_Price()

        self.set_sigma(sigma_temp)
        self.__compute_d1d2()
        vega = (price1 - self.get_Option_Price()) / dx
        return vega

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
#         return K*np.exp(-r*T)*norm.cdf(-d2) - S * np.exp(-div * T)*norm.cdf(-d1)

if __name__ == "__main__":
    K=100
    T=1
    S=100
    sigma = 0.2
    r=0.06
    base = BSBaseModel(S, K, T, r, sigma, div=0)
    print(f'base model: {BSBaseModel(S, K, T, r, sigma, div=0)}')
    print(base.get_Option_Price())

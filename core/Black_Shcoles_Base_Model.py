import abc
import numpy as np
import scipy.stats as stats

class BSBaseModel(object):
    """
    Summary of Black Scholes Model:
        This is a base class of Black Schole Model.
    Attributes:
        S: float - Spot Price
        K: float - Strike Price
        tao : float - Time to Maturity
        r: float - risk-free rate(TBD)
        sigma : float - Volatility
        div : float - dividend rate
        d1: float
        d2: float
    """
    def __init__(self, S, K, tao, r, sigma, div=0):
        """
        Constructor:
            It will call the private method to compute d1 and d2.
        Args:
            S: float - Spot Price
            K: float - Strike Price
            tao : float - Time to Maturity
            r: float - risk-free rate(TBD)
            sigma : float - Volatility
            div : float - dividend rate
        """
        self.S = S
        self.K = K
        self.tao = tao
        self.r = r
        self.sigma = sigma
        self.div = div
        self.__compute_d1d2()

    # compute d1 and d2
    def __compute_d1d2(self):
        """
        Private method:
            It will compute d1, d2 and assign the value into the attributes.
        Returns:

        """
        self.d1 = (np.log(self.S / self.K) + (self.r - self.div + 0.5 * self.sigma ** 2) * self.tao) / (
                    self.sigma * np.sqrt(self.tao))
        self.d2 = self.d1 - self.sigma * np.sqrt(self.tao)

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
        """
        Public Method:
            Use the numerical method to calculate delta, the first derivatives of spot price to option price.
            It will be inherited by both call and put option.
        Args:
            dx: delta_increment

        Returns:
            delta

        """
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
        """
        Public Method:
            Use the numerical method to calculate gamma, the second derivatives of spot price to option price.
            It will be inherited by both call and put option.
        Args:
            dx: delta_increment

        Returns:
            gamma

        """
        # get delta1
        S_temp = self.S
        self.set_S(self.S + dx)
        self.__compute_d1d2()
        delta1 = self.get_delta_numerical(dx)

        self.set_S(S_temp)
        self.__compute_d1d2()
        gamma = (delta1 - self.get_delta()) / dx
        return gamma

    def get_theta_numerical(self, dx=0.0001):
        """
        Public Method:
            Use the numerical method to calculate theta, the first derivatives of  T(time to maturity) to option price.
            It will be inherited by both call and put option.
        FYI:
            theta is really special, because time to maturity = T - t, thus, we should * -1 in numerical method.
        Args:
            dx: delta_increment

        Returns:
            theta

        """
        # get price1
        T_temp = self.tao
        self.set_tao(self.tao + dx)
        self.__compute_d1d2()
        price1 = self.get_Option_Price()

        self.set_tao(T_temp)
        self.__compute_d1d2()
        theta = -1 * (price1 - self.get_Option_Price()) / dx
        return theta



    def get_rho_numerical(self, dx=0.0001):
        """
        Public Method:
            Use the numerical method to calculate rho, the first derivatives of r(interest rate) to option price.
            It will be inherited by both call and put option.

        Args:
            dx: delta_increment

        Returns:
            rho

        """
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
        """
        Public Method:
            Use the numerical method to calculate vega, the first derivatives of sigma(volatility) to option price.
            It will be inherited by both call and put option.

        Args:
            dx: delta_increment

        Returns:
            vega

        """
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

    def set_tao(self, tao_):
        self.tao = tao_

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
    K_=100
    tao_=1
    S_=100
    sigma_ = 0.2
    r_=0.06
    base = BSBaseModel(S_, K_, tao_, r_, sigma_, div=0)
    print(f'base model: {BSBaseModel(S_, K_, tao_, r_, sigma_, div=0)}')
    print(base.get_Option_Price())

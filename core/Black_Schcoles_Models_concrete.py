
from core import Black_Shcoles_Base_Model
import scipy.stats as stats
import numpy as np

class European_Call_BS(Black_Shcoles_Base_Model.BSBaseModel):
    def __init__(self, S_, K_, T_, r_, sigma_, div_=0):
        super().__init__(S_, K_, T_, r_, sigma_, div_)
        self.d1 = (np.log(self.S / self.K) + (self.r - self.div + 0.5 * self.sigma ** 2) * self.T) / (
                self.sigma * np.sqrt(self.T))
        self.d2 = self.d1 - self.sigma * self.T

    def get_Option_Price(self):
        call_price = (self.S * np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1) - self.K * np.exp(
            -self.r * self.T) * stats.norm.cdf(self.d2, 0, 1))
        return call_price

    def get_delta(self):
        delta = np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1)
        return delta

    def get_gamma(self):
        gamma = np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1) / self.S * self.sigma * np.sqrt(self.T)
        return gamma

    def get_theta(self):
        theta = -(self.S * stats.norm.cdf(self.d1, 0, 1) * self.sigma) / (2 * np.sqrt(self.T)) - self.r * self.K * np.exp(-self.r * self.T) * stats.norm.cdf(self.d2, 0, 1)
        return theta

    def get_rho(self):
        rho = self.K * self.T * np.exp(-self.r * self.T) * stats.norm.cdf(self.d2, 0, 1)
        return rho


    def get_vega(self):
        vega = 1 / np.sqrt(2 * np.pi) * self.S * np.exp(-self.div * self.T) * np.exp(-self.d1 ** 2 * 0.5) * np.sqrt(
            self.T)
        return vega

    def get_delta_numerical(self):
        price=((self.S+0.0001) * np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1) - self.K * np.exp(
            -self.r * self.T) * stats.norm.cdf(self.d2, 0, 1))
        delta=(price-self.get_Option_Price())/0.0001
        return delta

    def get_gamma_numerical(self):
        price1=price=((self.S+0.0001) * np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1) - self.K * np.exp(
            -self.r * self.T) * stats.norm.cdf(self.d2, 0, 1))
        delta1=self.get_delta_numerical()
        price2=((self.S+0.0002) * np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1) - self.K * np.exp(
            -self.r * self.T) * stats.norm.cdf(self.d2, 0, 1))
        delta2=(price2-price1)/0.0001
        gamma=(delta2-delta1)/0.0001
        return gamma

    def get_theta_numerical(self):
        price=(self.S * np.exp(-self.div * (self.T+0.0001)) * stats.norm.cdf(self.d1, 0, 1) - self.K * np.exp(
            -self.r * (self.T+0.0001)) * stats.norm.cdf(self.d2, 0, 1))
        theta=(price-self.get_Option_Price())/0.0001
        return theta

    def get_rho_numerical(self):
        price=(self.S * np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1) - self.K * np.exp(
            -(self.r+0.0001) * self.T) * stats.norm.cdf(self.d2, 0, 1))
        rho=(price-self.get_Option_Price())/0.0001
        return rho

    def get_vega_numerical(self):
        d1 = (np.log(self.S / self.K) + (self.r - self.div + 0.5 * (self.sigma+0.0001) ** 2) * self.T) / (
            (self.sigma+0.0001) * np.sqrt(self.T))
        d2 = d1 - (self.sigma+0.0001) * self.T
        price=(self.S * np.exp(-self.div * self.T) * stats.norm.cdf(d1, 0, 1) - self.K * np.exp(
            -self.r * self.T) * stats.norm.cdf(d2, 0, 1))
        vega=(price-self.get_Option_Price())/0.0001
        return vega


class European_Put_BS(Black_Shcoles_Base_Model.BSBaseModel):
    def __init__(self, S_, K_, T_, r_, sigma_, div_=0):
        super().__init__(S_, K_, T_, r_, sigma_, div_)
        self.d1 = (np.log(self.S / self.K) + (self.r - self.div + 0.5 * self.sigma ** 2) * self.T) / (
                self.sigma * np.sqrt(self.T))
        self.d2 = self.d1 - self.sigma * self.T

    def get_Option_Price(self):
        put_price = (self.K * np.exp(-self.r * self.T) * stats.norm.cdf(-self.d2, 0, 1) - self.S * np.exp(
                     -self.div * self.T) * stats.norm.cdf(-self.d1, 0, 1))
        return put_price

    def get_delta(self):
        delta = -np.exp(-self.div * self.T) * stats.norm.cdf(-self.d1, 0, 1)
        return delta

    def get_gamma(self):
        gamma = np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1) / self.S * self.sigma * np.sqrt(self.T)
        return gamma

    def get_theta(self):
        theta = -(self.S * stats.norm.cdf(self.d1, 0, 1) * self.sigma) / (2 * np.sqrt(self.T)) + self.r * self.K * np.exp(-self.r * self.T) * stats.norm.cdf(-self.d2, 0, 1)
        return theta

    def get_rho(self):
        rho = -self.K * self.T * np.exp(-self.r * self.T) * stats.norm.cdf(-self.d2, 0, 1)
        return rho

    def get_vega(self):
        vega = 1 / np.sqrt(2 * np.pi) * self.S * np.exp(-self.div * self.T) * np.exp(-self.d1 ** 2 * 0.5) * np.sqrt(
            self.T)
        return vega

    def get_delta_numerical(self):
        price=(self.K * np.exp(-self.r * self.T) * stats.norm.cdf(-self.d2, 0, 1) - (self.S+0.0001) * np.exp(
                     -self.div * self.T) * stats.norm.cdf(-self.d1, 0, 1))
        delta=(price-self.get_Option_Price())/0.0001
        return delta

    def get_gamma_numerical(self):
        price1=(self.K * np.exp(-self.r * self.T) * stats.norm.cdf(-self.d2, 0, 1) - (self.S+0.0001) * np.exp(
                     -self.div * self.T) * stats.norm.cdf(-self.d1, 0, 1))
        delta1=self.get_delta_numerical()
        price2=(self.K * np.exp(-self.r * self.T) * stats.norm.cdf(-self.d2, 0, 1) - (self.S+0.0002) * np.exp(
                     -self.div * self.T) * stats.norm.cdf(-self.d1, 0, 1))
        delta2=(price2-price1)/0.0001
        gamma=(delta2-delta1)/0.0001
        return gamma


    def get_theta_numerical(self):
        price=(self.K * np.exp(-self.r * (self.T+0.0001)) * stats.norm.cdf(-self.d2, 0, 1) - self.S * np.exp(
                     -self.div * (self.T+0.0001)) * stats.norm.cdf(-self.d1, 0, 1))
        theta=(price-self.get_Option_Price())/0.0001
        return theta

    def get_rho_numerical(self):
        price=(self.K * np.exp(-(self.r+0.0001) * self.T) * stats.norm.cdf(-self.d2, 0, 1) - self.S * np.exp(
                     -self.div * self.T) * stats.norm.cdf(-self.d1, 0, 1))
        rho=(price-self.get_Option_Price())/0.0001
        return rho

    def get_vega_numerical(self):
        d1 = (np.log(self.S / self.K) + (self.r - self.div + 0.5 * (self.sigma+0.0001) ** 2) * self.T) / (
            (self.sigma+0.0001) * np.sqrt(self.T))
        d2 = d1 - (self.sigma+0.0001) * self.T
        price=(self.K * np.exp(-self.r * self.T) * stats.norm.cdf(-d2, 0, 1) - self.S * np.exp(
                     -self.div * self.T) * stats.norm.cdf(-d1, 0, 1))
        vega=(price-self.get_Option_Price())/0.0001
        return vega


if __name__ == "__main__":
    S = 105
    K = 105
    T = 1
    r = 0.06
    sigma = 0.2
    div=0
    test_object = European_Put_BS(S, K, T, r, sigma)

    print(test_object.get_gamma_numerical())

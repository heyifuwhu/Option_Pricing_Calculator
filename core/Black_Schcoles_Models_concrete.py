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
        theta = -np.exp(-self.div * self.T) * (self.S * stats.norm.cdf(self.d1, 0, 1) * self.sigma) / (2 * np.sqrt(self.T)) - self.r * self.K * np.exp(-self.r * self.T) * stats.norm.cdf(self.d2, 0, 1) + self.div * self.S * np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1)
        return theta

    def get_rho(self):
        rho = self.K * self.T * np.exp(-self.r * self.T) * stats.norm.cdf(self.d2, 0, 1)
        return rho


    def get_vega(self):
        vega = 1 / np.sqrt(2 * np.pi) * self.S * np.exp(-self.div * self.T) * np.exp(-self.d1 ** 2 * 0.5) * np.sqrt(
            self.T)
        return vega

    def get_delta_numerical(self):
        def f(s):
            f_val = (s * np.exp(-self.div * self.T) * stats.norm.cdf(self.d1, 0, 1) - self.K * np.exp(
            -self.r * self.T) * stats.norm.cdf(self.d2, 0, 1))
            return f_val
        x = np.linspace(10, 20, 101)
        df = np.zeros_like(x)
        f_vec = f(x)
        dx=x[1]-x[0]
        for i in range(1,100):
            df[i]=(f_vec[i+1]-f_vec[i-1])/(2*dx)
        df[0] =(f_vec[1]-f_vec[0])/dx
        df[-1]=(f_vec[-1]-f_vec[-2])/dx
        return df[0]

    def get_gamma_numerical(self):
        pass

    def get_theta_numerical(self):
        pass

    def get_rho_numerical(self):
        pass

    def get_vega_numerical(self):
        pass


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
        theta = -np.exp(-self.div * self.T) * (self.S * stats.norm.cdf(self.d1, 0, 1) * self.sigma) / (
                2 * np.sqrt(self.T)) + self.r * self.K * np.exp(-self.r * self.T) * stats.norm.cdf(
                -self.d2, 0, 1) - self.div * self.S * np.exp(-self.div * self.T) * stats.norm.cdf(-self.d1, 0, 1)
        return theta

    def get_rho(self):
        rho = -self.K * self.T * np.exp(-self.r * self.T) * stats.norm.cdf(-self.d2, 0, 1)
        return rho

    def get_vega(self):
        vega = 1 / np.sqrt(2 * np.pi) * self.S * np.exp(-self.div * self.T) * np.exp(-self.d1 ** 2 * 0.5) * np.sqrt(
            self.T)
        return vega


if __name__ == "__main__":
    S = 100
    K = 100
    T = 1
    r = 0.06
    sigma = 0.2
    div=0
    test_object = European_Call_BS(S, K, T, r, sigma)

    print(test_object.get_delta_numerical())
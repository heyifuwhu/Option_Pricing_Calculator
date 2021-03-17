from core import Black_Shcoles_Base_Model
import scipy.stats as stats
import numpy as np

class European_Call_BS(Black_Shcoles_Base_Model.BSBaseModel):
    """
    Summary of Black Scholes Model for European Call Option:
        This is a concrete class of Black Schole Model for European Call Option.
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
        Args:
            S: float - Spot Price
            K: float - Strike Price
            tao : float - Time to Maturity
            r: float - risk-free rate(TBD)
            sigma : float - Volatility
            div : float - dividend rate
        """
        super().__init__(S, K, tao, r, sigma, div)

    def get_Option_Price(self):
        """
        Public Method:
            (Call) get price of European Call Option
        Returns:
            call_price: float
        """
        call_price = (self.S * np.exp(-self.div * self.tao) * stats.norm.cdf(self.d1, 0, 1) - self.K * np.exp(
            -self.r * self.tao) * stats.norm.cdf(self.d2, 0, 1))
        return call_price

    def get_delta(self):
        """
        Public Method:
            (Call) get delta, the first derivatives of spot price to option price
        Returns:
            delta: float
        """
        delta = np.exp(-self.div * self.tao) * stats.norm.cdf(self.d1, 0, 1)
        return delta

    def get_gamma(self):
        """
        Public Method:
            (Call) get gamma, the second derivatives of spot price to option price
            It contains two formulas to calculate gamma, which are the same.
        Returns:
            gamma: float
        """
        # formula 1
        gamma = np.exp(-self.div * self.tao) * stats.norm.pdf(self.d1) / (self.S * self.sigma * np.sqrt(self.tao))

        # formula 2
        # gamma = self.K * np.exp(-self.tao * self.r) * stats.norm.pdf(self.d2) / (
        #         self.S ** 2 * self.sigma * np.sqrt(self.tao))

        return gamma



    def get_theta(self):
        """
        Public Method:
            (Call) get theta, the first derivatives of T(time to maturity) to option price
        Returns:
            theta: float
        """
        theta = -np.exp(-self.div * self.tao) * self.S * stats.norm.pdf(self.d1) * self.sigma / (
                2 * np.sqrt(self.tao)) - self.r * self.K * np.exp(-self.r * self.tao) * stats.norm.cdf(
            self.d2) + self.div * self.S * np.exp(
            -self.div * self.tao) * stats.norm.cdf(self.d1)
        return theta

    def get_rho(self):
        """
        Public Method:
            (Call) get tho, the first derivatives of r(interest rate) to option price
        Returns:
            rho: float
        """
        rho = self.K * self.tao * np.exp(-self.r * self.tao) * stats.norm.cdf(self.d2)
        return rho


    def get_vega(self):
        """
        Public Method:
            (Call) get vega, the first derivatives of sigma(volatility) to option price.
            It contains three formulas to calculate vega, which are the same.
        Returns:
            vega: float
        """
        # formula 1
        # vega = 1 / np.sqrt(2 * np.pi) * self.S * np.exp(-self.div * self.tao) * np.exp(-self.d1 ** 2 * 0.5) * np.sqrt(
        #     self.tao)

        # formula 2
        vega = self.S * np.exp(-self.div * self.tao) * stats.norm.pdf(self.d1) * np.sqrt(self.tao)

        # formula 3
        # vega = self.K * np.exp(-self.r * self.tao) * stats.norm.pdf(self.d2) * np.sqrt(self.tao)

        return vega


class European_Put_BS(Black_Shcoles_Base_Model.BSBaseModel):
    """
    Summary of Black Scholes Model for European Put Option:
        This is a concrete class of Black Schole Model for European Put Option.
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
        Args:
            S: float - Spot Price
            K: float - Strike Price
            tao : float - Time to Maturity
            r: float - risk-free rate(TBD)
            sigma : float - Volatility
            div : float - dividend rate
        """
        super().__init__(S, K, tao, r, sigma, div)

    def get_Option_Price(self):
        """
        Public Method:
            (Put) get price of European Call Option
        Returns:
            put_price: float
        """
        put_price = (self.K * np.exp(-self.r * self.tao) * stats.norm.cdf(-self.d2, 0, 1) - self.S * np.exp(
                     -self.div * self.tao) * stats.norm.cdf(-self.d1, 0, 1))
        return put_price

    def get_delta(self):
        """
        Public Method:
            (Put) get delta, the first derivatives of spot price to option price.
        Returns:
            delta: float
        """
        # delta = np.exp(-self.div * self.tao) * stats.norm.cdf(self.d1 - 1)
        delta = -np.exp(-self.div * self.tao) * stats.norm.cdf(-self.d1)
        return delta

    def get_gamma(self):
        """
        Public Method:
            (Put) get gamma, the second derivatives of spot price to option price.
            It contains two formulas to calculate gamma, which are the same.
        Returns:
            gamma: float
        """
        # formula 1
        gamma = np.exp(-self.div * self.tao) * stats.norm.pdf(self.d1) / (self.S * self.sigma * np.sqrt(self.tao))

        # formula 2
        # gamma = self.K * np.exp(-self.tao * self.r) * stats.norm.pdf(self.d2) / (
        #         self.S ** 2 * self.sigma * np.sqrt(self.tao))

        return gamma

    def get_theta(self):
        """
        Public Method:
            (Put) get theta, the first derivatives of T(time to maturity) to option price
        Returns:
            theta: float
        """
        theta = -np.exp(-self.div * self.tao) * self.S * stats.norm.pdf(-self.d1) * self.sigma / (
                2 * np.sqrt(self.tao)) + self.r * self.K * np.exp(-self.r * self.tao) * stats.norm.cdf(
            -self.d2) - self.div * self.S * np.exp(
            -self.div * self.tao) * stats.norm.cdf(-self.d1)
        return theta

    def get_rho(self):
        """
        Public Method:
            (Put) get rho, the first derivatives of r(interest rate) to option price
        Returns:
            rho: float
        """
        rho = -self.K * self.tao * np.exp(-self.r * self.tao) * stats.norm.cdf(-self.d2, 0, 1)
        return rho

    def get_vega(self):
        """
        Public Method:
            (Put) get vega, the first derivatives of sigma(volatility) to option price
            It contains three formulas to calculate vega, which are the same.
        Returns:
            vega: float
        """
        # formula 1
        # vega = 1 / np.sqrt(2 * np.pi) * self.S * np.exp(-self.div * self.tao) * np.exp(-self.d1 ** 2 * 0.5) * np.sqrt(
        #     self.tao)

        # formula 2
        vega = self.S * np.exp(-self.div * self.tao) * stats.norm.pdf(self.d1) * np.sqrt(self.tao)

        # formula 3
        # vega = self.K * np.exp(-self.r * self.tao) * stats.norm.pdf(self.d2) * np.sqrt(self.tao)

        return vega


if __name__ == "__main__":
    # test case 1
    ##############################
    # S = 105
    # K = 105
    # T = 1
    # r = 0.06
    # sigma = 0.2
    # div=0
    # test_object = European_Put_BS(S, K, T, r, sigma)

    # test case 2
    ##############################
    S = 200
    K = 210
    T = 1
    r = 0.00
    sigma = 0.2
    div = 0.0
    dx = 0.000001
    call = European_Call_BS(S, K, T, r, sigma, div)
    put = European_Put_BS(S, K, T, r, sigma, div)
    print("call: ", call.get_Option_Price())
    print("call delta0: ", call.get_delta())
    print("call delta1: ", call.get_delta_numerical(dx))
    print("call gamma0: ", call.get_gamma())
    print("call gamma1: ", call.get_gamma_numerical(dx))
    print("call theta0: ", call.get_theta())
    print("call theta1: ", call.get_theta_numerical(dx))
    print("call rho0: ", call.get_rho())
    print("call rho1: ", call.get_rho_numerical(dx))
    print("call vega0: ", call.get_vega())
    print("call vega1: ", call.get_vega_numerical(dx))
    print("\n###############################")
    print("put: ", put.get_Option_Price())
    print("put delta0: ", put.get_delta())
    print("put delta1: ", put.get_delta_numerical(dx))
    print("put gamma0: ", put.get_gamma())
    print("put gamma1: ", put.get_gamma_numerical(dx))
    print("put theta0: ", put.get_theta())
    print("put theta1: ", put.get_theta_numerical(dx))
    print("put rho0: ", put.get_rho())
    print("put rho1: ", put.get_rho_numerical(dx))
    print("put vega0: ", put.get_vega())
    print("put vega1: ", put.get_vega_numerical(dx))

    # #print(test_object.get_gamma_numerical())
    # # test git
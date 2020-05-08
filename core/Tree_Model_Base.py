import numpy as np

class tree_model(object):
    """
    Summary of Binomial Tree Model:
        This is a base class of Black Schole Model.
    Attributes:
        S: Spot Price
        K: Strike Price
        T : Time to Maturity
        r: risk-free rate(TBD)
        sigma : Volatility
        div : dividend rate
    """

    def __init__(self, S_: float, K_: float, T_: float, r_: float, sigma_: float, div_: float = 0):
        self.S = S_
        self.K = K_
        self.T = T_
        self.r = r_
        self.sigma = sigma_
        self.div = div_

    def European_Binomial_Mutiplicative(self, option_type, N, u, d):
        """

        :param str - option_type: option type "call" or "put"
        :param int - N: number of step
        :return: float - option price
        """
        # record value
        dt = self.T / N
        p = (np.exp(self.r * dt) - d) / (u - d)
        q = 1 - p
        disc = np.exp(-self.r * dt)

        # initialize underlying asset price
        St = np.asarray([self.S * u ** (N - i) * d ** i for i in range(N + 1)])

        # call
        if option_type == "call":
            C = np.where(St >= self.K, St - self.K, 0)
            while (len(C) > 1):
                C = disc * (p * C[:-1] + q * C[1:])
        # put
        if option_type == "put":
            C = np.where(self.K >= St, self.K - St, 0)
            while (len(C) > 1):
                C = disc * (p * C[:-1] + q * C[1:])
        return C[0]

    def American_Binomial_Multiplicative(self, option_type, N, u, d):
        # record value
        dt = self.T / N
        p = (np.exp(self.r * dt) - d) / (u - d)
        q = 1 - p
        disc = np.exp(-self.r * dt)

        # initialize underlying asset price
        St = np.asarray([self.S * u ** (N - i) * d ** i for i in range(N + 1)])

        # call
        if option_type == "call":
            C = np.where(St >= self.K, St - self.K, 0)
            while (len(C) > 1):
                C = disc * (p * C[:-1] + q * C[1:])
                St = St[:-1] * d
                C = np.where(C > (St - self.K), C, St - self.K)
        # put
        if option_type == "put":
            C = np.where(self.K >= St, self.K - St, 0)
            while (len(C) > 1):
                C = disc * (p * C[:-1] + q * C[1:])
                St = St[:-1] * d
                C = np.where(C > (self.K - St), C, self.K - St)
        return C[0]


    # mutators and accessors
    def set_S(self, S_):
        self.S = S_

    def set_K(self, K_):
        self.K = K_

    def set_T(self, T_):
        self.T = T_

    def set_r(self, r_):
        self.r = r_

    def set_sigma(self, sigma_):
        self.sigma = sigma_

    def sef_div(self, div_):
        self.div = div_

if __name__ == "__main__":
    S_ = 100
    K_ = 100
    T_ = 1
    r_ = 0.06
    sigma_ = 0.2
    u = 1.1
    N = 3
    model = tree_model(S_,K_,T_,r_,sigma_)
    print(f"European call Binomial Multiplicative : {model.European_Binomial_Mutiplicative('call', N, u, 1 / u)}")
    print(f"European put Binomial Multiplicative : {model.European_Binomial_Mutiplicative('put', N, u, 1 / u)}")
    print(f"American call Binomial Multiplicative : {model.American_Binomial_Multiplicative('call', N, u, 1 / u)}")
    print(f"American put Binomial Multiplicative : {model.American_Binomial_Multiplicative('put', N, u, 1 / u)}")
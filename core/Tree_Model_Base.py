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
        self.S = S_git
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

    def Multipl_Binomial_Tree_American(Option, K, T, S, r, N, u, d):
        """
        Parameters
        ----------
        Option: str
            "call" or "put"
        K: float
            strike price
        T: float
            time to maturity
        S: float
            spot price
        r: float
            interest rate
        N: int
            number of period
        u: float
            upward

        d: float
            downward factor
        Returns
        ----------
        res: float
            option price
        """
        # record value
        dt = T / N
        p = (np.exp(r * dt) - d) / (u - d)
        q = 1 - p
        disc = np.exp(-r * dt)

        # initialize underlying asset price
        St = np.asarray([S * u ** (N - i) * d ** i for i in range(N + 1)])

        # call
        if Option == "call":
            C = np.where(St >= K, St - K, 0)
            while (len(C) > 1):
                C = disc * (p * C[:-1] + q * C[1:])
                St = St[:-1] * d
                C = np.where(C > (St - K), C, St - K)
        # put
        if Option == "put":
            C = np.where(K >= St, K - St, 0)
            while (len(C) > 1):
                C = disc * (p * C[:-1] + q * C[1:])
                St = St[:-1] * d
                C = np.where(C > (K - St), C, K - St)
        return C[0]

    S = 100
    K = 100
    T = 1
    r = 0.06
    N = 3
    u = 1.1
    d = 1 / u
    print(f'European Call: {Multipl_Binomial_Tree_European("call", K, T, S, r, N, u, d)}')
    print(f'American Put: {Multipl_Binomial_Tree_American("put", K, T, S, r, N, u, d)}')
    print(Multipl_Binomial_Tree_European("call", K, T, S, 0.05, 3, 1.1, 0.9))

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

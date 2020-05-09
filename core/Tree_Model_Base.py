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

    def European_Binomial_Multiplicative(self, option_type, N, u, d):
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

    def European_Binomial_Additive(self,option_type, N):
        """

        :param str - option_type: option type "call" or "put"
        :param int - N: number of step
        :return: float - option price
        """

        # record value
        dt = self.T / N
        disc = np.exp(-self.r * dt)
        nu = self.r - 0.5 * self.sigma ** 2
        dx = np.sqrt(self.sigma ** 2 * dt + (nu * dt) ** 2)
        du = - dx
        pu = 0.5 + 0.5 * nu * dt / dx
        pd = 1 - pu

        # initialize underlying asset price
        St = self.S * np.exp(np.asarray([(N - i) * dx + i * du for i in range(N + 1)]))

        # call
        if option_type == "call":
            C = np.where(St >= self.K, St - self.K, 0)
            while (len(C) > 1):
                C = disc * (pu * C[:-1] + pd * C[1:])
        # put
        if option_type == "put":
            C = np.where(self.K >= St, self.K - St, 0)
            while (len(C) > 1):
                C = disc * (pu * C[:-1] + pd * C[1:])
        return C[0]

    def American_Binomial_Additive(self, option_type, N):
        """

        :param str - option_type: option type "call" or "put"
        :param int - N: number of step
        :return: float - option price
        """
        # record value
        dt = self.T / N
        disc = np.exp(-self.r * dt)
        nu = self.r - 0.5 * self.sigma ** 2
        dx = np.sqrt(self.sigma ** 2 * dt + (nu * dt) ** 2)
        du = - dx
        pu = 0.5 + 0.5 * nu * dt / dx
        pd = 1 - pu

        # initialize underlying asset price
        St = self.S * np.exp(np.asarray([(N - i) * dx + i * du for i in range(N + 1)]))
        # call
        if option_type == "call":
            C = np.where(St >= self.K, St - self.K, 0)
            while (len(C) > 1):
                C = disc * (pu * C[:-1] + pd * C[1:])
                St = St[:-1] * np.exp(du)
                C = np.where(C > (St - self.K), C, St - self.K)
        # put
        if option_type == "put":
            C = np.where(self.K >= St, self.K - St, 0)
            while (len(C) > 1):
                C = disc * (pu * C[:-1] + pd * C[1:])
                St = St[:-1] * np.exp(du)
                C = np.where(C > (self.K - St), C, self.K - St)
        return C[0]


    def European_Trinomial(self, option_type, N, dx):
        """

        :param str - option_type: option type "call" or "put"
        :param int - N: number of step
        :return: float - option price
        """
        # record value
        dt = self.T / N
        nu = self.r - self.div - 0.5 * self.sigma ** 2
        pu = 0.5 * ((self.sigma ** 2 * dt + (nu * dt) ** 2) / dx ** 2 + nu * dt / dx)
        pd = 0.5 * ((self.sigma ** 2 * dt + (nu * dt) ** 2) / dx ** 2 - nu * dt / dx)
        pm = 1 - pd - pu
        disc = np.exp(-self.r * dt)

        # initialize underlying asset price
        St = self.S * np.exp(np.asarray([dx * i for i in range(-N, N + 1)]))

        # call
        if option_type == "call":
            C = np.where(St >= self.K, St - self.K, 0)
            while (len(C) > 1):
                C = disc * (pd * C[:-2] + pm * C[1:-1] + pu * C[2:])
        # put
        if option_type == "put":
            C = np.where(St <= self.K, self.K - St, 0)
            while (len(C) > 1):
                C = disc * (pd * C[:-2] + pm * C[1:-1] + pu * C[2:])
        return C[0]

    def American_Trinomial(self, option_type, N, dx):
        """

        :param str - option_type: option type "call" or "put"
        :param int - N: number of step
        :return: float - option price
        """
        # record value
        dt = self.T / N
        nu = self.r - self.div - 0.5 * self.sigma ** 2
        pu = 0.5 * ((self.sigma ** 2 * dt + (nu * dt) ** 2) / dx ** 2 + nu * dt / dx)
        pd = 0.5 * ((self.sigma ** 2 * dt + (nu * dt) ** 2) / dx ** 2 - nu * dt / dx)
        pm = 1 - pd - pu
        disc = np.exp(-self.r * dt)

        # initialize underlying asset price
        St = self.S * np.exp(np.asarray([dx * i for i in range(-N, N + 1)]))

        # call
        if option_type == "call":
            C = np.where(St >= self.K, St - self.K, 0)
            while (len(C) > 1):
                C = disc * (pd * C[:-2] + pm * C[1:-1] + pu * C[2:])
                St = St[1:-1]
                C = np.where(C >= St - self.K, C, St - self.K)
        # put
        if option_type == "put":
            C = np.where(St <= self.K, self.K - St, 0)
            while (len(C) > 1):
                C = disc * (pd * C[:-2] + pm * C[1:-1] + pu * C[2:])
                St = St[1:-1]
                C = np.where(C >= self.K - St, C, self.K - St)
        return C[0]

    K = 100
    T = 1
    S = 100
    sigma = 0.2
    r = 0.06
    div = 0.03
    N = 3
    dx = 0.2


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
    print("Binomial Multiplicative")
    print(f"European call Binomial Multiplicative : {model.European_Binomial_Mutiplicative('call', N, u, 1 / u)}")
    print(f"European put Binomial Multiplicative : {model.European_Binomial_Mutiplicative('put', N, u, 1 / u)}")
    print(f"American call Binomial Multiplicative : {model.American_Binomial_Multiplicative('call', N, u, 1 / u)}")
    print(f"American put Binomial Multiplicative : {model.American_Binomial_Multiplicative('put', N, u, 1 / u)}")

    print("\nBinomial Additive")
    print(f"European call Binomial Additive : {model.European_Binomial_Additive('call', N)}")
    print(f"European put Binomial Additive : {model.European_Binomial_Additive('put', N)}")
    print(f"American call Binomial Additive : {model.American_Binomial_Additive('call', N)}")
    print(f"American put Binomial Additive : {model.American_Binomial_Additive('put', N)}")

    dx =0.2
    print("\nTrinomial Tree")
    print(f"European call Trinomial : {model.European_Trinomial('call', N, dx)}")
    print(f"European put Trinomial : {model.European_Trinomial('put', N, dx)}")
    print(f"American call Trinomial : {model.American_Trinomial('call', N, dx)}")
    print(f"American put Trinomial : {model.American_Trinomial('put', N, dx)}")
    # test
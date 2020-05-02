import pandas as pd
from math import log as log
from math import sqrt as sqrt
from math import exp as exp
from scipy.stats import norm
from numpy import nan


def BSM(Option_type, S, K, vol, T, r):
    """
    Black-Scholes Model

    Option_type: "call" or "put"
    S: spot price
    K: strike price
    vol : volatility
    T : Maturity
    r: risk-free rate

    """
    d1 = (log(S / K) + (r + 0.5 * vol ** 2) * T) / (vol * sqrt(T))
    d2 = d1 - vol * sqrt(T)
    if Option_type == "call":
        Option = S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)
        return Option
    elif Option_type == "put":
        Option = K * exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return Option
    else:
        return "Error: parameter Option_type only takes in 'call or 'put'"
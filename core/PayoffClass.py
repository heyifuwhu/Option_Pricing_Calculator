import abc

class PayOffBase(object):
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_payoff(self):
        pass

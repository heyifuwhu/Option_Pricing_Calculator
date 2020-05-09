from core import Pay_Off_Base
import numpy as np

class European_Pay_Off(Pay_Off_Base.PayOffBaseClass):
    def __init__(self, option_type_, Strike_):
        super().__init__()
        self.option_type_ = option_type_
        self.Strike = Strike_

    def get_payoff(self, S):
        if self.option_type_ == "call":
            return np.maximum(S - self.Strike, 0)
        if self.option_type_ == "put":
            return np.(self.Strike - S, 0)


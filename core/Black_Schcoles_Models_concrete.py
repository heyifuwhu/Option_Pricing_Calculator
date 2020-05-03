from core import Black_Shcoles_Base_Model

class European_Call_BS(Black_Shcoles_Base_Model.BSBaseModel):
    def __init__(self, S_, K_, T_, r_, sigma_, div_=0):
        super().__init__(S_, K_, T_, r_, sigma_, div_)


class European_Put_BS(Black_Shcoles_Base_Model.BSBaseModel):
    def __init__(self, S_, K_, T_, r_, sigma_, div_=0):
        super().__init__(S_, K_, T_, r_, sigma_, div_)


if __name__ == "__main__":
    S = 42
    K = 40
    T = 1
    r = 0.03
    sigma = 0.2
    test_object = European_Call_BS(S, K, T, r, sigma)
from typing import List

# from ..autocall import AutocallTemplate
from .. import AutocallTemplate

class OriginalSnowBall(AutocallTemplate):
    """经典雪球结构

    基类确定了autocall大类结构的设计模板。任何一种具体的结构，如经典/降敲/早利等，
    都基于该模板，定义相应的payoff形式、敲入敲出边界等。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 票息率，默认为0，
        view_day: 观察日，默认隔21个交易日观察一次，总时间为1年
        time_to_maturity: 续存期，默认为1年
    """
    name = '经典雪球'

    def __init__(
        self,
        knock_in_level: List[float] = [1.0],
        knock_out_level: List[float] = [1.0],
        coupon_rate: List[float] = 0.0,
        view_day: List[int] = [i*21-1 for i in range(1, 13)],
        time_to_maturity: float = 1.0
    ) -> None:
        """构造函数，定义autocall结构大类的参数"""
        self.knock_in_level = knock_in_level
        self.knock_out_level = knock_out_level
        self.coupon_rate = coupon_rate
        self.view_day = view_day
        self.time_to_maturity = time_to_maturity


    def set_knock_in_level(self) -> None:
        pass


    def set_knock_out_level(self) -> None:
        pass


    def set_coupon_rate(self) -> None:
        pass


    def set_view_day(self) -> None:
        pass


    def set_time_to_maturity(self) -> None:
        pass

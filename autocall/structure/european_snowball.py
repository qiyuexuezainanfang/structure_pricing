from typing import Dict

from .. import AutocallTemplate
from .. import PricingEngine


class EuropeanSnowBall(AutocallTemplate, PricingEngine):
    """欧式雪球

    仅在最后一天观察是否敲入。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '欧式雪球'

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义欧式雪球的参数"""
        super().__init__(setting)

    def _set_knock_out_view_day(self, setting) -> None:
        self.knock_out_view_day: list[int] = [
            setting['time_to_maturity']
            * setting['knock_out_view_day'] * 21 - 1
            ]

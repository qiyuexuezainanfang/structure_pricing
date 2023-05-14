from typing import Dict

from .. import AutocallTemplate
from .. import PricingEngine


class OriginalSnowBall(AutocallTemplate, PricingEngine):
    """经典雪球结构

    经典雪球结构在下方提供了下跌保护，只要后市跌幅不大，都可获得固定票息，
    若大幅下跌，只要在期限内涨回至期初价格，仍可获得固定票息，
    极端行情下大跌未涨回，投资者相当于直接持有标的资产。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '经典雪球'

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义经典雪球的参数"""

        super().__init__(setting)

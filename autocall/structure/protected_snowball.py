from typing import Dict

from . import OriginalSnowBall


class ProtectedSnowBall(OriginalSnowBall):
    """限损雪球

    在经典雪球的基础上限制最大亏损。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
        protected_level: 被保护的净值水平
    """

    name = '限损雪球'

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity',
        'protected_level'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义限损雪球的参数"""
        super.__init__(setting)

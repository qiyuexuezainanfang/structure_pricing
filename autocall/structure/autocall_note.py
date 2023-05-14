from typing import Dict

from . import OriginalSnowBall


class AutocallNote(OriginalSnowBall):
    """小雪球

    期限不固定，当触发特定条件时，期权自动敲出，投资者获得收益

    属性:
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '小雪球'

    params = [
        'knock_out_level',
        'coupon_rate',
        'knock_out_view_day',
        'time_to_maturity',
        'coupon_div'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义小雪球的参数"""
        super().__init__(setting)
        self.knock_in_level = 0

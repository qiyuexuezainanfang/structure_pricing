from typing import Dict

from . import OriginalSnowBall


class CouponSnowBall(OriginalSnowBall):
    """红利雪球

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '红利雪球'

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义红利雪球的参数"""
        super().__init__(setting)

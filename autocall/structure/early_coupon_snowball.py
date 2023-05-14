from typing import Dict

from . import CouponSnowBall


class EarlyCouponSnowBall(CouponSnowBall):
    """早利雪球

    在红利雪球的基础上，敲出票息第一阶段比第二阶段高

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '早利雪球'

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义早利雪球的参数"""
        super().__init__(setting)
        self._set_coupon_rate()

    def _set_coupon_rate(self) -> None:
        """生成敲出票息率列表"""
        self.new_coupon_rate = []
        high_coupon = self.coupon_rate[0]
        low_coupon = self.coupon_rate[1]
        self.new_coupon_rate.extend([high_coupon] * 12)
        self.new_coupon_rate.extend(
            [low_coupon] * (len(self.knock_out_view_day) - 12))
        self.coupon_rate = self.new_coupon_rate

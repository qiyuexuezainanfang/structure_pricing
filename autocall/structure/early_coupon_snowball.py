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

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义早利雪球的参数"""
        super.__init__(setting)

        # 如果敲出票息率是整数/浮点数，则默认设置后半段时间减半
        if (
            isinstance(self.coupon_rate, int)
                or isinstance(self.coupon_rate, float)):
            self._set_coupon_rate()

    def _set_coupon_rate(self) -> None:
        """生成默认敲出票息率列表"""
        high_count = len(self.knock_out_view_day) // 2
        low_count = len(self.knock_out_view_day) - high_count
        self.coupon_rate = [self.coupon_rate] * high_count \
            + [self.coupon_rate / 2] * low_count

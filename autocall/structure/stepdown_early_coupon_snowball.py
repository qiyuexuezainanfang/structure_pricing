from typing import Dict

import numpy as np

from . import EarlyCouponSnowBall


class StepDownEarlyCouponSnowBall(EarlyCouponSnowBall):
    """双降雪球

    在早利雪球的基础上，逐步降低敲出价

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '双降雪球'

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义双降雪球的参数"""
        super.__init__(setting)

        # 如果敲出水平是一个整数或者浮点数，则生成降敲列表
        if (
            isinstance(self.knock_out_level, int)
                or isinstance(self.knock_out_level, float)):
            self._set_knock_out_level()

    def _set_knock_out_level(self) -> None:
        """生成默认敲出水平列表"""
        self.knock_out_level = np.linspace(
            self.knock_out_level,
            self.knock_in_level,
            len(self.knock_out_view_day)
            )

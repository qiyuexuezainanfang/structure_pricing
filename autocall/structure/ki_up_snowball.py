from typing import Dict

import numpy as np

from . import OriginalSnowBall


class KiUpSnowBall(OriginalSnowBall):
    """KI递增雪球

    在经典雪球基础上，敲入价逐渐递增。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = 'KI递增雪球'

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义KI递增雪球的参数"""
        super.__init__(setting)

        # 如果敲入水平是一个整数或者浮点数，则生成递增敲入价列表
        if (
            isinstance(self.knock_in_level, int)
                or isinstance(self.knock_in_level, float)):
            self._set_knock_in_level()

    def _set_knock_in_level(self) -> None:
        """生成默认敲入水平列表"""
        self.knock_in_level = np.linspace(
            self.knock_in_level,
            1,
            self.time_to_maturity * 252
            )

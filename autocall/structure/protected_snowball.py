from typing import Dict

import numpy as np

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
        super().__init__(setting)

    def _cal_loss(self) -> None:
        """计算损失，重载PricingEngine的函数"""
        loss_rate_array = (self.st[
                -1,
                self.not_knock_out
                & self.knock_in_scenario
                & (self.st[-1] < self.s0)
                ] / self.s0 - 1)
        max_loss_rate = self.protected_level / self.s0 - 1
        protected_loss_rate_array = np.array(
            list(map(lambda x: max(x, max_loss_rate), loss_rate_array)))
        self.loss = np.sum(
            protected_loss_rate_array
            * self.s0
            * np.exp(-self.r * self.time_to_maturity)
            )  # 敲入造成的总亏损，对于st>s0的情况，损益为0，不需要考虑

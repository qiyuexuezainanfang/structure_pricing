from typing import Dict

import numpy as np

from . import OriginalSnowBall


class EnhancedSnowBall(OriginalSnowBall):
    """增强型雪球

    在经典雪球的基础上，上涨时挂钩一定比例指数涨幅。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
        participation_rate_no_knock_in: 上涨参与率
    """

    name = '增强型雪球'

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity',
        'participation_rate_no_knock_in'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义增强型雪球的参数"""
        super().__init__(setting)

    def _cal_knock_out_payoff(self) -> None:
        """重载PricingEgine的敲出payoff"""
        super()._cal_knock_out_payoff()
        # 计算上涨参与收益
        rise_profit = [
            self.st[t.astype(int), i]
            for i, t in enumerate(self.knock_out_date)
            if self.knock_out_date[i] != np.inf]
        rise_profit = np.sum(
            (np.array(rise_profit) - self.knock_out_level)
            * self.participation_rate_no_knock_in)
        self.knock_out_profit = self.knock_out_profit + rise_profit

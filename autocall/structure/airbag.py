from typing import Dict

import numpy as np

from . import OriginalSnowBall


class Airbag(OriginalSnowBall):
    """安全气囊

    设置价格保护区间，标的资产价格未跌破安全边界则不承受价格下降的风险。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        time_to_maturity: 续存期，默认为1年
        participation_rate_no_knock_in: 未敲入参与率
        participation_rate_knock_in: 敲入后参与率
    """

    name = '安全气囊'

    params = [
        'knock_in_level',
        'participation_rate_no_knock_in',
        'participation_rate_knock_in',
        'time_to_maturity'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义安全气囊的参数"""
        super().__init__(setting)
        self.knock_out_level = np.inf
        self.coupon_rate = 0
        self.coupon_div = 0

    def _cal_knock_out_payoff(self) -> None:
        """计算敲出payoff，这里计算的是上涨参与收益"""
        self.knock_out_profit = 0

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

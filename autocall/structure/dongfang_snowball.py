from typing import Dict

import numpy as np

from . import OriginalSnowBall


class DongfangSnowBall(OriginalSnowBall):
    """东方雪球

    敲出分红型雪球式期权，是雪球式期权的变形，主要期权要素和雪球式期权相同。
    不同的是，合约敲出可以获得约定行权价以上额外的上涨分红收益

    属性:
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        knock_in_level：敲入水平
        coupon_rate: 敲出票息率，
        coupon_div: 红利票息率
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
        abs_div_return: 绝对返息
        annualized_div_return：年化返息
        abs_div_return_2：绝对返息2
        annualized_div_return_2：年化返息2
        up_participation_rate：上涨参与率
        down_participation_rate：下跌参与率
        coupon_div：红利票息
        pre_paid_rate：预付金率
        knock_in_high_k：敲入高行权价
        knock_in_low_k：敲入低行权价
        nominal_principal: 名义本金
    """

    name = '东方雪球'

    params = [
        'knock_out_level',
        'knock_in_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity',
        'abs_div_return',
        'annualized_div_return',
        'abs_div_return_2',
        'annualized_div_return_2',
        'up_participation_rate',
        'down_participation_rate',
        'pre_paid_rate',
        'knock_in_high_k',
        'knock_in_low_k',
        'nominal_principal'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义东方雪球的参数"""
        super().__init__(setting)

    def _cal_knock_out_payoff(self) -> None:
        super()._cal_knock_out_payoff()
        self.knock_out_profit = np.sum(
            self.nominal_principal * self.up_participation_rate
            * (
                self.knock_out_year
                * (self.coupon_rate
                    + self.pre_paid_rate * self.annualized_div_return_2
                    + self.annualized_div_return)
                + self.abs_div_return
                + self.pre_paid_rate * self.abs_div_return_2
                + self.pre_paid_rate)
            * np.exp(-self.r * self.knock_out_year))  # 把payoff先折现再求和,计算敲出总所入

    def _cal_hold_to_maturity_payoff(self) -> None:
        super()._cal_hold_to_maturity_payoff()
        self.hold_to_maturity_profit = self.hold_to_maturity_count\
            * self.nominal_principal\
            * self.up_participation_rate\
            * (
                (self.coupon_div
                    + self.pre_paid_rate * self.annualized_div_return_2
                    + self.annualized_div_return)
                * self.time_to_maturity + self.abs_div_return
                + self.pre_paid_rate * self.abs_div_return_2
                + self.pre_paid_rate)\
            * np.exp(-self.r * self.time_to_maturity)  # 平稳持有到期收入

    def _cal_loss(self) -> None:
        super()._cal_loss()
        max_list = np.array(list(map(
            lambda x: max(x, 0),
            self.knock_in_high_k * self.s0
            - self.st[-1, self.not_knock_out & self.knock_in_scenario])))
        min_list = np.array(list(map(
            lambda x: min(x, (self.knock_in_high_k - self.knock_in_low_k)
                            * self.s0),
            max_list)))
        self.loss = np.sum((
            self.nominal_principal * self.down_participation_rate
            * (
                (self.annualized_div_return
                    + self.pre_paid_rate * self.annualized_div_return_2)
                * self.time_to_maturity + self.abs_div_return
                + self.pre_paid_rate * self.abs_div_return_2
                + self.pre_paid_rate)
            - self.nominal_principal * self.down_participation_rate / self.s0
            * min_list * self.down_participation_rate)
            * np.exp(-self.r * self.time_to_maturity))

from typing import Dict, List
from abc import ABC

import numpy as np
# import cupy as cp


class PricingEngine(ABC):
    """定价引擎, 用来为Autocall结构进行定价。

    本类的成员变量和方法都会被autocall继承。使用时分以下几步：
    1、被autocall继承，通过autocall实例化。
    2、运行set_underlying_parameters设置标的资产的参数。
    3、运行定价函数或希腊字母计算函数

    属性:
        s0: 标的资产初始价格，默认是None，
        sigma: 标的资产年化波动率，默认是None，
        r: 无风险利率，默认为None，
        q: 标的资产分红率，默认为None。
    """

    underlying_params = [
        's0',
        'sigma',
        'r',
        'q',
    ]

    def set_underlying_parameters(self, setting: Dict[str, float]) -> None:
        """设置标的资产参数"""

        # 确保标的资产参数都有被传入，并且创建它们
        for param in self.underlying_params:
            if param not in setting.keys():
                print(f'标的资产缺少{param}参数')
                return
            setattr(self, param, setting[param])
        self.drift: float = self.r - self.q

    def mc_pricing(self) -> float:
        """蒙特卡洛定价

        对雪球大类结构定价时，都要有以下几个步骤：
        1、生成路径
        2、判断每条路径是否敲出，若有，记录下敲出日期
        3、计算敲出的payoff
        4、计算不敲入也不敲出的payoff
        5、计算敲入的亏损
        6、计算价格

        本函数适用于大部分结构，某些特殊结构，可能需要重写其中的某个'_'开头的被保护函数

        """
        self._generate_paths()
        self._cal_knock_out_date()
        self._cal_knock_out_payoff()
        self._cal_hold_to_maturity_payoff()
        self._cal_loss()
        self._cal_price()
        return self.price

    def _generate_paths(self, n_path: int = 300000) -> None:
        """生成标的路径"""
        self.n_path = n_path
        tstep = self.time_to_maturity * 252 - 1
        dt = self.time_to_maturity / tstep
        # z = cp.random.normal(size=(tstep + 1, n_path))
        # st = cp.zeros((tstep + 1, n_path))
        z = np.random.normal(size=(tstep + 1, n_path))
        st = np.zeros((tstep + 1, n_path))
        st[0] = self.s0
        # for t in range(1, tstep + 1):
        #     st[t] = st[t - 1] * cp.exp(
        #         (self.drift - 0.5 * self.sigma ** 2) * dt
        #         + self.sigma * cp.sqrt(dt) * z[t]
        #         )

        for t in range(1, tstep + 1):
            st[t] = st[t - 1] * np.exp(
                (self.drift - 0.5 * self.sigma ** 2) * dt
                + self.sigma * np.sqrt(dt) * z[t]
                )
        self.st = st

    def _cal_knock_out_date(self) -> None:
        """计算每条路径敲出时间"""
        # knock_out_scenario = cp.tile(
        #     self.autocall.knock_out_view_day, (self.n_path, 1)).T
        # knock_out_scenario = cp.where(
        #     self.st[self.autocall.knock_out_view_day]
        #     > self.autocall.knock_out_level,
        #     knock_out_scenario,
        #     cp.inf
        #     )
        knock_out_scenario = np.tile(
            self.knock_out_view_day, (self.n_path, 1)).T
        self.knock_out_level = np.array(self.knock_out_level) * self.s0
        knock_out_level = np.tile(
            self.knock_out_level, (self.n_path, 1)).T
        knock_out_scenario = np.where(
            self.st[self.knock_out_view_day]
            > knock_out_level,
            knock_out_scenario,
            np.inf
            )
        # 记录每条路径的具体敲出日，如果无敲出则保留inf
        knock_out_date = np.min(knock_out_scenario, axis=0)
        self.knock_out_date = knock_out_date

    def _cal_knock_out_payoff(self) -> None:
        """计算敲出payoff"""
        is_knock_out = self.knock_out_date != np.inf
        if isinstance(self.coupon_rate, List):
            coupon_rate_array = np.array(self.coupon_rate)
            knock_out_month = (self.knock_out_date + 1) / 21
            knock_out_month = knock_out_month[is_knock_out]
            knock_out_year = knock_out_month / 12
            knock_out_month = knock_out_month.astype(int) - 1
            self.coupon_rate = coupon_rate_array[knock_out_month]
        else:
            knock_out_year = self.knock_out_date[is_knock_out] / 252  # 把天化为年

        knock_out_profit = np.sum(
            knock_out_year
            * self.coupon_rate
            * self.s0
            * np.exp(-self.r * knock_out_year)
            )  # 把payoff先折现再求和,计算敲出总所入
        self.knock_out_profit = knock_out_profit

    def _cal_hold_to_maturity_payoff(self) -> None:
        """计算持有到期的payoff"""
        # 判断某一条路径是否有敲入
        knock_in_level = np.tile(
            self.knock_in_level, (self.n_path, 1)).T
        self.knock_in_scenario = np.any(
            self.st < knock_in_level * self.s0, axis=0)
        # 持有到期，没有敲入也没有敲出
        self.not_knock_out = self.knock_out_date == np.inf
        hold_to_maturity = (~ self.knock_in_scenario) \
            & self.not_knock_out
        # 平稳持有到期路径条数
        hold_to_maturity_count = np.count_nonzero(hold_to_maturity)
        hold_to_maturity_profit = hold_to_maturity_count\
            * self.coupon_div\
            * self.s0\
            * np.exp(-self.r * self.time_to_maturity)  # 平稳持有到期收入
        self.hold_to_maturity_profit = hold_to_maturity_profit

    def _cal_loss(self) -> None:
        """计算损失"""
        self.loss = np.sum(
            (self.st[
                -1,
                self.not_knock_out
                & self.knock_in_scenario
                & (self.st[-1] < self.s0)
                ] / self.s0 - 1)
            * self.s0
            * np.exp(-self.r * self.time_to_maturity)
            )  # 敲入造成的总亏损，对于st>s0的情况，损益为0，不需要考虑

    def _cal_price(self) -> None:
        """计算期权价格"""
        self.price = (
            self.hold_to_maturity_profit
            + self.knock_out_profit
            + self.loss) / self.n_path

    def mc_delta(self) -> float:
        self.pre_st = self.st + 0.01
        self.beyond_st = self.st - 0.01
        pass

    def mc_gamma(self) -> float:
        pass

    def mc_vega(self) -> float:
        pass

    def mc_theta(self) -> float:
        pass

    def mc_charm(self) -> float:
        pass

    def mc_vanna(self) -> float:
        pass

    def mc_vomma(self) -> float:
        pass

    def mc_speed(self) -> float:
        pass

    def mc_zomma(self) -> float:
        pass

    def mc_greeks(self) -> float:
        pass

    def pde_pricing(self) -> float:
        """有限差分定价"""
        # 显式差分

        # 隐式差分

        # 半隐式差分

        # 差分格式不均匀

        pass

    def pde_delta(self) -> float:
        pass

    def pde_gamma(self) -> float:
        pass

    def pde_vega(self) -> float:
        pass

    def pde_theta(self) -> float:
        pass

    def pde_charm(self) -> float:
        pass

    def pde_vanna(self) -> float:
        pass

    def pde_vomma(self) -> float:
        pass

    def pde_speed(self) -> float:
        pass

    def pde_zomma(self) -> float:
        pass

    def pde_greeks(self) -> float:
        pass

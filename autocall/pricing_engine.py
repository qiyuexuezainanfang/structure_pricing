from typing import Dict

import numpy as np
import cupy as cp


class PricingEngine:
    """定价引擎, 用来为Autocall结构进行定价。

    使用时分以下几步：
    1、实例化（推荐不带任何参数）。
    2、运行set_underlying_parameters设置标的资产的参数。
    3、运行add_autocall添加具体的结构类，autocall_setting是结构相关参数。
    4、运行定价函数或希腊字母计算函数

    属性:
        s0: 标的资产初始价格，默认是None，
        sigma: 标的资产年化波动率，默认是None，
        r: 无风险利率，默认为None，
        q: 标的资产分红率，默认为None。
    """


    def __init__(
        self,
        s0: float = None,
        sigma: float = None,
        r: float = None,
        q: float = None
    ) -> None:
        """构造函数，定义标的资产的参数"""
        self.s0: float = s0
        self.sigma: float = sigma
        self.r: float = r
        self.q: float = q
        if r and q:
            self.drift: float = self.r - self.q
        self.autocalls: Dict[str, type] = {}

    def set_underlying_parameters(
        self,
        s0: float,
        sigma: float,
        r: float,
        q: float
    ) -> None:
        """设置标的资产参数"""
        self.s0: float = s0
        self.sigma: float = sigma
        self.r: float = r
        self.q: float = q
        self.drift: float = self.r - self.q


    def add_autocall(
        self,
        autocall_class: type,
        autocall_setting: dict
    ) -> None:
        """往引擎增加autocall"""
        self.autocall = autocall_class(autocall_setting)
        self.autocalls[autocall_class.name] = self.autocall

    def mc_pricing(
        self,
        n_path: int = 300000,
    ) -> float:
        """蒙特卡洛定价"""

        # 生成标的路径
        tstep = self.autocall.time_to_maturity * 252
        dt = self.autocall.time_to_maturity / tstep
        z = cp.random.normal(size=(tstep + 1, n_path))
        st = cp.zeros((tstep + 1, n_path))
        st[0] = self.s0
        for t in range(1, tstep + 1):
            st[t] = st[t - 1] * cp.exp(
                (self.drift - 0.5 * self.sigma ** 2) * dt
                + self.sigma * cp.sqrt(dt) * z[t]
                )

        # 先考虑敲出场景
        # 生成和观察日有关的网格
        knock_out_scenario = cp.tile(self.autocall.view_day, (n_path, 1)).T
        knock_out_scenario = cp.where(
            st[self.autocall.view_day] > self.autocall.knock_out_level,
            knock_out_scenario,
            cp.inf
            )
        # 记录每条路径的具体敲出日，如果无敲出则保留inf
        knock_out_date = np.min(knock_out_scenario, axis=0)
        is_knock_out = knock_out_date != np.inf
        not_knock_out = knock_out_date == np.inf
        knock_out_year = knock_out_date[is_knock_out] / 252  # 把天化为年
        knock_out_profit = np.sum(
            knock_out_year
            * self.autocall.coupon_rate
            * self.s0
            * np.exp(-self.r * knock_out_year)
            )  # 把payoff先折现再求和,计算敲出总所入

        # 下面考虑不敲出的情形，分为曾经敲入过和从未敲入过
        # 判断某一条路径是否有敲入
        knock_in_scenario = np.any(st < self.autocall.knock_in_level, axis=0)
        # 持有到期，没有敲入也没有敲出
        hold_to_maturity = (knock_in_scenario == False) & not_knock_out
        # 平稳持有到期路径条数
        hold_to_maturity_count = np.count_nonzero(hold_to_maturity)
        hold_to_maturity_profit = hold_to_maturity_count\
        * self.autocall.coupon_rate\
        * self.s0\
        * np.exp(-self.r * self.autocall.time_to_maturity)  # 平稳持有到期收入
        loss = np.sum(
            (st[
                -1,
                not_knock_out
                & (knock_in_scenario == True)
                & (st[-1] < self.s0)
                ] / self.s0 - 1)
            * self.s0
            * np.exp(-self.r * self.autocall.time_to_maturity)
            )  # 敲入造成的总亏损，对于st>s0的情况，损益为0，不需要考虑
        price = (hold_to_maturity_profit + knock_out_profit + loss) / n_path
        return price

    def mc_delta(self) -> float:
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
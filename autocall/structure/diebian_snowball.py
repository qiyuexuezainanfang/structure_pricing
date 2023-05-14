from typing import Dict

from . import EarlyCouponSnowBall


class DiebianSnowBall(EarlyCouponSnowBall):
    """蝶变雪球

    在早利雪球的基础上，敲出票息分几个阶段逐级降低

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '蝶变雪球'

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义蝶变雪球的参数"""
        super().__init__(setting)

    def _set_coupon_rate(self) -> None:
        """生成敲出票息率列表"""
        self.new_coupon_rate = []

        for i in range(len(self.coupon_rate) - 1):
            pre_item = self.coupon_rate[i]
            next_item = self.coupon_rate[i + 1]
            self.new_coupon_rate.extend(
                [pre_item[1]] * (next_item[0] - pre_item[0]))
        self.new_coupon_rate.extend(
            [next_item[1]] * (len(self.knock_out_view_day) - next_item[0]))
        self.coupon_rate = self.new_coupon_rate

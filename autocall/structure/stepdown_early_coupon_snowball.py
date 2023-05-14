from typing import Dict

from . import StepDownSnowBall


class StepDownEarlyCouponSnowBall(StepDownSnowBall):
    """双降雪球

    票息和敲出点位同时变，在降敲的基础上，敲出票息逐级下降

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '双降雪球'

    # params = [
    #     'knock_in_level',
    #     'knock_out_level',
    #     'coupon_rate',
    #     'coupon_div',
    #     'knock_out_view_day',
    #     'time_to_maturity'
    # ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义双降雪球的参数"""
        super().__init__(setting)
        self._set_coupon_rate()

    def _set_coupon_rate(self) -> None:
        """生成敲出票息列表"""
        self.new_coupon_rate = []
        for i in range(len(self.coupon_rate) - 1):
            pre_item = self.coupon_rate[i]
            next_item = self.coupon_rate[i + 1]
            self.new_coupon_rate.extend(
                [pre_item[1]] * (next_item[0] - pre_item[0]))
        self.new_coupon_rate.extend(
            [next_item[1]] * (len(self.knock_out_view_day) - next_item[0]))
        self.coupon_rate = self.new_coupon_rate

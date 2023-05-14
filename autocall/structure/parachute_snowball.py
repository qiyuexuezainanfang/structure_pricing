from typing import Dict

from . import StepDownSnowBall


class ParachuteSnowBall(StepDownSnowBall):
    """降落伞雪球

    票息不变，敲出点位最后一个月下跳，
    其他参数跟经典雪球一样。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '降落伞雪球'

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义降落伞雪球的参数"""
        super().__init__(setting)

    def _set_knock_out_level(self) -> None:
        """生成敲出水平列表"""
        self.new_knock_out_level = []
        high_knock_out_level = self.knock_out_level[0]
        low_knock_out_level = self.knock_out_level[1]
        self.new_knock_out_level.extend(
            [high_knock_out_level] * (len(self.knock_out_view_day) - 1))
        self.new_knock_out_level.append(low_knock_out_level)
        self.knock_out_level = self.new_knock_out_level

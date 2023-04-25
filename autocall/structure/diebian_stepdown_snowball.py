from typing import Dict

from . import StepDownSnowBall


class DiebianStepDownSnowBall(StepDownSnowBall):
    """次年双降雪球

    敲出票息随时间推移逐级降低，敲出点位从第二年开始随时间逐步下调。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '次年双降雪球'

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义次年双降雪球的参数"""
        super.__init__(setting)

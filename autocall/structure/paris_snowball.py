from typing import Dict, List

from . import OriginalSnowBall


class ParisSnowBall(OriginalSnowBall):
    """巴黎雪球

    票息不变，敲出点位随时间（每月）逐步下调，
    其他参数跟经典雪球一样。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
        knock_in_times: 累积敲入次数
        knock_in_view_day: 敲入观察日（改为每月）
    """

    name = '巴黎雪球'

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity',
        'knock_in_times',
        'knock_in_view_day'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义降敲雪球的参数"""
        super.__init__(setting)

        # 敲入观察日如果不是一个列表，则生成敲入观察日列表，每月一次
        if not isinstance(self.knock_in_view_day, list):
            self._set_knock_in_view_day(setting)

    def _set_knock_in_view_day(self, setting) -> None:
        self.knock_in_view_day: List[int] = [
            i*21-1 for i in range(
                1,
                setting['time_to_maturity'] * 12 + 1
                )
            ]

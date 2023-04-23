from typing import List, Dict

import numpy as np

from .. import AutocallTemplate


class StepDownSnowBall(AutocallTemplate):
    """降敲雪球

    票息不变，敲出点位随时间（每月）逐步下调。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        coupon_div: 红利率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
    """

    name = '降敲雪球'

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'time_to_maturity'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义降敲雪球的参数"""

        # 先检查本结构所需要的参数有没有被传入
        for param in self.params:
            if param not in setting.keys():
                print(f'缺少{param}参数')
                return

        super().__init__(setting)

        # 生成敲出观察日列表
        self.knock_out_view_day: List[int] = [
            i*21-1 for i in range(
                1,
                setting['time_to_maturity'] * setting['knock_out_view_day'] + 1
                )
            ]

        # 生成敲出水平列表
        self.knock_out_level = np.linspace(
            self.knock_out_level,
            self.knock_in_level,
            len(self.knock_out_view_day)
            )

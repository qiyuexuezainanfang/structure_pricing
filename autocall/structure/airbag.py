from typing import Dict

from .. import AutocallTemplate


class Airbag(AutocallTemplate):
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

        # 先检查本结构所需要的参数有没有被传入
        for param in self.params:
            if param not in setting.keys():
                print(f'缺少{param}参数')
                return

        # 再检查传入的参数是否多余
        for param in setting.keys():
            if param not in self.params:
                del setting[param]

        super().__init__(setting)

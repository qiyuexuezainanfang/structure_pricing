from abc import ABC
from typing import Dict


class AutocallTemplate(ABC):
    """autocall的基类，具体的结构需要先继承它。

    基类确定了autocall大类结构的设计模板。任何一种具体的结构，如经典/降敲/早利等，
    都基于该模板，定义相应的payoff形式、敲入敲出边界等参数，
    除此以外子类还可以调用_set..方法来进行参数列表的生成,
    本基类不能直接被实例化。

    属性:
        knock_in_level: 敲入水平，float or list，
        knock_out_level: 敲出水平，float or list，
        coupon_rate: 敲出票息率，float or list，
        coupon_div：红利票息率，float
        knock_out_view_day：敲出观察日，list，
        knock_in_view_day：敲入观察日，list，
        time_to_maturity：续存期，
        protected_level：保本率，
        strike_after_knock_in：敲入后行权价，
        participation_rate_no_knock_in：未敲入参与率，
        participation_rate_knock_in：敲入参与率，
        reset_time：重置敲出期，某个时间点之后，
        reset_knock_out_level：重置敲出水平，
        reset_coupon：重置票息，
        knock_in_times：累积敲入次数
    """

    params = [
        'knock_in_level',
        'knock_out_level',
        'coupon_rate',
        'coupon_div',
        'knock_out_view_day',
        'knock_in_view_day',
        'time_to_maturity',
        'protected_level',
        'strike_after_knock_in',
        'participation_rate_no_knock_in',
        'participation_rate_knock_in',
        'reset_time',
        'reset_knock_out_level',
        'reset_coupon',
        'knock_in_times'
    ]

    def __init__(self, setting: Dict[str, float]) -> None:
        """构造函数，定义autocall结构大类的参数"""

        # 当传入的参数属于autocall类变量，就创建它
        for param in setting.keys():
            if param in self.params:
                setattr(self, param, setting[param])

    # 以下方法在子类中如有需要可以实现，主要用来生成某种规则的参数列表
    def _set_knock_in_level(self) -> None:
        pass

    def _set_knock_out_level(self) -> None:
        pass

    def _set_coupon_rate(self) -> None:
        pass

    def _set_coupon_div(self) -> None:
        pass

    def _set_knock_out_view_day(self) -> None:
        pass

    def _set_knock_in_view_day(self) -> None:
        pass

    def _set_time_to_maturity(self) -> None:
        pass

    def _set_protected_level(self) -> None:
        pass

    def _set_strike_after_knock_in(self) -> None:
        pass

    def _set_participation_rate_no_knock_in(self) -> None:
        pass

    def _set_participation_rate_knock_in(self) -> None:
        pass

    def _set_reset_time(self) -> None:
        pass

    def _set_reset_knock_out_level(self) -> None:
        pass

    def _set_reset_coupon(self) -> None:
        pass

    def _set_knock_in_times(self) -> None:
        pass

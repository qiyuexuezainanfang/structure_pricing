from . import OriginalSnowBall


class Booster(OriginalSnowBall):
    """助推器

    既通过上涨参与率放大上涨收益，又可提供下跌保护

    属性:
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
        participation_rate_no_knock_in: 上涨参与率
        protected_level: 保本率
    """

    name = '助推器'

    params = [
        'knock_out_level',
        'coupon_rate',
        'knock_out_view_day',
        'time_to_maturity',
        'participation_rate_no_knock_in',
        'protected_level'
    ]

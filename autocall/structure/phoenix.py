from . import FCN


class Phoenix(FCN):
    """凤凰式雪球

    只要当月未敲入，则可领取票息，敲出则提前结束。

    属性:
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
        knock_in_level: 敲入水平
    """

    name = '凤凰式雪球'

    params = [
        'knock_out_level',
        'coupon_rate',
        'knock_out_view_day',
        'time_to_maturity',
        'knock_in_level'
    ]

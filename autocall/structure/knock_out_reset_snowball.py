from . import OriginalSnowBall


class KnockOutResetSnowBall(OriginalSnowBall):
    """救生艇雪球

    在特定的时间窗口内发生敲入后可重置（下调）敲出水平。

    属性:
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        knock_in_level: 敲入水平，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
        strike_after_knock_in: 敲入后行权价
        reset_time: 重置敲出期/某个日期之后
        reset_knock_out_level: 重置敲出水平
        reset_coupon: 重置敲出票息
    """

    name = '救生艇雪球'

    params = [
        'knock_out_level',
        'coupon_rate',
        'knock_out_view_day',
        'time_to_maturity',
        'strike_after_knock_in',
        'reset_time',
        'reset_knock_out_level',
        'reset_coupon'
    ]

from . import OriginalSnowBall


class FCN(OriginalSnowBall):
    """FCN

    不含敲入条款，续存期间每月敲出观察日自动派息，直至发生敲出，
    到期时能收回本金和固定票息，或是以较低的价格用本金认购标的。

    属性:
        knock_out_level: 敲出水平，默认为1，即标的初始价格S0水平，
        coupon_rate: 敲出票息率，
        knock_out_view_day: 敲出观察日，默认1年观察12次，
        time_to_maturity: 续存期，默认为1年
        strike_after_knock_in: 敲入后行权价
    """

    name = 'FCN'

    params = [
        'knock_out_level',
        'coupon_rate',
        'knock_out_view_day',
        'time_to_maturity',
        'strike_after_knock_in'
    ]

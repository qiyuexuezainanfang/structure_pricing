from . import OriginalSnowBall


class TongxinSnowBall(OriginalSnowBall):
    """同鑫结构

    持有期限固定，不可提前赎回；持有期限未敲入则按照固定收益结算，
    触发敲入的话，损益为标的资产涨跌幅。

    属性:
        knock_in_level: 敲入水平，默认为1，即标的初始价格S0水平，
        coupon_div: 固定收益率，
        time_to_maturity: 续存期，默认为1年，
        participation_rate_knock_in: 敲入后参与率
    """

    name = '同鑫结构'

    params = [
        'knock_in_level',
        'coupon_div',
        'time_to_maturity',
        'participation_rate_knock_in'
    ]

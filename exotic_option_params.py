# 期权的全部结构参数都在这里设置，且只在这里设置

OriginalSnowBall_params = {
        'knock_in_level': 85,
        'knock_out_level': 103,
        'coupon_rate': 0.3,
        'coupon_div': 0.3,
        'knock_out_view_day': 12,  # int表示一年观察次数
        'time_to_maturity': 1  # float，只能支持1/12的倍数
}

StepDownSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': [(0, 1.03), (3, 0.9), (9, 0.8)],  # 月份，敲出水平。
        'coupon_rate': 0.3,
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1
}

ProtectedSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': 1.03,
        'coupon_rate': 0.3,
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1,
        'protected_level': 0.9
}

KiUpSnowBall_params = {
        'knock_in_level': [(0, 0.7), (100, 0.8), (200, 0.9)],  # 日，敲入。
        'knock_out_level': 1.03,
        'coupon_rate': 0.3,
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1
}

CouponSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': 1.03,
        'coupon_rate': 0.3,
        'coupon_div': 0.15,
        'knock_out_view_day': 12,
        'time_to_maturity': 1
}

EarlyCouponSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': 1.03,
        'coupon_rate': [0.3, 0.2],  # 第一年高，之后变低
        'coupon_div': 0.15,
        'knock_out_view_day': 12,
        'time_to_maturity': 2  # float,大于1
}

StepDownEarlyCouponSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': [(0, 1.03), (3, 0.9), (9, 0.8)],
        'coupon_rate': [(0, 0.3), (3, 0.2), (9, 0.15)],
        'coupon_div': 0.15,
        'knock_out_view_day': 12,
        'time_to_maturity': 1
}

OTMSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': 1.03,
        'coupon_rate': 0.3,
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1,
        'strike_after_knock_in': 0.9  # 在s0和knock_in_level之间
}

EuropeanSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': 1.03,
        'coupon_rate': 0.3,
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1
}

ParachuteSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': [1.03, 1.01],  # 最后一个月敲出点位下跳
        'coupon_rate': 0.3,
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1
}

EnhancedSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': 1.03,
        'coupon_rate': 0.3,
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1,
        'participation_rate_no_knock_in': 0.5
}

FCN_params = {
        'knock_out_level': None,
        'coupon_rate': None,
        'knock_out_view_day': None,
        'time_to_maturity': None,
        'strike_after_knock_in': None
}

Phoenix_params = {
        'knock_out_level': None,
        'coupon_rate': None,
        'knock_out_view_day': None,
        'time_to_maturity': None,
        'knock_in_level': None
}

KnockOutResetSnowBall_params = {
        'knock_out_level': None,
        'coupon_rate': None,
        'knock_out_view_day': None,
        'time_to_maturity': None,
        'reset_time': None,
        'reset_knock_out_level': None,
        'reset_coupon': None
}

AutocallNote_params = {
        'knock_out_level': 1.03,
        'coupon_rate': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1,
        'coupon_div': 0.15
}

ParisSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None,
        'knock_in_times': None,
        'knock_in_view_day': None
}

DiebianSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': 1.03,
        'coupon_rate': [(0, 0.3), (3, 0.2), (9, 0.15)],
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1
}

BearishSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
}

DiebianParachuteSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': [1.03, 1.01],
        'coupon_rate': [(0, 0.3), (3, 0.2), (9, 0.15)],
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1
}

EuropeanDiebianSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': 1.03,
        'coupon_rate': [(0, 0.3), (3, 0.2), (9, 0.15)],
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1
}

DiebianStepDownSnowBall_params = {
        'knock_in_level': 0.85,
        'knock_out_level': [(0, 1.03), (12, 0.9), (15, 0.8)],  # 第二年开始降
        'coupon_rate': [(0, 0.3), (3, 0.2), (9, 0.15)],
        'coupon_div': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 2  # 大于1
}

Airbag_params = {
        'knock_in_level': 0.85,
        'participation_rate_no_knock_in': 0.5,
        'participation_rate_knock_in': 0.3,
        'time_to_maturity': 1
}

Booster_params = {
        'knock_out_level': 1.03,
        'coupon_rate': 0.3,
        'knock_out_view_day': 12,
        'time_to_maturity': 1,
        'participation_rate_no_knock_in': 0.5,
        'protected_level': 0.9
}

TongxinSnowBall_params = {
        'knock_in_level': None,
        'coupon_div': None,
        'time_to_maturity': None,
        'participation_rate_knock_in': None
}

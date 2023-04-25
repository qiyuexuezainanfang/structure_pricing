# 期权的全部结构参数都在这里设置，且只在这里设置

OriginalSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,  # int表示一年观察次数，list[int]表示具体观察列表
        'time_to_maturity': None  # float，只能支持1/12的倍数
}

StepDownSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,  # list[float] or list[tuple(float, float)]
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
}

ProtectedSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None,
        'protected_level': None
}

KiUpSnowBall_params = {
        'knock_in_level': None,  # list[float] or list[tuple(float, float)]
        'knock_out_level': None,
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
}

CouponSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
}

EarlyCouponSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,  # tuple(float, float)
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None  # float,大于1
}

StepDownEarlyCouponSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,  # list[float] or list[tuple(float, float)]
        'coupon_rate': None,  # list[float] or list[tuple(float, float)]
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
}

OTMSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None,
        'strike_after_knock_in': None
}

EuropeanSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
}

ParachuteSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,  # tuple(float, float)
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
}

EnhancedSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None,
        'participation_rate_no_knock_in': None
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
        'knock_out_level': None,
        'coupon_rate': None,
        'knock_out_view_day': None,
        'time_to_maturity': None,
        'coupon_div': None
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
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,  # list[float] or list[tuple(float, float)]
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
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
        'knock_in_level': None,
        'knock_out_level': None,  # tuple(float, float)
        'coupon_rate': None,  # list[float] or list[tuple(float, float)]
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
}

EuropeanDiebianSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,
        'coupon_rate': None,  # list[float] or list[tuple(float, float)]
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None
}

DiebianStepDownSnowBall_params = {
        'knock_in_level': None,
        'knock_out_level': None,  # list[tuple(float, float)]
        'coupon_rate': None,  # list[float] or list[tuple(float, float)]
        'coupon_div': None,
        'knock_out_view_day': None,
        'time_to_maturity': None  # 大于1
}

Airbag_params = {
        'knock_in_level': None,
        'participation_rate_no_knock_in': None,
        'participation_rate_knock_in': None,
        'time_to_maturity': None
}

Booster_params = {
        'knock_out_level': None,
        'coupon_rate': None,
        'knock_out_view_day': None,
        'time_to_maturity': None,
        'participation_rate_no_knock_in': None,
        'protected_level': None
}

TongxinSnowBall_params = {
        'knock_in_level': None,
        'coupon_div': None,
        'time_to_maturity': None,
        'participation_rate_knock_in': None
}

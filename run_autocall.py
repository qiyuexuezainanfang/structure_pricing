from typing import Dict, List

from autocall.structure import OriginalSnowBall
from autocall import PricingEngine

# autocall_structure
autocall_structure: List[type] = [
    OriginalSnowBall
]

# underlying_parameters
underlying_params: Dict[str, float] = {
    's0': 100,
    'sigma': 0.2,
    'r': 0.0,
    'q': 0.0
}

# autocall_parameters
autocall_params: Dict[str, float] = {
    'knock_in_level': 0.85,
    'knock_out_level': 1.03,
    'coupon_rate': 0.2,
    'coupon_div': 0.2,
    'knock_out_view_day': 12,
    'knock_in_view_day': 252,
    'time_to_maturity': 1,
    'protected_level': None,
    'strike_after_knock_in': None,
    'participation_rate_no_knock_in': None,
    'participation_rate_knock_in': None,
    'reset_time': None,
    'reset_knock_out_level': None,
    'reset_coupon': None,
    'knock_in_times': None
}


def main():
    engine = PricingEngine()  # 实例化定价引擎
    engine.set_underlying_parameters(underlying_params)  # 设置标的资产参数

    for structure in autocall_structure:  # 往定价引擎添加不同的autocall结构
        engine.add_autocall(structure, autocall_setting=autocall_params)

    for structure in engine.autocalls.keys():  # 对每种结构进行定价
        autocall_value = engine.mc_pricing()
        print(f"{structure}价格：{autocall_value}")


if __name__ == "__main__":
    main()

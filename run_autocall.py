from typing import Dict, List

from autocall.structure import *
from autocall import PricingEngine
from exotic_option_params import *
from judge_option_params import judge_option_params

# 可以进行定价的结构，用户根据需要进行选择，可多选
autocall_structure: List[type] = [
    # OriginalSnowBall,
    # StepDownSnowBall,
    # ProtectedSnowBall,
    # KiUpSnowBall,
    # CouponSnowBall,
    # EarlyCouponSnowBall,
    # StepDownEarlyCouponSnowBall,
    # OTMSnowBall,
    # EuropeanSnowBall,
    # ParachuteSnowBall,
    # EnhancedSnowBall,
    # FCN,
    # Phoenix,
    # KnockOutResetSnowBall,
    # AutocallNote,
    # ParisSnowBall,
    # DiebianSnowBall,
    # DiebianParachuteSnowBall,
    # EuropeanDiebianSnowBall,
    # DiebianStepDownSnowBall,
    # Airbag,
    # Booster,
    # TongxinSnowBall,
    # BearishSnowBall
]

# underlying_parameters
underlying_params: Dict[str, float] = {
    's0': 100,
    'sigma': 0.2,
    'r': 0.0,
    'q': 0.0
}


def main():
    engine = PricingEngine()  # 实例化定价引擎
    engine.set_underlying_parameters(underlying_params)  # 设置标的资产参数

    for structure in autocall_structure:  # 往定价引擎添加不同的autocall结构
        # 先判断期权结构参数输入是否正确
        judge_option_params(structure, eval(structure.__name__ + '_params'))
        engine.add_autocall(structure, eval(structure.__name__ + '_params'))

    for structure in engine.autocalls.keys():  # 对每种结构进行定价
        autocall_value = engine.mc_pricing()
        print(f"{structure}价格：{autocall_value}")


if __name__ == "__main__":
    main()

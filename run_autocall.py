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
    Booster,
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
    for structure in autocall_structure:  # 检查奇异期权结构参数输入是否服从规则
        judge_option_params(structure, eval(structure.__name__ + '_params'))

    # 先添加autocall结构，并对每个结构进行实例化
    autocalls: Dict[str, type] = {}
    for structure in autocall_structure:
        autocall = structure(eval(structure.__name__ + '_params'))
        autocall.set_underlying_parameters(underlying_params)
        autocalls[structure.name] = autocall

    # 定价
    for name, autocall in autocalls.items():
        value = autocall.mc_pricing()
        print(f"{name}价格：{value}")


if __name__ == "__main__":
    main()

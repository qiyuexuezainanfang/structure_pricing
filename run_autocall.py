from typing import Dict

from autocall.structure import OriginalSnowBall
from autocall import PricingEngine

# underlying_parameters
underlying_params: Dict[str, float] = {
    's0': 100,
    'sigma': 0.2,
    'r': 0.0,
    'q': 0.0
}

# 

def main():

    engine = PricingEngine()
    engine.set_underlying_parameters(**underlying_params)
    engine.add_autocall(OriginalSnowBall, autocall_setting={})
    autocall_value = engine.mc_pricing()
    print(f"{OriginalSnowBall.__name__}'s value is {autocall_value}")


if __name__ == "__main__":
    main()
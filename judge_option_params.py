from typing import List, Tuple, Dict


def judge_option_params(autocall_class: type, params: Dict) -> None:
    """期权结构参数识别

    对autocall大类下不同的期权结构，输入的参数有略微差异，
    因此在添加到定价引擎之前，需要先检查输入的参数是否有问题。

    参数：
        autocall_class: 准备定价的期权结构类
        params: 用户输入的参数字典

    返回：
        空值

    """
    if autocall_class.name == '经典雪球':
        if not (
            isinstance(params['knock_out_view_day'], int)
                ):
            print('经典雪球参数输入不合规范')
            exit(1)

    elif autocall_class.name == '降敲雪球':
        if not (
            isinstance(params['knock_out_level'], List) and
                isinstance(params['knock_out_level'][0], Tuple)):
            print('降敲雪球参数输入不合规范')
            exit(1)

    elif autocall_class.name == 'KI递增雪球':
        if not (
            isinstance(params['knock_in_level'], List) and
                isinstance(params['knock_in_level'][0], Tuple)):
            print('KI递增雪球参数输入不合规范')
            exit(1)

    elif autocall_class.name == '早利雪球':
        if not (
            isinstance(params['coupon_rate'], List) and
                (len(params['coupon_rate']) == 2)):
            print('早利雪球参数输入不合规范')
            exit(1)
        elif params['time_to_maturity'] <= 1:
            print('续存期不能低于一年')
            exit(1)

    elif autocall_class.name == '双降雪球':
        if not (
            isinstance(params['knock_out_level'], List) and
                isinstance(params['knock_out_level'][0], Tuple)):
            print('双降雪球参数输入不合规范')
            exit(1)
        elif not (
            isinstance(params['coupon_rate'], List) and
                isinstance(params['coupon_rate'][0], Tuple)):
            print('双降雪球参数输入不合规范')
            exit(1)

    elif autocall_class.name == 'OTM雪球':
        if not (
            params['knock_in_level'] < params['strike_after_knock_in'] < 1
                ):
            print('OTM雪球参数输入不合规范')
            exit(1)

    elif autocall_class.name == '降落伞雪球':
        if not (
            isinstance(params['knock_out_level'], List) and
                (len(params['knock_out_level']) == 2)):
            print('降落伞雪球参数输入不合规范')
            exit(1)

    elif autocall_class.name == '蝶变雪球':
        if not (
            isinstance(params['coupon_rate'], List) and
                isinstance(params['coupon_rate'][0], Tuple)):
            print('蝶变雪球参数输入不合规范')
            exit(1)

    elif autocall_class.name == '蝶变浮力雪球':
        if not (
            isinstance(params['coupon_rate'], List) and
                isinstance(params['coupon_rate'][0], Tuple)):
            print('蝶变浮力雪球参数输入不合规范')
            exit(1)
        elif not (
            isinstance(params['knock_out_level'], List) and
                (len(params['knock_out_level']) == 2)):
            print('蝶变浮力雪球参数输入不合规范')
            exit(1)

    elif autocall_class.name == '欧式蝶变雪球':
        if not (
            isinstance(params['coupon_rate'], List) and
                isinstance(params['coupon_rate'][0], Tuple)):
            print('欧式蝶变雪球参数输入不合规范')
            exit(1)

    elif autocall_class.name == '次年双降雪球':
        if not (
            isinstance(params['coupon_rate'], List) and
                isinstance(params['coupon_rate'][0], Tuple)):
            print('次年双降雪球敲出票息参数输入不合规范')
            exit(1)
        elif not (
            isinstance(params['knock_out_level'], List) and
                isinstance(params['knock_out_level'][0], Tuple)):
            print('次年双降雪球敲出水平参数输入不合规范')
            exit(1)
        elif not (
            params['knock_out_level'][0][0] == 0 and
                params['knock_out_level'][1][0] == 12):
            print('次年双降雪球敲出水平参数输入不合规范')
            exit(1)
        elif params['time_to_maturity'] <= 1:
            print('次年双降雪球敲出水平参数输入不合规范')
            exit(1)

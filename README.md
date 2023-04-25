# autocall_pricing
## 项目概述

本项目是“场外百科”小程序期权结构的配套定价库，提供基于GPU的蒙特卡洛定价法和有限差分定价法，可以为奇异期权估值并且计算相应的希腊字母。


## 文件构成

项目核心是autocall文件夹、exotic_option_params.py文件、judge_option_params.py文件、run_autocall.py文件。具体如下：

1、autocall文件夹包含structure子文件夹、autocall_base.py文件和pricing_enging.py文件。其中structure子文件夹是不同的期权结构，autocall_base.py文件是一切autocall期权结构的基类，pricing_engine是定价引擎。

2、exotic_option_params.py文件内含每一种奇异期权结构的参数设置

3、judge_option_params.py文件内的函数用来判断用户输入的参数是否与结构要求相一致

4、run_autocall.py文件是主程序


## 使用步骤

1、用户事先在exotic_option_params.py文件中设置好相应的期权结构参数，可设置多种结构。
2、在run_autocall.py文件中把需要研究的期权结构类注释取消掉，可同时对多种结构进行定价。
3、运行run_autocall.py文件，得到每一种期权结构的估值或希腊字母。


## 附注
本项目可继续扩展更多期权结构，开发步骤为：
1、根据autocall_base基类，设计相应的期权结构，生成一个对应的.py文件
2、在__init__函数中导入该期权类
3、在run_autocall.py主程序中把该类的名字补充上去，
4、在exotic_option_params.py文件中把输入的参数字典补上
5、在judge_option_params.py文件末尾通过增加elif的方式扩充函数
# exotic_option_pricing
## 项目概述

本项目是“场外百科”小程序期权结构的配套定价库，提供基于cupy/numpy的蒙特卡洛定价法和有限差分定价法，可以为奇异期权估值并且计算相应的希腊字母。


## 文件构成

项目核心是autocall文件夹、exotic_option_params.py文件、judge_option_params.py文件、run_autocall.py文件。具体如下：

1、autocall文件夹包含structure子文件夹、autocall_base.py文件和pricing_enging.py文件。其中structure子文件夹是不同的期权结构定义，autocall_base.py文件是一切autocall期权结构的基类，pricing_engine是定价引擎。

2、exotic_option_params.py文件内含每一种奇异期权结构的参数设置

3、judge_option_params.py文件内的函数用来判断用户输入的参数是否与结构要求相一致

4、run_autocall.py文件是主程序


## 使用说明

1、用户事先在exotic_option_params.py文件中设置好需要进行定价的期权结构参数，可同时设置多种结构。

2、在run_autocall.py主程序文件中的autocall_structure列表，把需要定价的期权结构类注释取消掉，剩下不需要定价的结构类依然保持被注释的状态。假设要同时对多种结构进行定价，则把这些结构的注释同时取消掉。

3、在run_autocall.py主程序文件中的underlying_params列表设置标的资产参数。

4、运行run_autocall.py文件，得到每一种期权结构的估值或希腊字母。


## 源码剖析

run_autocall.py文件具体代码运行逻辑如下：

1、首先从structure导入结构类，然后从exotic_option_params导入用户事先定义好的期权结构参数，最后导入judge_option_params函数（该函数用来判断用户输入的期权结构参数是否符合规范）。

2、autocall_structure中保留那些需要定价的结构类，underlying_params定义标的参数。

3、运行main()函数，首先遍历所有需要定价的期权结构，检查参数输入是否符合规范，如果符合则继续运行程序，不符合将会报错并且退出程序；对每个期权结构类进行实例化，设置标的参数；最后对每个期权结构对象调用mc_pricing函数进行定价。


## PricingEngine、AutocallTemplate类和structure具体结构类的关系

1、PricingEngine是定价引擎基类，AutocallTemplate是期权结构基类，一切structure的具体结构实现都需要同时继承这两个基类（或者继承那些已经实现的具体结构，多重继承），要写name和params，覆盖掉父类的名字和参数（如果参数和父类完全一样可以不写）。当某个具体结构类进行实例化之后，调用mc_pricing之后，将会调用PricingEngine父类的mc_pricing函数进行定价。

2、除此以外AutocallTemplate类当中有很多_set开头的函数，这些函数可以在子类当中被重载实现（如果有需要的话），比如降敲雪球，用户输入的是List[Tuple]，但是实际上需要变成一个List[float]，因此需要重新定义父类的_set_knock_out_level函数，生成敲出水平列表，在降敲雪球被实例化的时候，通过__init__函数调用_set_knock_out_level进行敲出水平列表的设置。

3、PricingEngine的函数也可以在子类中进行重载实现。比如Dongfang结构类、OTM雪球的payoff计算方法有一些特殊，则可以在子类中进行重新定义_cal_loss等函数。


## 扩展步骤
本项目可继续扩展更多期权结构，步骤为：

1、根据autocall_base基类，设计相应的期权结构，生成一个对应的.py文件

2、在__init__.py文件中导入该期权类

3、在run_autocall.py主程序中把该类的名字补充上去，

4、在exotic_option_params.py文件中把输入的参数字典补上

5、在judge_option_params.py文件末尾通过增加elif的方式扩充函数

6、运行run_autocall.py文件进行定价
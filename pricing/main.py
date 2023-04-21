import numpy as np
import cupy as cp
import timeit
from typing import List

#参数设置
s0: float = 100
knock_in: float = 90 #敲入水平
knock_out: float = 100#敲出水平
N: int = 252 #一年的交易日
view_day: List[int] = [i*21-1 for i in range(1,13)] #敲出观察日
T: int = 1 #时间是一年
coupon_rate: float = 0.2 #票息率

def simulate_mc():
    tstep, npath = 252, 1000000
    s0 = 100
    r = 0.05
    sigma = 0.2
    T = 1
    dt = T / tstep
    z = np.random.normal(size = (tstep + 1, npath))
    path = np.zeros((tstep + 1, npath))
    path[0] = s0
    for t in range(1, tstep + 1):
        path[t] = path[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z[t])
    return path

def cp_np_simulate_mc():
    tstep, npath = 252, 1000000
    s0 = 100
    r = 0.05
    sigma = 0.2
    T = 1
    dt = T / tstep
    z = cp.random.normal(size = (tstep + 1, npath))
    path = cp.zeros((tstep + 1, npath))
    path[0] = s0
    for t in range(1, tstep + 1):
        path[t] = path[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z[t])
    return path

def cp_simulate_mc():
    tstep, npath = 252, 300000
    s0 = 100
    r = 0.05
    sigma = 0.2
    T = 1
    dt = T / tstep
    z = cp.random.normal(size = (tstep + 1, npath))
    st = cp.zeros((tstep + 1, npath))
    st[0] = s0
    for t in range(1, tstep + 1):
        st[t] = st[t - 1] * cp.exp((r - 0.5 * sigma ** 2) * dt + sigma * cp.sqrt(dt) * z[t])
    return st

def complete_cp_simulate_mc():
    tstep, npath = 252, 300000
    s0 = 100
    r = 0
    sigma = 0.16
    q = 0
    drift = r - q
    T = 1
    dt = T / tstep
    z = cp.random.normal(size = (tstep + 1, npath))
    st = cp.zeros((tstep + 1, npath))
    st[0] = s0
    for t in range(1, tstep + 1):
        st[t] = st[t - 1] * cp.exp((drift - 0.5 * sigma ** 2) * dt + sigma * cp.sqrt(dt) * z[t])
    #先考虑敲出场景

    knock_out_scenario = cp.tile(view_day, (300000,1)).T  #先生成和观察日有关的网格
    knock_out_scenario = cp.where(st[view_day] > knock_out, knock_out_scenario, cp.inf)  #敲出的时候，记录下观察日
    knock_out_date = np.min(knock_out_scenario, axis=0) #每列最小的数，精确记录每条路径的具体敲出日，如果无敲出则保留inf
    knock_out_month = (knock_out_date + 1) / 21 #每条路径分别第几个月敲出
    is_knock_out = knock_out_month != np.inf
    not_knock_out = knock_out_month == np.inf
    knock_out_year = knock_out_month[is_knock_out] / 12 #把月份化为年
    knock_out_profit = np.sum(knock_out_year * coupon_rate * np.exp(-r * knock_out_year)) #把payoff先折现再求和,计算敲出总所入
    #下面考虑不敲出的情形，分为曾经敲入过和从未敲入过
    knock_in_scenario = np.any(st < knock_in, axis=0) #判断某一条路径是否有敲入
    hold_to_maturity = (knock_in_scenario == False) & not_knock_out #持有到期，没有敲入也没有敲出
    hold_to_maturity_count = np.count_nonzero(hold_to_maturity) #平稳持有到期路径条数
    htm_profit = hold_to_maturity_count * coupon_rate * np.exp(-r * T) #平稳持有到期收入
    loss = np.sum((st[-1, not_knock_out & (knock_in_scenario == True) & (st[-1] < s0)] / s0 - 1) * np.exp(-r * T)) #敲入造成的总亏损，对于st>s0的情况，损益为0，不需要考虑
    price = (htm_profit + knock_out_profit + loss)/300000
    return price

def cp_simulate_mc_cum():
    tstep, npath = 252, 1000000
    s0 = 100
    r = 0.05
    sigma = 0.2
    T = 1
    dt = T / tstep
    z = cp.random.normal(size = (tstep + 1, npath))
    path = s0 * cp.cumprod(cp.exp((r - 0.5 * sigma ** 2) * dt + sigma * cp.sqrt(dt) * z), 0)
    path[0] = s0
    return path



if __name__ == '__main__':
    # t1 = timeit.timeit('simulate_mc()', setup='from __main__ import simulate_mc', number=1)
    # t2 = timeit.timeit('cp_np_simulate_mc()', setup='from __main__ import cp_np_simulate_mc', number=1)
    # t3 = timeit.timeit('cp_simulate_mc()', setup='from __main__ import cp_simulate_mc', number=1)
    t4 = timeit.timeit('complete_cp_simulate_mc()', setup='from __main__ import complete_cp_simulate_mc', number=1)
    # t5 = timeit.timeit('cp_simulate_mc_cum()', setup='from __main__ import cp_simulate_mc_cum', number=1)
    #print('5千条路径')
    # print('numpy全向量化耗时', t1)
    # print('改进一：随机数用gpu耗时', t2)
    # print('改进二：随机数和路径都用gpu耗时', t3)
    print('完整雪球定价时间', t4)
    # print('改进三：连乘用gpu内置函数耗时', t5)
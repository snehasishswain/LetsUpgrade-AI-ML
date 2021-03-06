# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:31:13 2020

@author: SNEHASISH
"""


import pandas as pd

import statsmodels.api as sm

from statsmodels.formula.api import ols

dataset=pd.read_excel("ANCOVA1.xlsx",sheetname=0)

dataset.head()
Out[41]: 
   Store Number  Sales  Promotion  Coupon  ClietelRatings
0             1     10          1       1               9
1             2      9          1       1              10
2             3     10          1       1               8
3             4      8          1       1               4
4             5      9          1       1               6


model=ols('Sales~C(Promotion)',dataset).fit()

oneway=sm.stats.anova_lm(model,typ=2)

print(oneway)
                  sum_sq    df          F    PR(>F)
C(Promotion)  106.066667   2.0  17.943609  0.000011
Residual       79.800000  27.0        NaN       NaN

model=ols('Sales~C(Promotion)*C(Coupon)',dataset).fit()

twoway=sm.stats.anova_lm(model,typ=2)

print(twoway)
                            sum_sq    df          F        PR(>F)
C(Promotion)            106.066667   2.0  54.862069  1.116908e-09
C(Coupon)                53.333333   1.0  55.172414  1.143879e-07
C(Promotion):C(Coupon)    3.266667   2.0   1.689655  2.058092e-01
Residual                 23.200000  24.0        NaN           NaN

# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:30:14 2020

@author: SNEHASISH
"""


Python 3.6.3 |Anaconda custom (32-bit)| (default, Oct 15 2017, 07:29:16) [MSC v.1900 32 bit (Intel)]
Type "copyright", "credits" or "license" for more information.

IPython 6.1.0 -- An enhanced Interactive Python.

import pandas as pd

from scipy.stats import wilcoxon

dataset=pd.read_excel("1 Wilcoxon.xlsx",sheetname=0)

dataset.head()
Out[4]: 
   ID  TRT  AGE  WEIGHIN  STAGE  TOTALCIN  TOTALCW2  TOTALCW4 TOTALCW6
0   1    0   52    124.0      2         6         6         6        7
1   5    0   77    160.0      1         9         6        10        9
2   6    0   60    136.5      4         7         9        17       19
3   9    0   61    179.6      1         6         7         9        3
4  11    0   59    175.8      2         6         7        16       13

d1=dataset.TOTALCIN

d2=dataset.TOTALCW2

stat, p=wilcoxon(d1,d2)

print(stat,p)
29.5 0.00259741456482

from scipy.stats import friedmanchisquare

d3=dataset.TOTALCW4

stat,p=friedmanchisquare(d1,d2,d3)

print(stat,p)
27.9277108434 8.62133745016e-07

from scipy.stats import mannwhitneyu

dataset1=pd.read_excel("3 Mann Whitney.xlsx",sheetname=1)

dataset1.head()
Out[15]: 
   Design1  Design2
0       11       12
1       17       10
2       16       15
3       14       19
4       15       11

a1=dataset1.Design1

a2=dataset1.Design2

stat,p=mannwhitneyu(a1,a2)

print(stat,p)
9.0 0.264179663635

from scipy.stats import kruskal

dataset2=pd.read_excel("4 Kruskal Wallis.xlsx",sheetname=0)

dataset2.head()
Out[22]: 
   Design1  Design2  Design3
0       11       12        6
1       17       10        8
2       16       15       10
3       14       19        2
4       15       11       10

b1=dataset2.Design1

b2=dataset2.Design2

b3=dataset2.Design3

stat,p=kruskal(b1,b2,b3)

print(stat,p)
9.05703971119 0.0107966448452

from scipy.stats import ttest_1samp

dataset6=pd.read_excel("1. One Sample.xlsx",sheetname=0)

dataset6.head()
Out[30]: 
     ids  Height
0  43783   72.35
1  20278   70.66
2  20389   70.68
3  24559   67.43
4  28980   68.45

h1=dataset6.Height

stat,p=ttest_1samp(h1,65)

print(stat,p)
11.4988002386 1.08789357016e-26

from scipy.stats import ttest_rel

dataset3=pd.read_excel("2. Paired Sample.xlsx",sheetname=0)

dataset3.head()
Out[36]: 
     ids  English   Math
0  43783    88.24  60.02
1  20278    89.45  70.19
2  20389    96.73  71.20
3  22820    74.06  55.89
4  24559    82.61  65.52

p1=dataset3.English

p2=dataset3.Math

stat,p=ttest_rel(p1,p2)

print(stat,p)
36.3125689817 3.07109871922e-128

from scipy.stats import ttest_ind

dataset4=pd.read_excel("3. Independent Sample.xlsx",sheetname=3)

dataset4.head()
Out[50]: 
   Nonathelete  Athelete
0     0.004413  0.004462
1     0.004872  0.005146
2     0.008851  0.004023
3     0.006508  0.003941
4     0.006314  0.004764

z1=dataset4.Nonathelete

z2=dataset4.Athelete

stat,p=ttest_ind(z1,z2)

print(stat,p)
13.3687904321 7.11663315723e-33

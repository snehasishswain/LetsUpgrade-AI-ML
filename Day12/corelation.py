# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from scipy.stats import pearsonr
dataset=pd.read_excel("Correlation.xlsx",sheetname=1)
dataset.head()
a1=dataset.Attitude toward the City
a2=dataset.Duration of Residence
stat, p = pearsonr(a1,a2)
print(stat, p)



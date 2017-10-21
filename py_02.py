# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:30:34 2017

@author: yuhua
"""

import pandas as pd
import numpy as np
from tsutils import *

def performance(df):
    mean = df.iloc[:,0].mean()
    std = df.iloc[:,0].std()
    print('mean:',mean)
    print('std:',std)
    print('mean/std:',mean/std,'\n')

def event_01(df1,df2):
    i = 0
    count = 0
    while(i < len(df1)-2):
        if df1[i]>df1[i+1] and df1[i+1]>df1[i+2] and df1[i+2]<df1[i+3]:
            print(df1.index[i+3])
            count = count + 1
            Date_A = df1.index[i+3]
            Date_B = end_of_month(df1.index[i+3],1)
            df_period = df2.loc[(df2.index > Date_A) & (df2.index <= Date_B)]
            performance(df_period)
        i=i+1
    print('times added:',count,'\n')

#读入十年期国债收益率的EXCEL
df_bond_origin = pd.read_excel("bond.xlsx").set_index('date')
df_bond = df_bond_origin.dropna()
#读入宏观因子的EXCEL
df = pd.read_excel("macrofactor.xlsx",sheetname=0).set_index('date')
for name in df.columns:
    df_column=df[name].dropna()
    event_01(df_column,df_bond)

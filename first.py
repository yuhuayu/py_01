# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:06:21 2017

@author: yuhua
"""

import pandas as pd
import numpy as np

df = pd.read_excel("macrofactor.xlsx",sheetname=0).set_index('date')
df1=df['IVA_yoy'].dropna()
print(type(df1.index[0]))
time=list()
i=0
while(i < len(df1)-2):
    if df1[i]>df1[i+1] and df1[i+1]>df1[i+2] and df1[i+2]<df1[i+3]:
        time.append(df1.index[i+3])
    i=i+1

df_bond = pd.read_excel("bond.xlsx")
print(type(df_bond.index[0]))
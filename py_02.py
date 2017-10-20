# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:30:34 2017

@author: yuhua
"""

import pandas as pd
import numpy as np
import datetime as dt

df_bond_origin = pd.read_excel("bond.xlsx").set_index('date')
df_bond = df_bond_origin.dropna()
df = pd.read_excel("macrofactor.xlsx",sheetname=0).set_index('date')
df1=df['IVA_yoy'].dropna()

def end_of_month(regDate, months):
    addYear = months // 12
    addMonth = months - addYear * 12
    newMonth = regDate.month + addMonth
    if newMonth == 12:
        res = dt.datetime(regDate.year + addYear, newMonth, 31)
    else:
        res = dt.datetime(regDate.year + addYear, newMonth + 1, 1) - dt.timedelta(1)
        return res

i=0
while(i < len(df1)-2):
    if df1[i]>df1[i+1] and df1[i+1]>df1[i+2] and df1[i+2]<df1[i+3]:
            print(df1.index[i+3])
            if df1.index[i+3] in df_bond.index:
                print(df1.index[i+3],df_bond.loc[df1.index[i+3],'bondreturn'])
            Date_A = df1.index[i+3]
            Date_B = end_of_month(df1.index[i+3],1)
            print(df_bond.loc[(df_bond.index >= Date_A) & (df_bond.index <= Date_B)])
    i=i+1
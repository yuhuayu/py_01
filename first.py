# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:06:21 2017

@author: yuhua
"""

from tsutils import *
import pandas as pd
import numpy as np

df_bond_origin = pd.read_excel("bond.xlsx").set_index('date')
df_bond = df_bond_origin.dropna()
df = pd.read_excel("macrofactor.xlsx",sheetname=0).set_index('date')
df1=df['IVA_yoy'].dropna()
i=0
while(i < len(df1)-2):
    if df1[i]>df1[i+1] and df1[i+1]>df1[i+2] and df1[i+2]<df1[i+3]:
            print(df1.index[i+3])
            if df1.index[i+3] in df_bond.index:
                print(df1.index[i+3],df_bond.loc[df1.index[i+3],'bondreturn'])
            time_occur=str(df1.index[i+3])
            for time in df_bond.index:
                str_time = str(time)
                if int(time_occur[5:7]) == 12:
                    if int(time_occur[0:4])+1 == int(str_time[0:4]) and int(str_time[5:7]) == 1:
                        print(str_time,df_bond.loc[time,'bondreturn'])
                else:
                    if int(time_occur[0:4]) == int(str_time[0:4]) and int(time_occur[5:7])+1==int(str_time[5:7]):
                        print(str_time,df_bond.loc[time,'bondreturn'])
            print('\n')
    i=i+1

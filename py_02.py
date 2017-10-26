# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:30:34 2017

@author: yuhua
"""

import pandas as pd
import numpy as np
import xlwt
from tsutils import *

def occur(name):
    if name == 'Turn_To_Rise':
        def fuc_01(x):
            if x[0]>x[1] and x[1]>x[2] and x[2]<x[3]:
                return 1
            else:
                return 0
        dfn = df_column.rolling(4).apply(fuc_01)
        return dfn
    
    if name == 'Turn_To_Fall':
        def fuc_02(x):
            if x[0]<x[1] and x[1]<x[2] and x[2]>x[3]:
                return 1
            else:
                return 0
        dfn = df_column.rolling(4).apply(fuc_02)
        return dfn
    
    if name == 'Continue_To_Rise':
        def fuc_03(x):
            if x[0]<x[1] and x[1]<x[2] and x[2]<x[3]:
                return 1
            else:
                return 0
        dfn = df_column.rolling(4).apply(fuc_03)
        return dfn
    
    if name == 'Continue_To_Fall':
        def fuc_04(x):
            if x[0]>x[1] and x[1]>x[2] and x[2]>x[3]:
                return 1
            else:
                return 0
        dfn = df_column.rolling(4).apply(fuc_04)
        return dfn
    
    if name == 'Historical_High':
        df1 = df_column.expanding(min_periods=1).max()
        def fuc_05(x):
            if x[0]==x[1]:
                return 0
            else:
                return 1
        dfn = df1.rolling(2).apply(fuc_05)
        return dfn
        
    if name == 'Historical_Low':
        df1 = df_column.expanding(min_periods=1).min()
        def fuc_06(x):
            if x[0]==x[1]:
                return 0
            else:
                return 1
        dfn = df1.rolling(2).apply(fuc_06)
        return dfn
    
    if name == 'Low_In_Short_Time':
        v_mean = df_column.rolling(18).mean()
        v_std = df_column.rolling(18).std()
        diff = v_mean - 2*v_std
        df1 = df_column - diff.shift(1)
        def fuc_07(x):
            if x[18] < 0:
                return 1
            else:
                return 0
        dfn = df1.rolling(19).apply(fuc_07)
        return dfn
    
    if name == 'High_In_Short_Time':
        v_mean = df_column.rolling(18).mean()
        v_std = df_column.rolling(18).std()
        add = v_mean + 2*v_std
        df1 = df_column - add.shift(1)
        def fuc_08(x):
            if x[18] > 0:
                return 1
            else:
                return 0
        dfn = df1.rolling(19).apply(fuc_08)
        return dfn
        

def performance(date):
    count=0
    count_positive=0
    retn = []
    for t in date:
        Date_A = t
        Date_B = end_of_month(t,1)
        df_period = df_bond.loc[(df_bond.index > Date_A) & (df_bond.index <= Date_B)]
        def fuc_09(x):
            return 100*(x[0]-x[1])
        df_ret = df_period.rolling(2).apply(fuc_09)
        ret = df_ret.dropna().mean().get('yield')
        retn.append(ret)
        count=count+1
        if ret > 0:
            count_positive = count_positive + 1
    mean = np.mean(retn)
    std = np.std(retn)
    IR = mean/std
    sheet.write(a,2,count)
    sheet.write(a,3,count_positive)
    sheet.write(a,4,mean)
    sheet.write(a,5,std)
    sheet.write(a,6,IR)


#创建输出结果的工作表
file = xlwt.Workbook()
sheet = file.add_sheet('result')
row0 = ['FACTOR','EVENT','COUNT','COUNT_POSITIVE','MEAN','STD','IR']
for i in range(len(row0)):  
    sheet.write(0, i, row0[i]) 

#读入十年期国债收益率
df_bond_origin = pd.read_excel("bond.xlsx").set_index('date')
df_bond = df_bond_origin.dropna()

#读入宏观因子
df = pd.read_excel("macrofactor.xlsx",sheetname=0).set_index('date')
a=1
for name in df.columns:
    print('COLUMN:',name)
    df_column=df[name].dropna()  
      
    events=pd.Series(['Turn_To_Rise','Turn_To_Fall','Continue_To_Rise','Continue_To_Fall','Historical_High','Historical_Low','Low_In_Short_Time','High_In_Short_Time'])
    for event in events:
        sheet.write(a,0,name)
        sheet.write(a,1,event)
        print('EVENT NAME:',event)
        dfn = occur(event)
        time_signal = dfn.loc[dfn==1].index
        count = dfn.dropna().sum()
        print(time_signal,'\n')
        performance(time_signal)
        a = a+1
file.save('result.xls')

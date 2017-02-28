# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 22:24:12 2017

@author: George
"""

import talib as ta
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt

#import data
data=ts.get_k_data('000001',start='2016-01-01',end='2016-12-31',ktype='D',autype='qfq')
data.index=pd.to_datetime(data['date'],format='%Y-%m-%d')
#MA related
middleband=ta.abstract.MA(data,timeperiod=20)
upperband=middleband*1.03
lowerband=middleband*0.97
data_B=pd.concat([middleband,upperband,lowerband],axis=1)
data_B.columns=['middleband','upperband','lowerband']
#bolling
data_B=ta.abstract.BBANDS(data,timeperiod=20)
#average range
atr=ta.abstract.ATR(data,timeperiod=20)
middleband=ta.abstract.MA(data,20)
upperband=middleband+atr
lowerband=middleband-atr
data_B=pd.concat([middleband,upperband,lowerband],axis=1)
data_B.columns=['middleband','upperband','lowerband']
#high and low
upperband=ta.abstract.MAX(data,20,price='high')
lowerband=ta.abstract.MIN(data,20,price='low')
middleband=(upperband+lowerband)/2
data_B=pd.concat([middleband,upperband,lowerband],axis=1)
data_B.columns=['middleband','upperband','lowerband']

plt.plot(data['close'])
plt.plot(data_B['middleband'],'r',alpha=0.3)
plt.plot(data_B['upperband'],'r',alpha=0.3)
plt.plot(data_B['lowerband'],'r',alpha=0.3)
plt.show()


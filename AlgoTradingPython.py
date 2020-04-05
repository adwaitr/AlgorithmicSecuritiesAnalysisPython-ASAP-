#!/usr/bin/env python
# coding: utf-8

# ### Algorithmic Trading in Python. 
# 
# Adwait Rangnekar
# Github : https://github.com/adwaitr
# Linkedin : https://www.linkedin.com/in/adwait-rangnekar/
# Stack : https://stackoverflow.com/users/10079512/adwait-rangnekar
# Mail : adwaitedu@gmail.com

# In[ ]:





# In[1]:


pip install pandas


# In[1]:


pip install pandas_datareader


# In[3]:


import pandas as pd


# In[4]:


pd.core.common.is_list_like = pd.api.types.is_list_like


# In[5]:


from pandas_datareader import data


# In[11]:


df = data.get_data_yahoo ('^NSEI', '2018-01-01', '2019-01-01')


# In[12]:


df.head(10)


# In[13]:


df.tail(10)


# In[14]:


pip install quandl


# In[15]:


import quandl


# In[37]:


tesla = quandl.get("WIKI/TSLA", start_date="2018-01-01", end_date="2019-01-01")


# In[38]:


tesla.describe()


# In[39]:


aapl = quandl.get("WIKI/AAPL", start_date="2018-01-01", end_date="2019-01-01")


# In[40]:


aapl.describe()


# In[44]:


import pandas as pd


# In[45]:


import pandas_datareader as pdr


# In[46]:


import datetime


# In[47]:


aapl=pdr.get_data_yahoo('AAPL',start=datetime.datetime(2008,1,1), end=datetime.datetime(2012,1,1))


# In[48]:


aapl.describe()


# In[49]:


aapl.to_csv('Apple_2008-12.csv')


# In[50]:


download_aapl="Apple_2008-12.csv"


# In[51]:


aapl['Change']=aapl.Open - aapl.Close

aapl['Pct_Chg']=aapl.Change/aapl.Open

import matplotlib.pyplot as plt


# In[52]:


aapl['Pct_Chg'].plot(grid=True)


# In[53]:


tesla['Change']=tesla.Open - tesla.Close

tesla['Pct_Chg']=tesla.Change/tesla.Open

import matplotlib.pyplot as plt


# In[54]:


tesla['Pct_Chg'].plot(grid=True)


# In[55]:


plt.show()


# In[63]:


def get(tickers, startdate, enddate):
    def data(ticker):
        return(pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
    datas=map(data,tickers)
    return(pd.concat(datas,keys=tickers,names=['Ticker','Date']))
tickers=['MSFT', '500010.BO', 'INR=X', '^BSESN', '^NSEI']
all_data=get(tickers, datetime.datetime(2018,1,1), datetime.datetime(2019,1,1))


# In[64]:


all_data


# In[65]:


all_data.to_csv('IndianStocks.csv')


# In[66]:


import matplotlib.pyplot as plt


# In[68]:


list1 = []
with open("IndianStocks.csv") as f:
    for row in f:
        list1.append(row.split()[0])


# In[69]:


plt.plot(list1)


# In[70]:


plt.show()


# In[79]:


list1 = []
with open("IndianStocks.csv") as f:
    for row in f:
        list1.append(row.split()[0])
list2 = []
with open("IndianStocks.csv") as f:
    for column in f:
        list2.append(column.split()[0])


# In[80]:


plt.plot(list1,list2)


# In[81]:


plt.show()


# In[82]:


plt.scatter(list1,list2)


# In[ ]:


#Trying the same with only NSE Data and smaller time frame. 


# In[101]:


def get(tickers, startdate, enddate):
    def data(ticker):
        return(pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
    datas=map(data,tickers)
    return(pd.concat(datas,keys=tickers,names=['Ticker','Date']))
tickers=['^NSEI']
nse = get(tickers, datetime.datetime(2019,1,1), datetime.datetime(2019,4,1))


# In[91]:


nse.head(10)


# In[92]:


nse.tail(10)


# In[93]:


nse.to_csv('nse.csv')


# In[98]:


listn = []
with open("nse.csv") as f:
    for row in f:
        listn.append(row.split()[0])
listv = []
with open("nse.csv") as f:
    for column in f:
        listv.append(column.split()[0])


# In[100]:


plt.scatter(listn,listv)


# In[103]:


def get(tickers, startdate, enddate):
    def data(ticker):
        return(pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
    datas=map(data,tickers)
    return(pd.concat(datas,keys=tickers,names=['Ticker','Date']))
tickers=['^NSEI']
nse1 = get(tickers, datetime.datetime(2019,3,1), datetime.datetime(2019,4,1))


# In[104]:


nse1.to_csv("nse1.csv")


# In[114]:


listn = []
with open("nse1.csv") as f:
    for row in f:
        listn.append(row.split()[0])
listv = []
with open("nse1.csv") as f:
    for column in f:
        listv.append(column.split()[0])


# In[119]:


plt.bar(listn,listv)


# In[122]:


nse1['Change']=nse1.Open - nse1.Close

nse1['Pct_Chg']=nse1.Change/nse1.Open

import matplotlib.pyplot as plt


# In[124]:


nse1['Pct_Chg'].plot(grid=True)


# In[125]:


plt.plot(nse1.Open,nse1.Volume)


# In[126]:


plt.plot(nse1.Open,nse1.Volume)


# In[127]:


plt.plot(nse.Open,nse.Volume)


# #The End 
# Adwait Rangnekar
# Github : https://github.com/adwaitr
# Linkedin : https://www.linkedin.com/in/adwait-rangnekar/
# Stack : https://stackoverflow.com/users/10079512/adwait-rangnekar
# Mail : adwaitedu@gmail.com






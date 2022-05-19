#!/usr/bin/env python
# coding: utf-8

# # Bar Chart Race 

# In[3]:


import pandas as pd
import os


# In[4]:


files = [file for file in os.listdir(r'C:\Users\DELL\Downloads\Bar Chart')]
for file in files :
    print(file)


# In[6]:


path = r'C:\Users\DELL\Downloads\Bar Chart'

df = pd.DataFrame()

for file in files :
    current_data = pd.read_csv(path+'/'+file)
    df = pd.concat([df, current_data])
print(df)


# In[7]:


#data cleanning
df.columns


# In[8]:


df = df[['dateRep','countriesAndTerritories','cases']]
df


# In[9]:


df.dtypes


# In[10]:


df['date'] = pd.to_datetime(df['dateRep'],dayfirst = True)
df


# In[12]:


df = df.drop(columns = ['dateRep'])
df


# # calcul du cumul des cas

# In[15]:


df['total_cases'] = df.sort_values('date').groupby('countriesAndTerritories').cumsum().sort_index()
df


# In[17]:


df = df[['date','countriesAndTerritories','total_cases']]
df = df.rename(columns = {'countriesAndTerritories':'pays'})
df


# # Pivoter deux tables

# In[19]:


df = pd.pivot_table(df, index = ['date'], columns = ['pays'], values = ['total_cases'])
df


# In[20]:


df.columns


# In[21]:


df.index.name = None
df.columns = [col[1] for col in df.columns]
df


# In[23]:


#Remplacer la valeur Nan par 0
df = df.fillna(0).astype(int)
df


# In[26]:


df = df.drop(columns = ['Cases_on_an_international_conveyance_Japan'])


# In[28]:


df.columns = [col.replace('_',' ') for col in df.columns]
df


# In[29]:


#Alleger la bd
country_reserved = set()
for index, row in df.iterrows():
    country_reserved |= set(row[row > 0].sort_values(ascending = False).head(10).index)
df = df[list(country_reserved)]    


# In[30]:


df.shape


# In[32]:


#Générer la vidéo
get_ipython().system('pip install bar-chart-race')


# In[33]:


import bar_chart_race as bcr


# In[37]:


bcr.bar_chart_race(
    df = df,
    filename = '/Users/DELL/Downloads/Bar Chart/covid-19.mp4',
    n_bars = 10,
    period_fmt = '%B %d, %Y ',
    title = 'Evolution des cas covid par pays'
)


# In[38]:


pip install ffmpeg


# In[39]:


bcr.bar_chart_race(
    df = df,
    filename = '/Users/DELL/Downloads/Bar Chart/covid-19.mp4',
    n_bars = 10,
    period_fmt = '%B %d, %Y ',
    title = 'Evolution des cas covid par pays'
)


# In[ ]:





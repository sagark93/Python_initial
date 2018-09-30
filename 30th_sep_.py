#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[9]:


import numpy as np
df = pd.read_csv("train_1.csv")


# In[3]:


import os


# In[5]:


os.chdir('/home/jovyan/binder/Untitled Folder')


# In[36]:


correlation_matrix = df.select_dtypes(include = (np.number)).corr()


# In[37]:


correlation_matrix


# In[ ]:


type correlation_matrix


# In[ ]:


correlation_matrix[["SalePrice"]]


# In[ ]:


correlation_matrix[["SalePrice"]].iloc


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns


# In[2]:


data=pd.read_csv("insurance.csv")
data.head()


# In[3]:


data.shape


# In[4]:


data.columns


# In[5]:


data.info()


# In[6]:


data.describe()


# In[7]:


data.describe(include="all")


# In[8]:


data.isnull().sum()


# In[9]:


data["bmi"].isnull().sum()


# In[10]:


sns.heatmap(data.corr(),annot=True)


# In[11]:


sns.scatterplot(x=data["age"],y=data["expenses"])


# In[12]:


sns.histplot(data=data,x="age",color="green",edgecolor="black",bins=5)


# In[13]:


sns.boxplot(data=data,x="age")


# In[14]:


from sklearn.preprocessing import LabelEncoder
enc=LabelEncoder()


# In[15]:


data.sex=enc.fit_transform(data.sex)


# In[16]:


data.sex


# In[17]:


data.region=enc.fit_transform(data.region)
data.region


# In[18]:


data.smoker=enc.fit_transform(data.smoker)
data.smoker


# In[19]:


sns.heatmap(data.corr(),annot=True)


# In[20]:


data.drop('region',axis=1,inplace=True)


# In[21]:


data


# In[22]:


x=data[['age','sex','bmi','children','smoker']]
y=data.expenses


# In[23]:


data


# In[24]:


from sklearn.model_selection import train_test_split


# In[25]:


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=10)
x_train.shape


# In[26]:


from sklearn.linear_model import LinearRegression


# In[27]:


x_test.shape


# In[28]:


from sklearn.linear_model import LinearRegression


# In[29]:


model=LinearRegression()


# In[30]:


model.fit(x_train,y_train)


# In[31]:


model_pred=model.predict(x_test)


# In[32]:


print(model_pred)


# In[33]:


from sklearn.metrics import r2_score


# In[34]:


r2_score(y_test,model_pred)


# In[35]:


from joblib import dump,load


# In[36]:


dump(model,'insur.joblib')


# In[ ]:





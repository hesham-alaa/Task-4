#!/usr/bin/env python
# coding: utf-8

# # 1- Question 
# 1-read you csv file (https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv )
# 
# 2-print the first 5 rows 
# 
# 3-print the shape of the data
# 
# 4- print and data type of each column

# In[27]:


import pandas as pd
import numpy as np

dataframe = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv ')

print(dataframe.head(5))
print('shape of the data:')
print(dataframe.shape)
print(dataframe.dtypes)


# # 2-Question
# 1- print carat column
# 
# 2- Write a Pandas program to create a new 'Quality -color' Column (cut,color)
# 
# examble => ( Ideal, E)

# In[31]:


print(dataframe["carat"])
dataframe["Quality-color"] = dataframe["cut"] + ', ' + dataframe["color"]
print(dataframe["Quality-color"])


# # 3-Question
# 1-Write a Pandas program to summarize the data.
# 
# 2- only one column => 'table'
# 
# 3- only 'float64' columns of the diamonds Dataframe. => include=['...']

# In[32]:


print(dataframe.describe())
print('only one column: ',dataframe['table'].describe())
print('only columns of the diamonds Dataframe: ',dataframe.describe(include="float64"))


# # 4-Question
# Write a Pandas program to find the details of the diamonds where length>5, width>5 and depth>5. (x,y,z)

# In[13]:


print("Diamonds where length>5, width>5 and depth>5:")
result = dataframe[(dataframe["x"]>5) & (dataframe["y"]>5) & (dataframe["z"]>5)]
print(result.head())


# # 5-Question
# 1- rename one col
# 
# 2- rename two col togeather
# 
# 3- rename all col togeather

# In[14]:


dataframe.rename(columns={'price':'dataframe_price'}, inplace=True)
print("rename one col : ",dataframe.head())
dataframe.rename(columns={'color':'dataframe_color', 'carat':'dataframe_carat'}, inplace=True)
print("rename two col togeather: ",dataframe.head())
dataframe_cols = ['new_carat', 'new_cut', 'new_color', 'new_clarity', 'new_depth', 'new_table', 'new_price', 'new_x', 'new_y', 'new_z',"new-Quality-color"]
dataframe.columns = dataframe_cols
print("\n renaming all the columns of thedataframe: ",dataframe)


# # 6-Question
# Write a Pandas program to find the diamonds that are either Good or Very Good.

# In[15]:


result = dataframe[dataframe['new_cut'].isin(['Good', 'Very Good'])]
print(result)


# # 7-Question
# 1-print the name of all the columns
# 
# 2- Mean of each column
# 
# 3-Mean of each row of diamonds DataFrame:

# In[16]:


print(dataframe.columns)
print('Mean of each column : ',dataframe.mean())
print('Mean of each row of diamonds DataFrame : ',dataframe.mean(axis=1))


# # 8-Question
# 1- mean of 'price' column only
# 
# 2- Write a Pandas program to calculate the mean of price for each cut of diamonds DataFrame.
# 
# 3-Write a Pandas program to calculate count, minimum, maximum price for each cut of diamonds DataFrame.
# 
# 4- count how many times each value in cut series of diamonds DataFrame occurs. value_counts()

# In[17]:


print('Mean of price column : ',dataframe['new_price'].mean())
print('Mean of price column : ',dataframe.groupby('new_cut')['new_price'].mean())
print("many times each value in cut series of diamonds DataFrame occurs",dataframe['new_cut'].value_counts())


# # 9-Question
# Write a Pandas program to count the number of missing values in each Series of diamonds DataFrame.

# In[18]:


print("the number of missing values ",dataframe.isnull().sum())


# In[ ]:





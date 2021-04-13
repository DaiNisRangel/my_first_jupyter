#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Load of all .csv
df_ubereats_centro = pd.read_csv(r'csv/ubereats-pizza-centro.csv')
df_ubereats_alamos = pd.read_csv(r'csv/ubereats-pizza-alamos.csv')
df_ubereats_juriquilla = pd.read_csv(r'csv/ubereats-pizza-juriquilla.csv')
df_ubereats_milenio = pd.read_csv(r'csv/ubereats-pizza-milenio.csv')
df_ubereats_refugio = pd.read_csv(r'csv/ubereats-pizza-refugio.csv')

df_ubereats_balvanera = pd.read_csv(r'csv/ubereats-pizza-balvanera.csv')
df_ubereats_campanario = pd.read_csv(r'csv/ubereats-pizza-campanario.csv')
df_ubereats_cerritocolorado = pd.read_csv(r'csv/ubereats-pizza-cerritocolorado.csv')
df_ubereats_cimatario = pd.read_csv(r'csv/ubereats-pizza-cimatario.csv')
df_ubereats_el_pueblito = pd.read_csv(r'csv/ubereats-pizza-el-pueblito.csv')

df_rappi_centro = pd.read_csv(r'csv/rappi-pizza-centro.csv')
df_rappi_alamos = pd.read_csv(r'csv/rappi-pizza-alamos.csv')
df_rappi_juriquilla = pd.read_csv(r'csv/rappi-pizza-juriquilla.csv')
df_rappi_milenio = pd.read_csv(r'csv/rappi-pizza-milenio.csv')
df_rappi_refugio = pd.read_csv(r'csv/rappi-pizza-refugio.csv')

df_rappi_balvanera = pd.read_csv(r'csv/rappi-pizza-balvanera.csv')
df_rappi_campanario = pd.read_csv(r'csv/rappi-pizza-campanario.csv')
df_rappi_cerritocolorado = pd.read_csv(r'csv/rappi-pizza-cerritocolorado.csv')
df_rappi_cimatario = pd.read_csv(r'csv/rappi-pizza-cimatario.csv')
df_rappi_el_pueblito = pd.read_csv(r'csv/rappi-pizza-el-pueblito.csv')

frames = [
    df_ubereats_centro, 
    df_ubereats_alamos, 
    df_ubereats_juriquilla, 
    df_ubereats_milenio, 
    df_ubereats_refugio, 
    df_ubereats_balvanera, 
    df_ubereats_campanario, 
    df_ubereats_cerritocolorado, 
    df_ubereats_cimatario, 
    df_ubereats_el_pueblito, 
    df_rappi_centro, 
    df_rappi_alamos, 
    df_rappi_juriquilla, 
    df_rappi_milenio, 
    df_rappi_refugio, 
    df_rappi_balvanera, 
    df_rappi_campanario, 
    df_rappi_cerritocolorado, 
    df_rappi_cimatario, 
    df_rappi_el_pueblito]

# We concat all frames and ignore the current index to generate a new one
df = pd.concat(frames, ignore_index=True)


# In[3]:


print('Size of the df: {} items'.format(df.count()['name']))


# In[4]:


# Note that the price-food has MX$
df.loc[:,['name','rating','evals','name-food','price-food']]


# In[5]:


# Remove MX$ from price-food
df['price-food'] = df['price-food'].apply(lambda x: (float(x[3:] if x[0] == 'M' else x[1:]) if not isinstance(x, int) else float(x)) if not isinstance(x, float) else x)

# for index, row in df.iterrows():
#     print(float(row['price-food'][3:]) if not isinstance(row['price-food'], float) else row['price-food'])


# In[6]:


df.loc[:,['name','name-food','price-food']]


# In[7]:


# Get all "pizza" dataframes
dfPizzas = df[df['name-food'].str.contains("pizza", na=False, case=False)]
dfPizzas.reset_index(drop=True, inplace=True)
dfPizzas.loc[:,['name','name-food','price-food']]


# In[8]:


minPizza = dfPizzas.loc[dfPizzas['price-food'] == dfPizzas['price-food'].min()]

print('The pizzas with the lower price are:')
minPizza.loc[:,['name','name-food','price-food']]


# In[9]:


maxPizza = dfPizzas.loc[dfPizzas['price-food'] == dfPizzas['price-food'].max()]

print('The pizzas with the greatest price are:')
maxPizza.loc[:,['name','name-food','price-food']]


# In[10]:


meanPizzaVal = dfPizzas['price-food'].mean()
meanPizza = dfPizzas.loc[dfPizzas['price-food'] == meanPizzaVal]

print(f'The mean price is ${meanPizzaVal}:')
meanPizza.loc[:,['name','name-food','price-food']]


# In[11]:


medianPizza = dfPizzas.loc[dfPizzas['price-food'] == dfPizzas['price-food'].median()]

print('The pizzas with the median price are:')
medianPizza.loc[:,['name','name-food','price-food']]


# In[12]:


modePizza = dfPizzas.loc[dfPizzas['price-food'] == dfPizzas['price-food'].mode()[0]]

print('The pizzas with the mode price are:')
modePizza.loc[:,['name','name-food','price-food']]


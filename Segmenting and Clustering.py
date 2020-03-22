#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np # library to handle data in a vectorized manner

import pandas as pd # library for data analsysis
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

import json # library to handle JSON files

#!conda install -c conda-forge geopy --yes # uncomment this line if you haven't completed the Foursquare API lab
from geopy.geocoders import Nominatim # convert an address into latitude and longitude values

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

# import k-means from clustering stage
from sklearn.cluster import KMeans

#!conda install -c conda-forge folium=0.5.0 --yes # uncomment this line if you haven't completed the Foursquare API lab
#import folium # map rendering library

import requests

from bs4 import BeautifulSoup

print('Libraries imported.')


# In[54]:


source = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text
soup = BeautifulSoup(source, 'html5lib')


# In[55]:


Dictionary_of_postal_codes = {} 
for table_cell in soup.find_all('td'):
    try:
        zip_code = table_cell.p.b.text 
        zip_code_investigate = table_cell.span.text
        area_data = table_cell.span.text 
        borough = area_data.split('(')[0] 
        if area_data == 'Not assigned': area = []
        else:
            Dictionary_of_postal_codes[zip_code] = {}                              
            try:
                area = area_data.split('(')[1]
                area = area.replace('(', ' ')
                area = area.replace(')', ' ')
                area_names = area.split('/')
                area_clean = ', '.join([name.strip() for name in area_names])
            except:
                borough = borough.strip('\n')
                area_clean = borough
            Dictionary_of_postal_codes[zip_code]['borough'] = borough
            Dictionary_of_postal_codes[zip_code]['neighborhoods'] = area_clean
    except:pass   


# In[56]:


# First an empty dataframe is created
columns = ['PostalCode', 'Borough', 'Neighborhood']
city_data = pd.DataFrame(columns=columns)
city_data


# In[74]:


# Fill dataframe with data from dictionary
for ind, zip_code in enumerate(Dictionary_of_postal_codes):
    borough = Dictionary_of_postal_codes[zip_code]['borough']
    neighborhood = Dictionary_of_postal_codes[zip_code]['neighborhoods']
    city_data = city_data.append({"PostalCode": zip_code, "Borough": borough, "Neighborhood": neighborhood},ignore_index=True)


# In[75]:


# printing the top 11 rows from the dataframe
city_data.head(12) 


# In[76]:


print ('The number if rows in the dataframe is ', city_data.shape[0])


# In[60]:





# In[62]:


source2 = requests.get('http://cocl.us/Geospatial_data').text
soup2 = BeautifulSoup(source2, 'html5lib')


# In[83]:


Dictionary_of_postal_codes2 = {} 
for table_cell in soup.find_all('td'):
    try:
        zip_code2 = table_cell.p.b.text 
        zip_code_investigate2 = table_cell.span.text
        area_data2 = table_cell.span.text 
        borough2 = area_data.split('(')[0] 

        if area_data2 == 'Not assigned': area2 = []
        else:
            Dictionary_of_postal_codes2[zip_code2] = {}                              
            try:
                area2 = area_data2.split('(')[1]
                area2 = area2.replace('(', ' ')
                area2 = area2.replace(')', ' ')
                area_names2 = area2.split('/')
                area_clean2 = ', '.join([name.strip() for name in area_names2])
            except:
                borough2 = borough2.strip('\n')
                area_clean2 = borough2
            Dictionary_of_postal_codes2[zip_code2]['borough'] = borough2
            Dictionary_of_postal_codes2[zip_code2]['neighborhoods'] = area_clean2
    except:pass 


# In[71]:


# First an empty dataframe is created
columns2 = ['PostalCode', 'Borough', 'Neighborhood', 'Latitude', 'Longitude']
city_data2 = pd.DataFrame(columns=columns2)
city_data2


# In[ ]:





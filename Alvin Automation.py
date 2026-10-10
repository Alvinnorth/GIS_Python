#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("have a nice day!")


# In[2]:


import geopandas as gpd


# In[3]:


import matplotlib.pyplot as plt
print("pustaka anda siap digunakan")


# In[4]:


import leafmap as lm
m = lm.Map(center=[-6.2, 106.8], zoom=10)
m.add_basemap("HYBRID")
m


# In[5]:


num_points = 7
print("Jumlah titik yang akan dibuat:", num_points)


# In[6]:


import leafmap
import geopandas as gpd

# 1. Tentukan path file shapefile lokal Anda (gunakan huruf 'r' di depan string)
shapefile_path = r"D:\SHP_Sungai\SHP_Sungai_TP.shp"

# 2. Baca file shapefile menggunakan GeoPandas
gdf = gpd.read_file(shapefile_path)

# 3. Buat objek peta dengan leafmap dan tambahkan basemap
m = leafmap.Map(center=[-6.2, 106.8], zoom=10)
m.add_basemap("HYBRID")

# 4. Tambahkan GeoDataFrame ke peta
m.add_gdf(gdf, layer_name="Data Sungai", zoom_to_layer=True)

# 5. Tampilkan peta
m


# In[ ]:





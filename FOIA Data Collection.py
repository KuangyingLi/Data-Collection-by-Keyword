#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary library
import os
import pandas as pd


# In[2]:


#Extract all the file name
fileList = []
path = 'data'
for root, dirs, files in os.walk(path):
    for fileName in files:
        if fileName.endswith(".csv"):
            fileList.append(os.path.join(root, fileName))


# In[3]:


keyword = "administrat" # search by the keyword 

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_adm = df.loc[df['Keyword'] == 1, :]
    df_adm.to_csv('FOIA_administration.csv', mode = 'a', header = False)

df_adm=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_administration.csv', header=None, error_bad_lines=False) 
df_adm.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[4]:


keyword = "Administrat"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Adm = df.loc[df['Keyword'] == 1, :]
    df_Adm.to_csv('FOIA_Administration.csv', mode = 'a', header = False)
    
df_Adm=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Administration.csv', header=None, error_bad_lines=False) 
df_Adm.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[5]:


keyword = "invent"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_inv = df.loc[df['Keyword'] == 1, :]
    df_inv.to_csv('FOIA_inventory.csv', mode = 'a', header = False)
    
df_inv=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_inventory.csv', header=None, error_bad_lines=False) 
df_inv.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[6]:


keyword = "Invent"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Inv = df.loc[df['Keyword'] == 1, :]
    df_Inv.to_csv('FOIA_Inventory.csv', mode = 'a', header = False)
    
df_Inv=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Inventory.csv', header=None, error_bad_lines=False) 
df_Inv.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[7]:


keyword = "wast"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_wtg = df.loc[df['Keyword'] == 1, :]
    df_wtg.to_csv('FOIA_wastage.csv', mode = 'a', header = False)
    
df_wtg=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_wastage.csv', header=None, error_bad_lines=False) 
df_wtg.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[8]:


keyword = "Wast"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Wtg = df.loc[df['Keyword'] == 1, :]
    df_Wtg.to_csv('FOIA_Wastage.csv', mode = 'a', header = False)
    
df_Wtg=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Wastage.csv', header=None, error_bad_lines=False) 
df_Wtg.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[9]:


keyword = "distribut"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_dtb = df.loc[df['Keyword'] == 1, :]
    df_dtb.to_csv('FOIA_distribution.csv', mode = 'a', header = False)
    
df_dtb=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_distribution.csv', header=None, error_bad_lines=False) 
df_dtb.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[10]:


keyword = "Distribut"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Dtb = df.loc[df['Keyword'] == 1, :]
    df_Dtb.to_csv('FOIA_Distribution.csv', mode = 'a', header = False)
    
df_Dtb=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Distribution.csv', header=None, error_bad_lines=False) 
df_Dtb.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[11]:


keyword = "allocat"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_alc = df.loc[df['Keyword'] == 1, :]
    df_alc.to_csv('FOIA_allocation.csv', mode = 'a', header = False)
    
df_alc=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_allocation.csv', header=None, error_bad_lines=False) 
df_alc.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[12]:


keyword = "Allocat"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Alc = df.loc[df['Keyword'] == 1, :]
    df_Alc.to_csv('FOIA_Allocation.csv', mode = 'a', header = False)
    
df_Alc=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Allocation.csv', header=None, error_bad_lines=False) 
df_Alc.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[13]:


keyword = "ship"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_shp = df.loc[df['Keyword'] == 1, :]
    df_shp.to_csv('FOIA_shipping.csv', mode = 'a', header = False)
    
df_shp=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_shipping.csv', header=None, error_bad_lines=False) 
df_shp.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[14]:


keyword = "Ship"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Shp = df.loc[df['Keyword'] == 1, :]
    df_Shp.to_csv('FOIA_Shipping.csv', mode = 'a', header = False)
    
df_Shp=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Shipping.csv', header=None, error_bad_lines=False) 
df_Shp.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[15]:


keyword = "Pfizer"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Pfz = df.loc[df['Keyword'] == 1, :]
    df_Pfz.to_csv('FOIA_Pfizer.csv', mode = 'a', header = False)
    
df_Pfz=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Pfizer.csv', header=None, error_bad_lines=False) 
df_Pfz.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[16]:


keyword = "pfizer"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_pfz = df.loc[df['Keyword'] == 1, :]
    df_pfz.to_csv('FOIA_pfizer.csv', mode = 'a', header = False)
    
df_pfz=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_pfizer.csv', header=None, error_bad_lines=False) 
df_pfz.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[17]:


keyword = "Moderna"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Mdn = df.loc[df['Keyword'] == 1, :]
    df_Mdn.to_csv('FOIA_Moderna.csv', mode = 'a', header = False)
    
df_Mdn=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Moderna.csv', header=None, error_bad_lines=False) 
df_Mdn.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[18]:


keyword = "moderna"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_mdn = df.loc[df['Keyword'] == 1, :]
    df_mdn.to_csv('FOIA_moderna.csv', mode = 'a', header = False)
    
df_mdn=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_moderna.csv', header=None, error_bad_lines=False) 
df_mdn.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[19]:


keyword = "Janssen"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Jan = df.loc[df['Keyword'] == 1, :]
    df_Jan.to_csv('FOIA_Janssen.csv', mode = 'a', header = False)
    
df_Jan=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Janssen.csv', header=None, error_bad_lines=False) 
df_Jan.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[20]:


keyword = "janssen"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_jan = df.loc[df['Keyword'] == 1, :]
    df_jan.to_csv('FOIA_janssen.csv', mode = 'a', header = False)
    
df_jan=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_janssen.csv', header=None, error_bad_lines=False) 
df_jan.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[21]:


keyword = "Johnson"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_Jos = df.loc[df['Keyword'] == 1, :]
    df_Jos.to_csv('FOIA_Johnson.csv', mode = 'a', header = False)
    
df_Jos=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_Johnson.csv', header=None, error_bad_lines=False) 
df_Jos.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[22]:


keyword = "johnson"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_jos = df.loc[df['Keyword'] == 1, :]
    df_jos.to_csv('FOIA_johnson.csv', mode = 'a', header = False)
    
df_jos=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_johnson.csv', header=None, error_bad_lines=False) 
df_jos.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[23]:


keyword = "J&J"

for name in fileList:
    df = pd.read_csv(name, skiprows = 1)
    df['Keyword'] = 0
    
    try:
        for index, row in df.iterrows():
            if keyword in row['Request Description']:
                df['Keyword'].iloc[index] = 1
                    
    except:
        print("There might be some processing errors")
        
        
    df_JJ = df.loc[df['Keyword'] == 1, :]
    df_JJ.to_csv('FOIA_JJ.csv', mode = 'a', header = False)
    
df_JJ=pd.read_csv('/Users/arian/Python files/COVID project/FOIA_JJ.csv', header=None, error_bad_lines=False) 
df_JJ.columns=['','Request ID','Received Date','Requester Name','Organization','Request Description','']


# In[24]:


df_Adm=df_Adm.append(df_adm, ignore_index=True)
df_Inv=df_Inv.append(df_inv, ignore_index=True)
df_Wtg=df_Wtg.append(df_wtg, ignore_index=True)
df_Dtb=df_Dtb.append(df_dtb, ignore_index=True)
df_Alc=df_Alc.append(df_alc, ignore_index=True)
df_Shp=df_Shp.append(df_shp, ignore_index=True)
df_Pvd=df_Pfz.append(df_pfz, ignore_index=True)
df_Pvd=df_Pvd.append(df_Mdn, ignore_index=True)
df_Pvd=df_Pvd.append(df_mdn, ignore_index=True)
df_Pvd=df_Pvd.append(df_Jan, ignore_index=True)
df_Pvd=df_Pvd.append(df_jan, ignore_index=True)
df_Pvd=df_Pvd.append(df_Jos, ignore_index=True)
df_Pvd=df_Pvd.append(df_jos, ignore_index=True)
df_Pvd=df_Pvd.append(df_JJ, ignore_index=True)


# In[25]:


# check duplicated records by 'Request ID'
print(sum(df_Adm.duplicated(subset=['Request ID'])))
print(sum(df_Inv.duplicated(subset=['Request ID'])))
print(sum(df_Wtg.duplicated(subset=['Request ID'])))
print(sum(df_Dtb.duplicated(subset=['Request ID'])))
print(sum(df_Alc.duplicated(subset=['Request ID'])))
print(sum(df_Shp.duplicated(subset=['Request ID'])))
print(sum(df_Pvd.duplicated(subset=['Request ID'])))


# In[26]:


# Drop duplicates, and make sure no duplicates in new dataframe
df_Adm=df_Adm.drop_duplicates(subset=['Request ID'])
print(sum(df_Adm.duplicated(subset=['Request ID'])))
df_Inv=df_Inv.drop_duplicates(subset=['Request ID'])
print(sum(df_Inv.duplicated(subset=['Request ID'])))
df_Wtg=df_Wtg.drop_duplicates(subset=['Request ID'])
print(sum(df_Wtg.duplicated(subset=['Request ID'])))
df_Dtb=df_Dtb.drop_duplicates(subset=['Request ID'])
print(sum(df_Dtb.duplicated(subset=['Request ID'])))
df_Alc=df_Alc.drop_duplicates(subset=['Request ID'])
print(sum(df_Alc.duplicated(subset=['Request ID'])))
df_Shp=df_Shp.drop_duplicates(subset=['Request ID'])
print(sum(df_Shp.duplicated(subset=['Request ID'])))
df_Pvd=df_Pvd.drop_duplicates(subset=['Request ID'])
print(sum(df_Pvd.duplicated(subset=['Request ID'])))


# In[27]:


# export as a new excel file
new_file = pd.ExcelWriter('FOIA_keyword.xlsx', engine='xlsxwriter')

df_Adm.to_excel(new_file, sheet_name='Administration')
df_Inv.to_excel(new_file, sheet_name='Inventory')
df_Wtg.to_excel(new_file, sheet_name='Wastage')
df_Dtb.to_excel(new_file, sheet_name='Distribution')
df_Alc.to_excel(new_file, sheet_name='Allocation')
df_Shp.to_excel(new_file, sheet_name='Shipping')
df_Pvd.to_excel(new_file, sheet_name='Provider')

new_file.save()


# In[ ]:





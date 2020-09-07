#!/usr/bin/env python
# coding: utf-8

# In[25]:


from bs4 import BeautifulSoup
import urllib.request as req
import pandas as pd


# In[4]:


html = """

<html>
    <head>
            <meta charaset="utf-8">
            <title>キノコード
            </title>
    </head>
    <body>
            <h1>こんにちは</h1>
    </body>
</html>
"""


# In[5]:


html


# In[7]:


parse_html = BeautifulSoup(html,'html.parser')


# In[8]:


print(parse_html)


# In[9]:


url = "https://kino-code.com/python-scraping/"
response = req.urlopen(url)


# In[10]:


parse_html = BeautifulSoup(response,'html.parser')


# In[11]:


parse_html


# In[12]:


print(parse_html.title)


# In[13]:


print(parse_html.title.string)


# In[14]:


print(parse_html.find_all('a'))


# In[15]:


title_lists=parse_html.find_all('a')


# In[16]:


title_lists[1:10]


# In[17]:


title_lists[10].attrs['href']


# In[20]:


title_list=[]
url_list=[]

for i in title_lists:
    title_list.append(i.string)
    url_list.append(i.attrs['href'])


# In[21]:


title_list


# In[22]:


url_list


# In[26]:


df_title_url = pd.DataFrame({'Title':title_list, 'URL':url_list})


# In[27]:


df_title_url


# In[28]:


df_notnull = df_title_url.dropna(how='any')


# In[29]:


df_notnull 


# In[30]:


df_notnull['Title'].str.contains('Python超入門コース')


# In[35]:


df_contain_python = df_notnull[df_notnull['Title'].str.contains('Python超入門コース')]


# In[36]:


df_contain_python


# In[38]:


df_contain_python.to_csv('aaa.csv')
print("書き出し完了")


# In[ ]:





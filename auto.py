#!/usr/bin/env python
# coding: utf-8

# In[26]:



from selenium import webdriver
import time 
import pandas as pd


# In[27]:


USER = "test_user"
PASS = "test_pw"


# In[28]:


browser = webdriver.Chrome()
browser.implicitly_wait(3) #chromedriver起動するまでの時間
print("アクセスしました")


# In[29]:


#ログインページするサイトへアクセス

url_login = "https://kino-code.com/membership-login/"
browser.get(url_login)
time.sleep(3)
print("ログインページにアクセスしました")


# In[30]:


#テキストボックス入力

element = browser.find_element_by_id('swpm_user_name')
element.clear()
element.send_keys(USER)
element = browser.find_element_by_id('swpm_password')
element.clear()
element.send_keys(PASS)
print("フォーム送信")


# In[31]:


browser_from = browser.find_element_by_name("swpm-login")
time.sleep(3)
browser_from.click()
print("情報を入力してログインボタンを押しました")


# In[32]:


url = "https://kino-code.com/member-only/"
time.sleep(3)
browser.get(url)
print(url,":アクセス完了")


# In[33]:


#ダウンロードボタンをクリック
frm = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div/main/article/div/p[2]/button")
time.sleep(1)
frm.click()
print("ダウンロードボタンをクリック")


# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[576]:


import os
import re
import time
import datetime
import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup, Comment
from selenium import webdriver
from IPython.display import clear_output
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# In[515]:


def foreigner(html):
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    links = soup.find_all('p')
    # print(links)
    # <span itemprop="birthPlace">

    links = soup.find_all(['span'] , attrs = { 'itemprop' : 'birthPlace'})
    for link in links:
        for c in (link.descendants):
            aa = ((c.find_next('a')).attrs)
            if 'country=US' in aa['href']:
                return False
    return True


# ## Should exccute the chromedriver and get the page source

# In[519]:


def league(html):
    result = []
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    links = soup.find_all('div', attrs = {'class': 'leaderboard_wrapper' , 'id': 'all_leaderboard'})

    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    for comment in comments:
        a = comment.find('div_leaderboard')
        if (a != -1):
            #print(a,comment)
            break
            
    ts = BeautifulSoup(comment.string, 'html.parser')
    ts = ts.find_all('div', {'id' : 'leaderboard_all_league' , 'class' : 'data_grid_box'})
    for tt in ts:
        kk = tt.table.find_all('a')
        for k in kk:
            result.append((k.text))
    return result


# ## Should exceute the chromedriver and get the page source

# In[569]:


def allstar(html):
    result = []
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    links = soup.find_all('div', attrs = {'class': 'leaderboard_wrapper' , 'id': 'all_leaderboard'})

    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    for comment in comments:
        a = comment.find('div_leaderboard')
        if (a != -1):
            #print(a,comment)
            break
    ts = BeautifulSoup(comment.string, 'html.parser')
    ts = ts.find_all('div', {'id' : 'leaderboard_allstar' , 'class' : 'data_grid_box'})
    for tt in ts:
        kk = tt.table.find_all('a')
        for k in kk:
            result.append((k.text))
            
    result = list(map (lambda x : str(int(x.split()[0])-1 ) + '-' + (x.split()[0][2:])  , result))
    return result


# In[530]:


def Hall(html):
    soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    links = soup.find_all('li' , {'class'  : 'bling_special bling_hof'})
    for link in links:
        if link.text == "Hall of Fame":
            return True


# In[589]:




def btn_click(wd,url):
    wd.get(url)
    script = "vjs_addClass(document.getElementById('leaderboard_allstar'),'show_all')"
    script2 = "vjs_addClass(document.getElementById('leaderboard_allleague'),'show_all')"
    btn = wd.execute_script(script)
    btn = wd.execute_script(script2)
    return(wd.page_source)



def get_all_info(url):
    # chrome_options.add_argument("--headless") # make the chrome invisible
    chrome_options = Options() 
    chrome_options.add_argument("--window-size=100x10")
    wd = webdriver.Chrome(options=chrome_options)
    html = btn_click(wd,url)
    aa = pd.Series([Hall(html) ,league(html), allstar(html), foreigner(html)])
    return (aa)

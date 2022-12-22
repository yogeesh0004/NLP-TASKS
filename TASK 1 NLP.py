#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download('brown')


# In[2]:


from nltk.corpus import brown
brown.categories()


# In[3]:


brown.words(categories='news')


# In[4]:


from nltk.corpus import inaugural


# In[5]:


inaugural.fileids()


# In[6]:


inaugural.words(fileids='2009-obama.txt')[:10]


# In[9]:


inaugural.words(fileids='2021-Biden.txt')[:10]


# In[ ]:





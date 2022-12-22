#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk


# In[2]:


#frequency distribution
text1='Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.'
fd=nltk.FreqDist(text1.split())
fd


# In[5]:


#conditional frequency distribution
from nltk.probability import ConditionalFreqDist
cfd=ConditionalFreqDist((len(word),word)for word in text1.split())
cfd[3]


# In[10]:


#CHINESE SEGMENTATION USING JEIBA
import jieba


# In[17]:


seg=jieba.cut("西渡機能意投立見堂御咲付支配密言月球。元応問容接二作時陸化権油方病見石戸祖存分。技山定速型異長意極女率提。輸中作多飛声海人意連将問防中前今貼地示。幡無授井周夕変辺関剤合皇激識横久載一。認手田味断議覧聞行日集彰弘。死政率無別築橋来虫出知戦責間工。購注易医上候口反極製最戦投図断質載。本各尚宗食力撃済点広回辺今君復美出亜。",cut_all = True)
print(" ".join(seg))


# In[12]:


# BASIC TEXT PROCESSING PIPELINE
import nltk
sent="Become an expert in NLP"
words=nltk.word_tokenize(sent)
print(word)


# In[21]:


texts="Kohli has been the recipient of multiple awards– most notably the Sir Garfield Sobers Trophy (ICC Men's Cricketer of the Decade): 2011–2020; Sir Garfield Sobers Trophy (ICC Cricketer of the Year) in 2017 and 2018; ICC Test Player of the Year (2018); ICC ODI Player of the Year (2012, 2017, 2018) and Wisden Leading Cricketer in the World (2016, 2017 and 2018). At the national level, he was awarded the Arjuna Award in 2013, the Padma Shri under the sports category in 2017 and the Rajiv Gandhi Khel Ratna award, the highest sporting honour in India, in 2018."
for text in texts:
    sentences=nltk.sent_tokenize(texts)
    for sentence in sentences:
        words=nltk.word_tokenize(sentence)
    print(words)
    tagged=nltk.pos_tag(words)
    print(tagged)


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Task 1


# In[26]:


def gender_features(word):
    return{'last_letter':word[-1]}


# In[2]:


gender_features('winston')


# In[8]:


from nltk.corpus import names
labeled_names=([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])


# In[10]:


import random
random.shuffle(labeled_names)


# In[11]:


featuresets=[(gender_features(n),gender)for(n,gender) in labeled_names]


# In[13]:


train_set,test_set=featuresets[500:],featuresets[:500]


# In[15]:


import nltk
classifier = nltk.NaiveBayesClassifier.train(train_set)


# In[21]:


classifier.classify(gender_features('David'))


# In[18]:


print(nltk.classify.accuracy(classifier,test_set))


# In[22]:


#Task 2


# In[24]:


import nltk
from nltk.tokenize import TweetTokenizer
text='The party was so fun:D #supenfun😀'
twtkn=TweetTokenizer()
twtkn.tokenize(text)


# In[25]:


#task 3


# In[ ]:





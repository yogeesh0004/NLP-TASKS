#!/usr/bin/env python
# coding: utf-8

# In[6]:


import nltk
sentence = [("the","DT"),("little","JJ"),("cat","NN"),("was","VV")]
grammar = "NP: {<DT.?,JJ>*<NN>}"
#production from CFG for NP and VP


# In[7]:


cp = nltk.RegexpParser(grammar)
result = cp.parse(sentence)
print(result)


# In[ ]:


result.draw()


# In[ ]:





# In[ ]:





# In[ ]:





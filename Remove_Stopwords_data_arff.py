#!/usr/bin/env python
# coding: utf-8

# In[16]:


import nltk
#nltk.download()


from nltk.corpus import stopwords

stop_words = set(stopwords.words('english')) 

with open("C:/Users/Usuario/dataTrainRaw.arff") as text:
    with open("C:/Users/Usuario/TrainRaw_noStopwords.arff", "w") as new_text:
        for sentence in text:
            filtered_words = [word for word in sentence.split() if word.lower() not in stop_words] 
            x = ' '.join(filtered_words)
            new_text.write(x + "\n")



    






# In[ ]:





# coding: utf-8

import pandas as pd  

data = pd.read_csv('test_labeled_mal.csv') 
data.pop('id')
data.to_csv("C:/Users/Usuario/test_labeled_bien.csv", index=False)







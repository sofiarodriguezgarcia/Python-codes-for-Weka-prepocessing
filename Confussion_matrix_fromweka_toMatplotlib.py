#!/usr/bin/env python
# coding: utf-8

# In[16]:


import matplotlib

cmat = np.array([[353, 24, 1, 2, 1, 7],
                       [103, 260, 3, 24, 1, 25],
                       [9, 3, 17, 0, 0, 0],
                       [70, 78, 0, 230, 4, 26],
                       [33, 32, 2, 2, 221, 9],
                       [46, 40, 3, 7, 4, 178]])
fig, ax = plot_confusion_matrix(
    conf_mat=cmat,
    cmap='Greens',
    class_names= ['DESC', 'ENTY', 'ABBR', 'HUM', 'NUM', 'LOC'],
    norm_colormap=matplotlib.colors.LogNorm()  
)


# In[ ]:





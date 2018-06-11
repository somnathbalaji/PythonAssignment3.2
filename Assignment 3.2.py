
# coding: utf-8

# # @author: Somnath Balaji
# # To Implement a Python program to generate all sentences where subject is in["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in["Baseball","cricket"].

# In[26]:


# Defining the objects as given in the hint
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

# Looping over each of the predicates
for x in subjects:
    for y in verbs:
        for z in objects:
            # Concatenating the loops by creating a new object and printing it
            a = x + ' ' + y + ' ' + k
            print (a)


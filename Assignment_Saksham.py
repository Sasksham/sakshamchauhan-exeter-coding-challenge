#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
start_time = time.time()
import pandas as pd
import re
import os, psutil
def textConversion():
    #-------Reading the text file-------------------------------------------------------
    with open ("t8.shakespeare.txt", "r+") as myfile:
        data = myfile.read().lower().strip()
    b=""
    for i in data:
        if i.isalnum() or i.isspace():
            b+=i
    #------Counting the occurence of the words-------------------------------------------
    def word_count(str):
        counts = dict()
        words = str.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        return counts
    g=word_count(b)
    #------Exporting the csv file containing the frequencies of different English words-----------
    tyu=pd.read_csv('french_dictionary.csv',header=None)
    tyu.rename(columns = {0:'English word',1:'French word'}, inplace = True)
    y=[]
    for i in tyu['English word']:
        for j in g.keys():
            if i == j:
                y.append(g[i])
    tyu['Frequency']=y
    tyu.to_csv("frequency.csv",index=False)
    #------Replacing the English words with French Words-------------------------------------------
    yp=b
    for i in range(len(tyu['English word'])):
        t=tyu['English word'][i]
        o=tyu['French word'][i]
        yp=re.sub(f" {t} | {t}\n | \n{t} |\n{t}\n| \n{t}\n |\n{t} | {t}\n",f" {o} ",yp)
    #-----Writing the converted text file-------------------------------------------------------------
    with open('t8.shakespeare.translated.txt', 'w') as f:
        f.write(yp)
textConversion()
#-----Checking the memory used and the time taken to process the code---------------------------------
print(psutil.Process(os.getpid()).memory_info().rss / 1024 ** 2)
print("--- %s seconds ---" % (time.time() - start_time))


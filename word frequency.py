# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 08:08:22 2020

@author: think
"""

import jieba
import csv
#loading data
text = open('train1.txt','r',encoding='utf-8').read()
len(text)
#let all words lower
text = text.lower()
#reading stopword
stwlist = [line.strip() for line in open( 'stopword.txt',encoding='utf-8').readlines() ] 
#getting splitted words
words = jieba.cut(text,cut_all = False,HMM = True)
#cut_all model
#HMM：HMM model
#deleting stopword and counting words frequency
word_ = {}
for word in words:
    if word.strip() not in stwlist:
        if len(word) > 1:
            if word != '\t':
                if word != '\r\n':
                    #word frequency
                    if word in word_:
                        word_[word] += 1
                    else:
                        word_[word] = 1
#save as tuple
word_freq = []
for word,freq in word_.items():
    word_freq.append((word,freq))
#listing the data by the number of word frequency
word_freq.sort(key = lambda x:x[1],reverse = True)
#get the first 200
for i in range(200):
    word,freq =word_freq[i]
    print('{0:10}{1:5}'.format(word,freq))   
with open('ur file.csv','wb') as out:
    csv_out=csv.writer(out)
    csv_out.writerow(['name','num'])
    for row in word_freq:
        csv_out.writerow(row)
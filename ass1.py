#!/usr/bin/env python
# coding: utf-8

# In[45]:


import numpy as np
import os
import collections

leng = 40
max_iter = 100
    
Global = 0
def arr_cr(s,digits):
    A = np.ones(digits)
    B = np.zeros(s-digits)
    C = np.concatenate((A, B), axis = 0)
    np.random.shuffle(C)
    return C

def Fval(val):
    return abs(13*val-170)

def ones(arr):
    return collections.Counter(arr)[1]
    

def nxtlist(array,size): 
    nxt_list = []
    for index in range(size):
        tmp = list(array)
        tmp[index] = 1 - array[index]
        nxt_list.append(tmp)
    return nxt_list

def HighFval(array):
    highval = 0
    for i in array:
        cnt = ones(i)
        val = Fval(cnt)
        if val > highval:
            highval = val
            highn = i
    return highn

ran_flag = True

while Global < max_iter:

    if ran_flag ==True:
        ran_vals = arr_cr(leng,np.random.randint(0,20))
        ran_flag = False
    else: 
        ran_vals = arr_cr(leng,np.random.randint(20,leng))
        ran_flag = True

    cnt1s = ones(ran_vals)
    Fvalue = Fval(cnt1s)

    local = 0
    while(local ==0 and (Global < max_iter)):  
        lst = nxtlist(ran_vals,leng)
        highn = HighFval(lst)
        cnt_high = ones(highn)
        highFvalue = Fval(cnt_high)
        if Fvalue < highFvalue:
            Fvalue = highFvalue
            ran_vals = highn
        else:
            local = 1
    if Global < 99:
        print(str(Fvalue) + ',',end='')
    else:
        print(Fvalue)
    Global += 1


# In[ ]:





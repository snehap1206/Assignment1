#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import os
import collections

leng = 40
max_iter = 100

Global = 0


def arr_cr(s, digits):
    P = np.ones(digits)
    Q = np.zeros(s - digits)
    R = np.concatenate((P,Q), axis=0)
    np.random.shuffle(R)
    return R


def Fval(val):
    fvalue = abs(13 * val - 170)
    return fvalue


def ones(count):
    countvalue = collections.Counter(count)[1]
    return countvalue


def nxtlist(array, size):
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

    if ran_flag == True:
        ran_vals = arr_cr(leng, np.random.randint(0, 20))
        ran_flag = False
    else:
        ran_vals = arr_cr(leng, np.random.randint(20, leng))
        ran_flag = True

    cnt1s = ones(ran_vals)
    Fvalue = Fval(cnt1s)

    local = 0
    while (local == 0 and (Global < max_iter)):
        lst = nxtlist(ran_vals, leng)
        highn = HighFval(lst)
        cnt_high = ones(highn)
        highFvalue = Fval(cnt_high)
        if Fvalue < highFvalue:
            Fvalue = highFvalue
            ran_vals = highn
        else:
            local = 1
    if Global < 99:
        print(str(Fvalue) + ',', end='')
    else:
        print(Fvalue)
    Global += 1


# In[6]:


import numpy as np
import os
import collections


class HillClimbing:
    """ 
    Initializing the constants 
    STRING_LENGTH and NUMBER_OF_ITERATIONS 
    """
    def __init__(self):
        self.STRING_LENGTH = 40
        self.MAX = 100
    
    """ 
    The below function creates a random array of 0's and 1's
    given the array size and how many ones you want in that array   
    """
    def CreateRandomArray(self,arsize,ones):
        A = np.ones(ones, dtype=np.int)
        B = np.zeros(arsize-ones, dtype=np.int)
        C = np.concatenate((A, B), axis = 0)
        # print(C)
        np.random.shuffle(C)
        return C
    
    """ 
    The below function calculates the fitness value for the given random array
    It counts the number of 1's in the given array and applies that in the function and returns
    the fitness value 
    """
    def CalculateFitness(self,onescount):
        return abs(13*onescount-170)

    def getOnesCount(self,arr):
        return collections.Counter(arr)[1]
    
    """ 
    Given an array of length asize this function returns a array list of 
    one bit changed neighbours of length asize 
    """
    def getNeighbours(self,arr,asize): 
        neighbours = []
        for index in range(asize):
            temparr = list(arr)
            temparr[index] = 1 - arr[index]
            neighbours.append(temparr)
        return neighbours
    
    """ 
    Given a array list of arrays 
    this function returns calculates Fitness value for each array in the list and 
    returns the largest fitness value 
    """
    def GetLargestFV(self,arr):
        largestFV = 0
        for a in arr:
            currentOnesCount = self.getOnesCount(a)
            currentFV = self.CalculateFitness(currentOnesCount)
            if currentFV > largestFV:
                largestFV = currentFV
                largestVN = a
        return largestVN

def main():
    hc = HillClimbing()
    #reset the algorithm for MAX times
    t = 0
    while t < hc.MAX:
        """
        Selection of random array with zero's and one's evenly distributed to get the 
        Global maximum value and Local Maximum value
        """
        if t%2 == 0:
            randomVC = hc.CreateRandomArray(hc.STRING_LENGTH,np.random.randint(0,20))
        else: 
            randomVC = hc.CreateRandomArray(hc.STRING_LENGTH,np.random.randint(20,hc.STRING_LENGTH))
        """
        Calculating the number of ones for the random VC and Evaluating the fitness value 
        for VC
        """
        randomOnescount = hc.getOnesCount(randomVC)
        funtionvalueRandomVC = hc.CalculateFitness(randomOnescount)

        local = False
        while(not(local) and (t < hc.MAX)):  
            neighbours = hc.getNeighbours(randomVC,hc.STRING_LENGTH)
            largestVN = hc.GetLargestFV(neighbours)
            onesCountLargestVN = hc.getOnesCount(largestVN)
            functionValuelargestVN = hc.CalculateFitness(onesCountLargestVN)
            if funtionvalueRandomVC < functionValuelargestVN:
                funtionvalueRandomVC = functionValuelargestVN
                randomVC = largestVN
            else:
                local = True
        if t < 99:
            print(funtionvalueRandomVC,end='')
            print(',',end='')
        else:
            print(funtionvalueRandomVC)
        t += 1

if __name__=="__main__":
    main()


# In[ ]:





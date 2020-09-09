#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy
import os
import collections
from math import exp


leng = 50
max_iter = 200

Global = 0


    def arr_cr(s, digits):
        P = numpy.ones(digits)
        Q = numpy.zeros(s - digits)
        R = numpy.concatenate((P, Q), axis=0)
        numpy.random.shuffle(R)
        return R

    def Ffunction(count):
        fvalue = abs(14 * onescount - 190)
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


    # reset the algorithm for MAX times
    t = 0
    Temperature = 100
    randomVC = sa.CreateRandomArray(sa.STRING_LENGTH, np.random.randint(0, sa.STRING_LENGTH))


    randomOnescount = sa.getOnesCount(randomVC)
    functionvalueRandomVC = sa.CalculateFitness(randomOnescount)

    while t < sa.MAX:
        neighbours = sa.getNeighbours(randomVC, sa.STRING_LENGTH)
        """
        For each neighbour in the neighbours list and we calculating its fitness value and comparing 
        it with fitness value of randomVc and the new randomVC is updated based on two different conditions
        """
        for neighbour in neighbours:
            onescount = sa.getOnesCount(neighbour)
            functionValueneigbourVN = sa.CalculateFitness(onescount)
            expcalc = exp((functionValueneigbourVN - functionvalueRandomVC) / Temperature)
            if functionvalueRandomVC < functionValueneigbourVN:
                functionvalueRandomVC = functionValueneigbourVN
                randomVC = neighbour
            elif np.random.uniform(0, 1) < expcalc:
                functionvalueRandomVC = functionValueneigbourVN
                randomVC = neighbour
        # Print the output
        if t < (sa.MAX - 1):
            print(functionvalueRandomVC, end='')
            print(',', end='')
        else:
            print(functionvalueRandomVC)
        # Decrease the temperature by 5 percent
        Temperature = Temperature * 0.95
        # Increase the iteration by 1 until MAX
        t += 1


if __name__ == "__main__":
    main()


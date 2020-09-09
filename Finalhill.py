import numpy
import os
import collections

bits = 40
MAX = 100

Global = 0


def arr_cr(num, digits):
    tot_ones = numpy.ones(digits)
    tot_zeroes = numpy.zeros(num - digits)
    random_arr = numpy.concatenate((tot_ones, tot_zeroes), axis=None)
    numpy.random.shuffle(random_arr)
    return random_arr

def fun_val(val):
    f_value = abs(13 * val - 170)
    return f_value

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


def get_array_values(array):
    highval = 0
    for i in array:
        cnt = ones(i)
        val = fun_val(cnt)
        if val > highval:
            highval = val
            arr_val = i
    return arr_val


ran_flag = True

while Global < MAX:

    if ran_flag == True:
        ran_vals = arr_cr(bits, numpy.random.randint(0, 20))
        ran_flag = False
    else:
        ran_vals = arr_cr(bits, numpy.random.randint(20, bits))
        ran_flag = True

    cntls = ones(ran_vals)
    Fvalue = fun_val(cntls)

    local = 0
    while local == 0 and (Global < MAX):
        lst = nxtlist(ran_vals, bits)
        highn = get_array_values(lst)
        cnt_high = ones(highn)
        highFvalue = fun_val(cnt_high)
        if Fvalue < highFvalue:
            Fvalue = highFvalue
            ran_vals = highn
        else:
            local = 1

    if Global < 99:
        print(str(Fvalue) + ',', end='')
    else:
        print(Fvalue)
    Global = Global + 1

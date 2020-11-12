# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 16:58:27 2020

@author: koka5
"""

def out(i, res):
    if i < 10:    
        print("res" + str(i) + " " + ": |  | " + ''.join([str(elem) for elem in res]))
    else:
        print("res" + str(i) + ": |  | " + ''.join([str(elem) for elem in res]))

def minus(op1_, op2_):
    
    l1 = len(op1_)
    l2 = len(op2_)
    delta = 0
    if l1 >= l2:
        delta = l1 - l2
        for i in range(delta):
            op2_.insert(0, '0')
    else:
        delta = l2 - l1
        for i in range(delta):
            op1_.insert(0, '0')
    l_ = len(op1_)
    res = ['_' for _ in range(l_)]
    i = 0
    n = 0
    while (i < l_):
        out(i, res)
            
        if op1_[l_ - i - 1] == '0' and op2_[l_ - i - 1] == '0':
            res[l_ - i - 1] = '0'
        elif op1_[l_ - i - 1] == '1' and op2_[l_ - i - 1] == '0':
            res[l_ - i - 1] = '1'
        elif op1_[l_ - i - 1] == '1' and op2_[l_ - i - 1] == '1':
            res[l_ - i - 1] = '0'
        elif op1_[l_ - i - 1] == '0' and op2_[l_ - i - 1] == '1':
            res[l_ - i - 1] = '1'
            for n in range(l_ - i - 1):
                if op1_[l_ - i - 1 - n - 1] == '1' and op2_[l_ - i - 1 - n - 1] == '1':
                    res[l_ - i - 1 - n - 1] = '1'
                elif op1_[l_ - i - 1 - n - 1] == '0' and op2_[l_ - i - 1 - n - 1] == '0':
                    res[l_ - i - 1 - n - 1] = '1'
                elif op1_[l_ - i - 1 - n - 1] == '0' and op2_[l_ - i - 1 - n - 1] == '1':
                    res[l_ - i - 1 - n - 1] = '0'
                elif op1_[l_ - i - 1 - n - 1] == '1' and op2_[l_ - i - 1 - n - 1] == '0':
                    res[l_ - i - 1 - n - 1] = '0'
                    break
            i = i + n + 1
        i += 1
    print("res_ : |  | " + ''.join([str(elem) for elem in res]))
    return res

minus(list('1010110011001100110000100'),list('101011001100110011001101'))


# iter 0
#111110000110011001100110    -- op1 online        True
#111110000110011001100110    -- op1 programm      True
# iter 1
#1001011100110011001100100   -- op1 online        True
#1001011100110011001100100   -- op1 programm      True
# iter 2
#1000000110011001100101110   -- op1 online        True
#1110101001100110011001010   -- op1 programm      True
# iter 3
#1010110011001100110000100   -- op1 online        True
#111101100110011001100000    -- op1 programm      True


# iter 0
#10010111001100110011001     -- res online        True
#10010111001100110011001     -- res programm      True
# iter 1
#100000011001100110010111    -- res online        True
#100000011001100110010111    -- res programm      True
# iter 2
#10101100110011001100001     -- res online        True
#10101100110011001100001     -- res programm      True
# iter 3
#101011001100110010110111    -- res online        True
#101011001100110010110111    -- res programm      True
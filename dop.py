# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 23:24:19 2020

@author: koka5
"""
import struct
def float_to_bin(num):
    bits, = struct.unpack('!I', struct.pack('!f', num))
    return "{:032b}".format(bits)  

def div_mantis(mantisa_op1, mantisa_op2):
    print()
    len_mantisa_op1 = len(mantisa_op1)
    pice_of_mantisa_op1 = []
    c_op1_0 = 0
    for i in range(len_mantisa_op1):
        if mantisa_op1[len_mantisa_op1 - i - 1] == '0':
            c_op1_0 += 1
        elif mantisa_op1[len_mantisa_op1 - i - 1] == '1':
            break
    c_op2_0 = 0 
    len_mantisa_op2 = len(mantisa_op2)
    pice_of_mantisa_op2 = []
    for i in range(len_mantisa_op2):
        if mantisa_op2[len_mantisa_op2 - i - 1] == '0':
            c_op2_0 += 1
        elif mantisa_op2[len_mantisa_op2 - i - 1] == '1':
            break
    if c_op1_0 <= c_op2_0:
        for i in range(len_mantisa_op1):
            if mantisa_op1[len_mantisa_op1 - i - 1] == '0':
                pice_of_mantisa_op1.append('0')
                mantisa_op1.pop()
            elif mantisa_op1[len_mantisa_op1 - i - 1] == '1':
                break
        for i in range(len_mantisa_op2):
            if mantisa_op2[len_mantisa_op2 - i - 1] == '0':
                pice_of_mantisa_op2.append('0')
                mantisa_op2.pop()
            elif mantisa_op2[len_mantisa_op2 - i - 1] == '1':
                break
    elif c_op1_0 > c_op2_0:
        for i in range(c_op2_0):
            pice_of_mantisa_op1.append('0')
            mantisa_op1.pop()
            pice_of_mantisa_op2.append('0')
            mantisa_op2.pop()
            
    len_op1 = len(mantisa_op1)
    result = []
    x = mantisa_op1[0:len(mantisa_op2)].copy()
    z = 0
    print("man1 : |  | " + ''.join([str(elem) for elem in mantisa_op1]))
    print("man2 : |  | " + ''.join([str(elem) for elem in mantisa_op2]))
    while(len_op1 >= 0):
        print("iter ========= " + str(z))
        r = minus(x, mantisa_op2)
        result.append('1')
        co = 0
        rr = r.copy()
        for i in range(len(r)):
            if r[i] == '0':
                rr.pop(0)
            elif r[i] == '1':
                break
            
        for elem in rr:
            if elem == '1':
                co += 1  
        if co > 0:
            pass
        else:
            break
        try:
            rr.append(mantisa_op1[len(mantisa_op2) + 1])
        except:
            rr.append('0')
        
        counter_0 = 0
        for i in range(50):
            if count(rr) > count(mantisa_op2):
                break
            if count(rr) < count(mantisa_op2):
                try:
                    rr.append(mantisa_op1[len(mantisa_op2) + 1])
                except:
                    rr.append('0')
                counter_0 += 1
                result.append('0')

        x = rr
        if len(result) > 20:
            len_op1 = len_op1 - len(mantisa_op2) - counter_0 - 1
        z +=1
    print("res_ : |  | " + ''.join([str(elem) for elem in result]))
    result_ = result.copy()
    for i in range(len(result)):
        if result[len(result) - i - 1] == '0':
            result_.pop()
        elif result[len(result) - i - 1] == '1':
            break
    result_.pop(0)
    for i in range(23 - len(result_)):
        result_.append('0')
    return result_

def count(num):
    len_ = len(num)
    res = 0
    for i in range(len_):
        if num[len_ - i - 1] == '1':
            res += 2**i
    return res
   
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
    return res

def div(op1, op2):
    sign_op1 = op1[0]
    exp_op1 = op1[1:9]
    mantisa_op1 = op1[9:]
    mantisa_op1.insert(0, '1')
    sign_op2 = op2[0]
    exp_op2 = op2[1:9]
    mantisa_op2 = op2[9:]
    mantisa_op2.insert(0, '1')
    exp_res = 0
    sign_res = sign_op1
    
    l_ex_op1 = len(exp_op1) 
    res_op1 = 0        
    for i in range (l_ex_op1):
        if exp_op1[l_ex_op1 - i - 1] == '1':
            res_op1 += 2**i

    l_ex_op2 = len(exp_op2)
    res_op2 = 0
    for i in range (l_ex_op2):
        if exp_op2[l_ex_op2 - i - 1] == '1':
            res_op2 += 2**i

    if res_op1 > res_op2:
        exp_res = res_op1 - res_op2
    elif res_op1 < res_op2:
        exp_res = res_op2 - res_op1
    exp_res += 127
    res = div_mantis(mantisa_op1, mantisa_op2)
    res = count_reverse(exp_res) + res
    res.insert(0, sign_res)
    return res

def count_reverse(num):
    res = []
    while(num > 0):
        res.append(str(num % 2))
        num = num // 2
    res.reverse()
    return res
    


a = float_to_bin(62.1)
b = float_to_bin(2.7)
print("A   : |  | " + ''.join([str(elem) for elem in a]))
print("B   : |  | " + ''.join([str(elem) for elem in b]))
res = div(list(a),list(b))
print("RES : |  | " + ''.join([str(elem) for elem in res]))
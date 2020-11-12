# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:07:51 2020

@author: koka5
"""
from pathlib import Path
import struct

class Micro_Processor:
    def __init__ (self):
        self.n = 22
        self.first_reg = 1
        self.R = ['11001011101010100110011000110101',
                  '11001011101010100110011000110101',
                  '11001011101010100110011000110101',
                  '11001011101010100110011000110101',
                  '11001011101010100110011000110101',
                  '11001011101010100110011000110101',
                  '11001011101010100110011000110101',
                  '11001011101010100110011000110101']
        self.SP = 0
        self.PS = ''
        self.PC = 0
        self.TC = 0
        self.IR = ''
        self.first_bit = 0
        self.command = ''
        self.opperand = ''
        self.info()
        self.file_name = 'commands2.txt'
        print("Press enter")
        with open(Path(self.file_name), encoding = "utf-8", mode = 'r') as file:
            for self.line in file:
                self.line = self.line.split("\n")[0]
                line_ = self.line.split(" ")
                self.command = line_[0]
                try:
                    self.opperand = list(self.float_to_bin(float(line_[1])))
                except:
                    pass
                if self.command == "PUSH":
                    self.func_push(self.opperand)
                elif self.command == "DUP":
                    self.func_dup()
                elif self.command == "POP":
                    self.func_pop()
                elif self.command == "FADD":
                    self.func_fadd()
                elif self.command == "DIV":
                    self.func_div()

    def float_to_bin(self, num):
        bits, = struct.unpack('!I', struct.pack('!f', num))
        return "{:032b}".format(bits)    
    
    def info(self):
        print("Лабораторна робота №2")
        print("Киричека Миколи Павловича, К-21")
        print("Варіант 2 (f(x) = (a + b) / b)")
    
    def check_par(self):
        if self.first_bit == '0':
            self.PS = '+'
        else:
            self.PS = '-'
        self.TC += 1
        if self.TC > 2:
            self.TC = 1
    
    def stack_counter_plus(self):
        self.SP += 1
        
    def stack_counter_minus(self):
        self.SP -= 1
    
    def func_push(self, opp, con = 1):
        if con:    
            self.en_in()
            self.PC += 1
            self.IR = self.line
            self.check_par()
            self.print_table()
            self.en_in()
        self.R[self.SP] = opp
        self.first_bit = self.R[0][0]
        self.stack_counter_plus()
        if con:
            self.check_par()
            self.print_table()
    
    def func_dup(self):
        self.en_in()
        self.PC += 1
        self.IR = self.line
        self.check_par()
        self.print_table()
        self.en_in()
        self.R[self.SP] = self.R[self.SP-1].copy()
        self.stack_counter_plus()
        self.check_par()
        self.print_table()
    
    def func_pop(self, con = 1):
        if con:
            self.en_in()
            self.PC += 1
            self.IR = self.line
            self.check_par()
            self.print_table()
            self.en_in()
        self.stack_counter_minus()
        x = self.R[self.SP]
        if con:
            self.check_par()
            self.print_table()
        return x
    
    def func_fadd(self):
        self.en_in()
        self.PC += 1
        self.IR = self.line
        self.check_par()
        self.print_table()
        op1 = self.func_pop(0)
        op2 = self.func_pop(0)
        self.func_push(self.add(op1,op2),0)
        self.en_in()
        self.check_par()
        self.print_table()
    
    def add(self, op1, op2):
        sign_op1 = op1[0]
        exp_op1 = op1[1:9]
        mantisa_op1 = op1[9:]
        mantisa_op1.insert(0, '1')
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
            for i in range(res_op1 - res_op2):
                mantisa_op2.insert(0, '0')
                mantisa_op1.append('0')
            exp_res = exp_op1
        elif res_op1 < res_op2:
            for i in range(res_op2 - res_op1):
                mantisa_op1.insert(0, '0')
                mantisa_op2.append('0')
            exp_res = exp_op2

        res = self.add_mantis(mantisa_op1.copy(), mantisa_op2.copy())
        c_res = res.copy()
        l_res = len(res)
        for i in range(l_res):
            if res[i] == '0':
                c_res.pop(0)
            elif res[i] == '1':
                c_res.pop(0)
                break
        l_res = len(c_res)
        while (l_res > 23):
            c_res.pop()
            l_res = len(c_res)
        c_res = exp_res + c_res
        c_res.insert(0, sign_res)
        return c_res
        
    def add_mantis(self, mantisa_op1, mantisa_op2):
        l = len(mantisa_op1)
        i = 0
        res = mantisa_op2.copy()
        while(i < l):
            if mantisa_op1[l - i - 1] == '0' and mantisa_op2[l - i - 1] == '0':
                res[l - i - 1] = '0'
            elif mantisa_op1[l - i - 1] == '0' and mantisa_op2[l - i - 1] == '1':
                res[l - i - 1] = '1'
            elif mantisa_op1[l - i - 1] == '1' and mantisa_op2[l - i - 1] == '0':
                res[l - i - 1] = '1'
            elif mantisa_op1[l - i - 1] == '1' and mantisa_op2[l - i - 1] == '1':
                res[l - i - 1] = '0'
                for j in range(l - i - 1):
                    if mantisa_op1[l - i - j - 2] == '0' and mantisa_op2[l - i - j - 2] == '0':
                        res[l - i - j - 2] = '1'
                        i = l - (l - i - j - 2) - 1
                        break
                    elif mantisa_op1[l - i - j - 2] == '0' and mantisa_op2[l - i - j - 2] == '1':
                        res[l - i - j - 2] = '0'
                    elif mantisa_op1[l - i - j - 2] == '1' and mantisa_op2[l - i - j - 2] == '0':
                        res[l - i - j - 2] = '0'
                    elif mantisa_op1[l - i - j - 2] == '1' and mantisa_op2[l - i - j - 2] == '1':
                        res[l - i - j - 2] = '1'
            i += 1
        return res    
        
    def func_div(self):
        self.en_in()
        self.PC += 1
        self.IR = self.line
        self.check_par()
        self.print_table()
        op1 = self.func_pop(0)
        op2 = self.func_pop(0)
        self.func_push(self.div(op1,op2),0)
        self.en_in()
        self.check_par()
        self.print_table()
    
    def div(self, op1, op2):
        sign_op1 = op1[0]
        exp_op1 = op1[1:9]
        mantisa_op1 = op1[9:]
        mantisa_op1.insert(0, '1')
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
        res = self.div_mantis(mantisa_op1, mantisa_op2)
        res = self.count_reverse(exp_res) + res
        res.insert(0, sign_res)
        return res
    
    def count_reverse(self, num):
        res = []
        while(num > 0):
            res.append(str(num % 2))
            num = num // 2
        res.reverse()
        return res
    
    def en_in(self):
        input()
        pass
    
    def div_mantis(self, mantisa_op1, mantisa_op2):
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
        while(len_op1 >= 0):
            r = self.minus(x, mantisa_op2)
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
                if self.count(rr) > self.count(mantisa_op2):
                    break
                if self.count(rr) < self.count(mantisa_op2):
                    try:
                        rr.append(mantisa_op1[len(mantisa_op2) + 1])
                    except:
                        rr.append('0')
                    counter_0 += 1
                    result.append('0')
    
            x = rr
            if len(result) > 22:
                len_op1 = len_op1 - len(mantisa_op2) - counter_0 - 1
            z +=1
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
       
    def minus(self,op1_, op2_):
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
        
    def count(self, num):
        len_ = len(num)
        res = 0
        for i in range(len_):
            if num[len_ - i - 1] == '1':
                res += 2**i
        return res
    
    def print_table(self):
        print("IR: |  | " + self.IR)
        print("R0: |  | " + ''.join([str(elem) for elem in self.R[0]]))
        print("R1: |  | " + ''.join([str(elem) for elem in self.R[1]]))
        print("R2: |  | " + ''.join([str(elem) for elem in self.R[2]]))
        print("R3: |  | " + ''.join([str(elem) for elem in self.R[3]]))
        print("R4: |  | " + ''.join([str(elem) for elem in self.R[4]]))
        print("R5: |  | " + ''.join([str(elem) for elem in self.R[5]]))
        print("R6: |  | " + ''.join([str(elem) for elem in self.R[6]]))
        print("R7: |  | " + ''.join([str(elem) for elem in self.R[7]]))
        print("SP: |  | " + str(self.SP))
        print("PS: |  | " + str(self.PS))
        print("PC: |  | " + str(self.PC))
        print("TC: |  | " + str(self.TC), end="")
        
proc = Micro_Processor()
print()
input("Press enter to exit")



# commands0   (23)
# my com: 01000001101101111111111111111110
# online: 01000001101110000000000000000000

# commands1   (5)
# my com: 01000000101001001001001001001000
# online: 01000000101000000000000000000000
    
# commands2   (3)
# my com: 01000000001111111111111111111110
# online: 01000000010000000000000000000000    
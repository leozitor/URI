# -*- coding: utf-8 -*-

import math
fatCalc = []
if __name__ == '__main__':
    while True:
        try:
            s = input()  # entrada
            n = len(s)
            letter = dict()  # dicionario dos caracteres
            total = 0
            num = 0  # numerador
            den = 1  # denominador
            for i in s:
                if i in letter.keys():
                   # print(" achou no dicionario a chave...")
                    letter[i] += 1  # soma ao numero de letras
                else:
                   # print("nao achou no dicionario a chave então adicionou ")
                    letter[i] = 1  # adicionou letra e
            #print(letter)
            #print("fatorial de 28",math.factorial(28))
            num = math.factorial(n)
            #print("numerador é", num)

            for i in letter:
                if letter[i] != 1:
                    temp = math.factorial(letter[i])
                    den *= temp
                    #print("parcial", den)
                    #print(temp)
            #print()
            #print("denominador é:",den)
            total = num // den
            total = total % 1000000007
            print(int(total))
        except EOFError:
            break

# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while True:
        try:
            lineList=[]
            s = input()
            cont = 0
            for i in range(len(s)):
                if s[i].isalpha():  # caracter diferente de espaco
                    if cont % 2 == 0:  # se ultima string adicionada for minusculo
                        # print(s[i].upper(), end="")
                        lineList.append(s[i].upper())
                    elif cont % 2 == 1:
                        # print(s[i].lower(), end="")
                        lineList.append(s[i].lower())
                    cont += 1  # quando le caracter incrementa contador
                else:
                    lineList.append(s[i])


            for i in lineList:
                print(i, end="")
            print()
        except EOFError:
            break

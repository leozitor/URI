# -*- coding: utf-8 -*-

def strToInt(s): # pega e troca o e O por 0 e l por 1
    st = []
    for i in s:
        if i == 'O' or i == 'o':
            st.append('0')
        elif i == 'l':
            st.append('1')
        else:
            st.append(i)
    return ''.join(st)

def strCheck(s):
    st=[]
    if s == "":
        return "error"
    s = strToInt(s)
    if s.isdigit():
        val = int(s)
        if val == 0:
            return '0'
        elif 0 <= val <= 2147483647:
            return s
        else:
            return "error"
    else:
        for i in s:
            if i == 'O' or i == 'o':
                st.append('0')
            elif i == 'l':
                st.append('1')
            else:
                st.append(i)
        return ''.join(st)


if __name__ == '__main__':
    while True:
        string = [] # string nova
        try:
            s = input().replace(" ", "").replace(",", "") # remove n e espacos
            #print("após remoção de virgula e espacos: {}".format(s))
            s = strCheck(s)
            #print("após transformar para inteiros: {}".format(s))
            if s == '0':
                print(s)
            elif s.isdigit():
                print(s.lstrip('0'))
            else:
                print("error")

            #print()
        except:
            break

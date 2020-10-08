if __name__ == '__main__':
    while True:
        s = input().split()
        if s == ['0','0']:
            quit()
        a, b = s[0], s[1]
        A = len(a)
        B = len(b)
        if B > A:   # se b for maior troca
            #print("trocou")
            temp = a
            a = b
            b = temp
            A = len(a)
            B = len(b)
        count = 0
        carry = 0
        if A == B: # se ambos tiverem mesmo tamanho
            i = 0
            while i < A:
                x = int(b[-i - 1]) + int(a[-i - 1])+ carry
                if x > 9:
                    carry = 1
                    count += carry
                else:
                    carry = 0
                i += 1
        else:  # se tamanho de a for menor que tamanho de b
            i = 0
            while i < B:
                #print(i)
                x = int(b[-i - 1]) + int(a[-i - 1]) + carry
                if x > 9:
                    carry = 1
                    count += carry
                else:
                    carry = 0
                i +=1
            #print("a[-i-1]:",a[-i-1])
            while i < A:
                if carry == 1 and int(a[-i-1]) == 9:
                    #print("entrou aqui e somou")
                    count += carry
                else:
                    break
                #print(i)
                i += 1
        if count == 0:
            print("No carry operation.")
        elif count == 1:
            print("1 carry operation.")
        else:
            print("{} carry operations.".format(count))

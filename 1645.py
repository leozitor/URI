if __name__ == '__main__':

    while True:

        s = input().split()
        n = int(s[0])
        k = int(s[1])

        A = [] # vetor de numeros
        cont = 0
        M = [None] * n
        for i in range(n):
            M[i] = [None] * n  # cria matriz

        if n == 0 and k == 0:
            break

        s = input().split()
        for i in s:
            A.append(int(i)) # vetor dos numeros

        for i in range(n):
            M[i][0] = 1

            for j in range(1, k):  # loop  do 1 até o tamanho de k
                M[i][j] = 0     # zero na primeira posicao

                for ii in range(i):  # loop até o i ultimo numero da linha
                    if A[ii] >= A[i]:   # se verifica que é maior já pula pra proxima iteração
                        continue
                    M[i][j] += M[ii][j-1] # contabiliza na posicao atual o valor da atual mais da anterior
            cont += M[i][k-1]
        print(cont)





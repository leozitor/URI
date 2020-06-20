
from collections import deque as dq


p = dq()# deque com pontos do gráfico
cont = 0
def peak(n):
    global cont
    if (p[n] > p[n - 1]) and (p[n] > p[n + 1]):
        cont += 1
    elif (p[n] < p[n - 1]) and (p[n] < p[n + 1]):
        cont += 1

if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:   # finaliza programa
            quit()
        else:
            cont = 0
            s = input().split()
            p = dq(map(int, s))  # reinicia deque
            p.appendleft(p[-1]), p.append(p[1])  # replicando ultima amostra no inicio do deque e a "antiga"(após insercao no inicio a primeira fica segunda) primeira amostra no fim
            #print("cont antes: {}".format(cont))
            for i in range(1, len(p) - 1):
                peak(i)
            #print("cont depois: {}".format(cont))
            print(cont)

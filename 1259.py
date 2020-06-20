# -*- coding: utf-8 -*-

import heapq as hp
if __name__ == '__main__':
        oddHeap = []  # lista de prioridade ímpar
        evenHeap = []  # lista de prioridade Par
        numbers = int(input())  # numero de entradas a seguir
        for _ in range(numbers):
            n = int(input())  # numero de entrada
            if n % 2 == 0:   # se número é par
                hp.heappush(evenHeap, n)
            else:  # item é ímpar
                hp.heappush(oddHeap, -n)
        while len(evenHeap) > 0:
            print(hp.heappop(evenHeap))
        while len(oddHeap) > 0:
            print(-hp.heappop(oddHeap))

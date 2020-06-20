from heapq import heappush, heappop


class Node:
    def __init__(self, num, mod):
        self.num = num
        self.mod = mod
        if (num & 1) == 0:
            self.even = True
        else:
            self.even = False

    def __lt__(a, b):
        if a.mod == b.mod:
            if a.even and b.even: # se ambos forem pares
                return a.num < b.num
            elif (a.even is False) and (b.even == False): # se ambos forem impares
                return b.num < a.num
            else:
                if a.even:  # apenas a for par
                    return False
                else: # se b for par
                    return True
        else:
            return a.mod < b.mod


heap = []

if __name__ == '__main__':
    while True:
        s = input()
        if s == "0 0":
            print("0 0")
            break
        s = s.split()
        N = int(s[0]) # recebe o N numero de inteiros
        M = int(s[1]) # recebe o M que sera o valor que sera feito o mod
        for _ in range(N):
            n = int(input())
            if n < 0 and n % M != 0:
                x = Node(n, -M + n % M)
            else:
                x = Node(n, n % M)  # instancia objeto
            heappush(heap, x)

        print("{} {}".format(N, M))
        for _ in range(len(heap)):
            j = heappop(heap)
            print(j.num)

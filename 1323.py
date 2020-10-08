# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while True:
        n = int(input())  # entrada
        total = 0  # valor total
        if n != 0:
            for i in range(n):
                j = n - i
                total += (n - j + 1)*(n - j + 1)

            print(total)
        else:
            quit()

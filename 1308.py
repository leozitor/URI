# -*- coding: utf-8 -*-

import math


def eq2(A, B, C):
    B = B * B # Bquadrado
    C = C * -2  # C passa para outro lado
    delta = B-(4*A*C) # calculo do delta
    raiz1 = (-1 * B + math.sqrt(delta)) / (2 * A)
    return raiz1
"""    
    if delta < 0:
        print("A equação não possui raizes reais.")
    elif delta == 0:
        raiz = (-1 * b + math.sqrt(delta)) / (2 * a)
        print("A equacao possui apenas uma raiz que e ", raiz)
    elif delta > 0:
        raiz1 = (-1 * b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-1 * b - math.sqrt(delta)) / (2 * a)
        print("As raizes da equacao sao ", raiz1, "e", raiz2)
"""


if __name__ == '__main__':
    n = int(input()) # casos de teste
    for _ in range(n):
        a = 1
        b = 1
        c = int(input())
        print(int(eq2(a, b, c)))

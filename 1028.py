def euclides_mdc(dividendo, divisor): #maximo divisor comum pelo metodo de euclides
    while divisor != 0:
        temp = divisor
        divisor = dividendo % divisor
        dividendo = temp
    return dividendo


if __name__ == '__main__':
    s = int(input())
    for _ in range(s):
        s = input().split()
        x = int(s[0])
        y = int(s[1])
        print(euclides_mdc(x, y))

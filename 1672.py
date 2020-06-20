import math

def func(n):
    return (n - (1 << (int)(math.log(n)/math.log(2)))) * 2 +1

if __name__ == '__main__':
    while True:
        s = input()
        if s == '00e0':
            break
        s = list(s)
        n = s[0] + s[1]
        dec = ""
        for i in range(int(s[3])):
            dec = dec + '0'
        n = int(n + dec) # transforma pra inteiro
        print(func(n))


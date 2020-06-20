def checkQuestion(s):
    vet = ["A", "B", "C", "D", "E"]
    cont = 0
    r = 0
    for i in range(len(s)):
        if s[i] <= 127:
            r = i
            cont +=1
    if cont == 1:
        return vet[r]
    else:
        return "*"

if __name__ == '__main__':
    n = -1
    while n != 0:
        n = int(input())
        eFlag = False
        for i in range(n):
            s = list(map(int, input().split()))
            print(checkQuestion(s))

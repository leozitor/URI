import math

grid = []  # grid matriz

def comb(p, n):
    #print("p:",p)
    #print("n:",n)
    if p <= 0:
        return 0
    else:
        N = math.factorial(n)
        D = math.factorial(p)
        D *= math.factorial(n-p)
        return (N//D) - 1

if __name__ == '__main__':
    s = input().split()  # entrada N e M já splitado
    N, M = int(s[0]), int(s[1])  # recebe N e M respc
    for _ in range(N):
        lin = input()  # recebe cada linha do grid
        grid.append(lin)

    # debug print do grid
    #print()
    #print(grid)
    #for i in grid:
        #print(i)
    # debug print do grid

    while True:
        try:
            p = 0  # p numero de casas preenchidas
            s = input().split()  # linhas já splitadas
            Xa, Ya, Xb, Yb = int(s[0]) - 1, int(s[1]) - 1, int(s[2]) - 1, int(s[3]) - 1  # variaveis dos teste dos quadrados já deslocados em 1 para se adequar aos vatores da matriz
            B = Xb - Xa + 1
            A = Yb - Ya + 1
            n = A * B  # n é o numero de casas totais
            for i in range(B):
                p += grid[i + Xa][Ya:Yb + 1].count('#')
                #print(grid[i + Xa][Ya:Yb + 1])

            total = comb(p,n) % 1000000007
            #print("resultado final é: ",int(total))
            print(int(total))
            # debug print das variaveis (Xa,Ya)  (Xb, Yb)
            #print(Xa)
            #print(Ya)
            #print(Xb)
            #print(Yb)
            # debug print das variaveis (Xa,Ya)  (Xb, Yb)

        except EOFError:
            break

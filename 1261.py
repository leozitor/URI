# -*- coding: utf-8 -*-

if __name__ == "__main__":
    roleHayPoint = dict() # criacao do dicionário de cargos
    s = input().split(" ")
    m = int(s[0])
    n = int(s[1])
    for _ in range(m):   # for para o  numero de cargos serem adicionados ao dicionario
        job = input().split()
        roleHayPoint[job[0]] = float(job[1]) # adicao do cargo no dicionário
    #print(roleHayPoint) # DEBUG
    for _ in range(n):
        totalSalary = 0.0  # salario
        s = ""
        x = ""
        while s != '.':
            s = input()
            if s != '.':
                x = x + " " + s
            #print(s) # DEBUG
        x = x.split()
        #print(x) # DEBUG
        for i in x:
            #print(i)
            if i in roleHayPoint:
                totalSalary += roleHayPoint[i]
                #print(i)
        print(int(totalSalary))

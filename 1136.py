if __name__ == '__main__':
    while True:
        s = input()
        if s == "0 0":  # condição de parada
            quit()
        s = s.split()

        n = int(s[0])
        b = int(s[1])
        stockGlobe = set()
        for i in range(n + 1):   # globo padrão
            stockGlobe.add(i)

        acmGlobe = set(map(int, input().split()))
        acmList = sorted(acmGlobe)  # lista do globo permanecente
        checkGlobe = stockGlobe - acmGlobe
        diffSet = set()
        #print("Globo padrão {}".format(stockGlobe))
        #print("Globo modificado ACM {}".format(acmGlobe))
        #print("Globo lista ACM {}".format(acmList))
        #print("Globo resultante {}".format(checkGlobe))

        if len(checkGlobe) == 0:
            print('Y')
        else:
            flag = False
            for i in range(len(acmList) - 1, 0, -1):
                # print(i)
                if flag is True:
                    break
                for j in range(i):
                    diff = acmList[i] - acmList[j]
                    if diff not in diffSet:
                        diffSet.add(acmList[i] - acmList[j])
                        if diff in checkGlobe:
                            checkGlobe.remove(diff)  # remove elemento do globo
                            if len(checkGlobe) == 0: # globo esta vazio portanto
                                flag = True
                                break
            #print("Globo diferencas {}".format(diffSet))
            if flag is True:
                print('Y')
            else:
                print('N')

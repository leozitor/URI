# -*- coding: utf-8 -*-

import heapq as hq
from sys import stdin

if __name__ == "__main__":
    dayCount = 1  # contador dos dias
    dragonLodge = []  # alojamento de dragões
    currentDragon = 0.0  # dragão sendo treinado atualmente
    totalFine = 0  # valor de multa
    for line in stdin:
        s = line
        # s = arq.read()
        s = s.split(" ")  # splita cada linha de entrada pelo tempo e  multa
        try:
            t = float(s[0])  # tempo
            f = float(s[1])  # multa
        except:
            break
        newDragon = [t / f, t, f, dayCount]  # insere na fila novos dragoes
        #  print("Dia:", dayCount)
        if currentDragon == 0:  # nenhum dragao sendo treinado
            #  print("nenhum dragão sendo treinado")
            if len(dragonLodge) == 0:
                currentDragon = newDragon
                #  print("insere dragao pra ser treinado", currentDragon)
            else:
                currentDragon = hq.heappushpop(dragonLodge, newDragon)
                #  print("insere dragao da fila pra ser treinado", currentDragon)
            totalFine += currentDragon[2] * (dayCount - currentDragon[3]) # calcula multa
            #  print("valor multa do dragão atual:",currentDragon[2])
            #  print("dia que o dragão atual entrou:", currentDragon[3])
            #  print("dia atual",dayCount)
            #  print("calculo",currentDragon[2] * (dayCount - currentDragon[3]))
        else:
            hq.heappush(dragonLodge, newDragon)
        currentDragon[1] -= 1  # decrementa dia de treinamento
        #  print(currentDragon)
        if currentDragon[1] == 0:
            currentDragon = 0  # dragao é removido do treinamento
        dayCount += 1
        #  print("fila de dragões", dragonLodge)
        #  print(totalFine)

    #  print("não vem mais dragao")
    while len(dragonLodge) != 0:
        # print("Dia:", dayCount)
        if currentDragon == 0:  # nenhum dragao sendo treinado
            currentDragon = hq.heappop(dragonLodge)
            totalFine += currentDragon[2] * (dayCount - currentDragon[3])  # calcula multa
            currentDragon[1] -= 1
            if currentDragon[1] == 0:
                currentDragon = 0  # dragao é removido do treinamento
            dayCount += 1
        else:  # tem dragão treinando
            valJump = currentDragon[1]  # pega o tempo restante
            currentDragon[1] -= valJump
            if currentDragon[1] == 0:
                currentDragon = 0  # dragao é removido do treinamento
            dayCount += valJump
        # print(totalFine)
        # print(dragonLodge)
    print(int(totalFine))

# -*- coding: utf-8 -*-

if __name__ == "__main__":
	n = int(input())  # numero de casos de teste
	for _ in range(n):
		flagDiff = 0 # flag de diferenca
		listLang = []
		k = int(input())  # numero de entradas
		for i in range(k):
			x = input() # entrada string
			if i != 0: # verificar o penultimo com o ultimo
				if listLang[-1] != x:
					#print("ativou flagDiff")
					flagDiff = 1 # ativa flag 1
			listLang.append(x)
		if flagDiff == 1:
			print("ingles")
		else:
			print(listLang[-1])

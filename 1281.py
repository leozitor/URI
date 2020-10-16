# -*- coding: utf-8 -*-

if __name__ == "__main__":
    n = int(input())  # quantidade de idas a feira
    for _ in range(n):
        productList = dict()  # lista de produtos dicionário
        totalPrice = 0.00  # preço total
        m = int(input())  #produtos disponiveis na feira
        for _ in range(m):
            product = input().split()  # produto e preço splitados
            #print("produtoNome=",product[0])
            #print("produtoPreço=", float(product[1]))
            #print()
            productList[product[0]] = float(product[1])  # adicionando produto e preço inserido no dicionário productList
        p = int(input()) # produtos a serem comprados
        for _ in range(p): # produtos que serão comprados
            product = input().split() # produto e precco splitados
            productName = product[0]
            productQuantity = int(product[1])
            #print("produtoNome=", product[0])
            #print("produtoQuantidade=", int(product[1]))
            #print()
            totalPrice = totalPrice + productQuantity * productList[productName]
        #print("R$", totalPrice)
        totalPrice = '%.2f' % totalPrice
        print("R$", totalPrice)

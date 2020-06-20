rank =[1, 3, 5, 10, 25, 50, 100]
if __name__ == '__main__':
    s = int(input())
    x = rank[0]
    cont = 0
    while x < s:
        cont += 1
        x = rank[cont]
    print("Top {}".format(rank[cont]))

w = []
v = []
W = 50
items = []

def totalvalue(comb):
    ' Totalise a particular combination of items'
    totwt = totval = 0
    for item, wt, val in comb:
        totwt += wt
        totval += val
    return (totval, -totwt) if totwt <= 50 else (0, 0)

def knapsack01_dp(items, limit):
    table = [[0 for w in range(limit + 1)] for j in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, wt, val = items[j - 1]
        for w in range(1, limit + 1):
            if wt > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - wt] + val)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            item, wt, val = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result

if __name__ == '__main__':
    n = int(input())  # valor de casos de teste
    for _ in range(n):
        pac = int(input())  # valor de pac de entradas de cada caso de teste

        items = []

        for i in range(pac):
            s = input().split()
            qt, peso = int(s[0]), int(s[1])  # entrada quantidade e peso
            l = [str(i), peso, qt]
            items.append(l)

        bagged = knapsack01_dp(items, 50)
        val, wt = totalvalue(bagged)
        print("{} brinquedos".format(val)) #saida

        print("Peso: {} kg".format(-wt))
        print("sobra(m) {} pacote(s)".format(len(items) - len(bagged)))
        print()

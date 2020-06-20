# -*- coding: utf-8 -*-

def deckBuilder(s):
    deck = []
    for i in range(s):
        deck.append('-')
    deck[0] = 'x'
    return deck

def shuffle(s, pos, half):
    if pos < half:
        s[pos] = '-'
        newPos = (2 * pos) + 1
        #print("posicao firs:", newPos)
        s[newPos] = 'x'
    else:
        s[pos] = '-'
        newPos = (2*pos)-(2*half)
        #print("posicao Second: ", newPos)
        s[newPos] = 'x'
    return s, newPos


if __name__ == '__main__':
    P = int(input())  # inteiro P par indicando numero de cartas do baralho
    deck = deckBuilder(P)  # construcao do deck
    half = int(len(deck) / 2)
    sdeck = deck[:]
    # print(deck)
    sdeck, pos = shuffle(sdeck, 0, half)  # deck que sera embaralhado ja faz primeiro embaralhamento
    # print(sdeck)
    count = 1  # portanto contador inicia como 1
    while deck[0] != sdeck[0]:  # embaralha enquanto os dois decks nao sao iguais
        sdeck, pos = shuffle(sdeck, pos, half)
        # print(sdeck)
        # print(pos)
        count += 1
    # print("n = ", P)
    # print("resp = ", count)
    print(count)

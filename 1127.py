# dicionario para retornar um numero por accord
accords = {'C': 0, 'B#': 0, 'Db': 1, 'C#': 1, 'D': 2, 'Eb': 3, 'D#': 3, 'E': 4, 'Fb': 4, 'F': 5, 'E#': 5, 'Gb': 6,
           'F#': 6, 'G': 7, 'Ab': 8, 'G#': 8, 'A': 9, 'Bb': 10, 'A#': 10, 'B': 11, 'Cb': 11}


def partial(pattern):
    """ Calculate partial match table: String -> [Int]"""
    ret = [0]

    for i in range(1, len(pattern)):
        j = ret[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = ret[j - 1]
        ret.append(j + 1 if pattern[j] == pattern[i] else j)
    return ret


def search(T, P):
    """
            KMP search main algorithm: String -> String -> [Int]
            Return all the matching position of pattern string P in S
            """
    part, ret, j = partial(P), [], 0

    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = part[j - 1]
        if T[i] == P[j]: j += 1
        if j == len(P):
            ret.append(i - (j - 1))
            j = 0

    return ret


def patternDistance(s):
    vet = []
    vet.append(s[0])
    for i in range(1, len(s)):
        sub = s[i] - s[i - 1]
        if sub >= 0:
            vet.append(sub)
        else:
            vet.append(12 + sub)
    return vet[1:]


if __name__ == '__main__':
    while True:
        s = input()  # entra de string
        if s == "0 0":
            quit()
        s = s.split()
        m, t = int(s[0]), int(s[1])
        mIn = input().split()
        tIn = input().split()
        music = []
        track = []
        patDist = []
        musicDist = []
        for i in range(len(mIn)):
            l = mIn[i]
            music.append(accords[l])

        for i in range(len(tIn)):
            l = tIn[i]
            track.append(accords[l])

        musicDist = patternDistance(music)
        patDist = patternDistance(track)

        # print("lista Cifras da música: ", music)
        # print("lista Trecho do padrão: ", track)
        # print("lista Cifras da música em distancia: ", musicDist)
        # print("lista Trecho da música em distancia: ", patDist)
        if len(search(musicDist, patDist)) > 0:
            print('S')
        else:
            print('N')


if __name__ == '__main__':
    while True:
        try:
            i = 0
            resto = 0
            s = input()  # entrada em string
            count = len(s)  # tamanho da entrada
            s = int(s)      # passa pra inteiro
            for j in range(count):
                i += 1
                resto = resto*10 + 1
            while True:
                resto = (resto*10 + 1)%s
                if resto == 0:
                    print(i + 1)
                    break
                i += 1
        except EOFError:
            break

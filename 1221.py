def is_prime(n):
    if n == 1:
        return "Prime"
    i = 2
    while i*i <= n:
        if n % i == 0:
            return "Not Prime"
        i += 1

    return "Prime"

if __name__ == '__main__':

    n = int(input())
    for _ in range(n):
        x = int(input())
        print(is_prime(x))

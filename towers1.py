def tower(n):
    if n == 0:
        return 0
    else:
        t = 2 * tower(n - 1) + 1
        return t

n = int(input('n ='))

print(tower(n))

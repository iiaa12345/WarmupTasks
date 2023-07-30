def l(n):
    if n == 0:
        return 1
    else:
        k = l(n - 1) + n
        return k

n = int(input('n ='))

print(l(n))

def jos(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        j = 2 * jos(n // 2) - 1
        return j
    elif n % 2 != 0:
        j = 2 * jos(n // 2) + 1
        return j

n = int(input('n = '))

print(jos(n))

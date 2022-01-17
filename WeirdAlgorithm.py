n = int(input('Type a number: '))
while n != 1:
    print(int(n), end=' ')
    if n % 2 == 0:
        n /= 2
    elif n % 2 != 0:
        n *= 3
        n += 1

def sg():
    from random import randint as ri
    y = []
    s = 0
    b = []
    for i in range(6):
        n = 55 - 6
        for j in range(3):
            t = ri(n // 2 - 10 , n // 2 + 10)
            d = n - t
            t = t - 4 if t % 4 == 0 else t // 4 * 4
            d = d - 4 if d % 4 == 0 else d // 4 * 4
            n = t + d
        s += n // 4
        if n == 36 :
            y.append('_____')
            b.append(1)
        elif n == 24 :
            y.append('__ __')
            b.append(1)
        elif n == 28 :
            y.append('_____')
            b.append(0)
        elif n == 32 :
            y.append('__ __')
            b.append(0)
        else:
            raise IndexError('%d'%n)
    k = 55 - s
    k %= 11
    if k <= 6 :
        g = 5 - (k - 1)
    else:
        g = 5 - (11 - k)
    b = b[::-1]
    ans = ''
    for i,j in enumerate(y[::-1]):
        ans += '     '
        if i == g :
            if b[i] == 1 :
                ans += '_____  <*' if j == '__ __' else '__ __  <*'
            else:
                ans += j + '  <'
        else:
            ans += j
        ans += '\n'
    return ans
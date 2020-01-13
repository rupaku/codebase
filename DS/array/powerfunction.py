'''
Implement pow(x, n) % d.

In other words, given x, n and d,

find (x^n % d)
'''


def pow(x, y, d):
    if (y == 0): return 1 % d
    temp = pow(x, int(y / 2), d)

    if (y % 2 == 0):
        return (temp * temp) % d
    else:
        if (y > 0):
            return (x * temp * temp) % d
        else:
            return ((temp * temp) / x) % d

x = 2
y = 3
d = 3
print(pow(x, y, d)) #2
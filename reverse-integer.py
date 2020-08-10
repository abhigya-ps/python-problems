def reverse(x):
    sign = [1, -1][x < 0]
    rev  = sign * int(str(abs(x))[::-1])
    return rev if -(2**31) - 1 < rev < (2**31) else 0

print(reverse(-120))

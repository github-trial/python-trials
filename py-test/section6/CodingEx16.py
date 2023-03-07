def sum_eo(n, t):
    """Sum even or odd in range
    """
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))

x = sum_eo(1, 'spam')
print(x)


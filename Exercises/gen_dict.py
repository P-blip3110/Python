def gen_dict(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i**2
    return d
    pass

print(gen_dict(5))
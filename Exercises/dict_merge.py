def dict_merge(d1,d2,d3):
    d_merged = {}
    for i in (d1, d2, d3):
        print(i)
        d_merged.update(i)
    return d_merged
    pass

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

print(dict_merge(d1, d2, d3))
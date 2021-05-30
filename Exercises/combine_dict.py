def combine_dict(d1,d2):
    for d in d2:
        if d in d1:
            d1[d] += d2[d]
        else:
            d1[d] = d2[d]
    return d1
    pass

d1 = {'a': 40, 'b': 80}
d2 = {'a': 30, 'b': 90, 'c': 23}
print (combine_dict(d1,d2))
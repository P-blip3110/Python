def unique_dict(d):
    li = []
    for v in d.values():
        li.append(v)
    return set(li)
    pass

print(unique_dict({'a': 1, 'b': 2, 'c': 1, 'd':3}))
d2 = {'a': 1, 'b': 2, 'c': 1, 'd':3}

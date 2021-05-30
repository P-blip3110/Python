import operator

def dict_sort(d):
    d_sorted = dict(sorted(d.items(), key=operator.itemgetter(1)))
    return d_sorted
    pass

print(dict_sort({'a': 3, 'b': 1, 'c': 2}))
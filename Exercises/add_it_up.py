def add_it_up(n):
    try:
        result = sum(range(n + 1))
    except TypeError:
        result = 0
    return result

    pass

print(add_it_up(10987340904385))
print(add_it_up(10.1))
print(add_it_up('Summer'))
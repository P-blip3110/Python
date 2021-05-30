def is_perfect_number(n):
    list = []
    for i in range(1, n):
        if n % i == 0:
            list.append(i)
    if sum(list) == n:
        return True
    return False



print(is_perfect_number(15))
print(is_perfect_number(6))
print(is_perfect_number(12))
print(is_perfect_number(100078888))
import math

def perfect_square(num):
    sq_rt = num ** (0.5)
    num_part = math.modf(sq_rt)
    if num_part[0]:
        return False
    return True
    pass

print(perfect_square(9))
print(perfect_square(8))
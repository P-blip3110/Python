import math

def power_of_2(num):
    log = math.log(num,2)
    num_part = math.modf(log)
    if num_part[0]:
        return False
    return True

print(power_of_2(4))
print(power_of_2(5))
print(power_of_2(8))
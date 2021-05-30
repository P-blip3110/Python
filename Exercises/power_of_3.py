import math

def power_of_3(num):
    log = math.log(num,3)
    num_part = math.modf(log)
    if num_part[0]:
        return False
    return True

print(power_of_3(27))
print(power_of_3(5))
print(power_of_3(8))

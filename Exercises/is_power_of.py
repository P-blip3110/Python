import math

def is_power_of(num, power):
    log = math.log(num, power)
    num_part = math.modf(log)
    if num_part[0]:
        return False
    return True
    
print(is_power_of(8,2))
print(is_power_of(9,2))
print(is_power_of(27,3))
import re
def count_code(str):
    result = re.findall('co[a-z]e', str)

    return len(result)

print (count_code('aaacobebbbcodeoijacooe'))
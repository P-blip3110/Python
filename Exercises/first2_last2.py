def first2_last2(str):
    if len(str) < 2:
        return ""
    else:
        return str[:2] + str[-2:]
    pass

print(first2_last2("w3resource"))
print(first2_last2("w3"))
print(first2_last2("w"))    
def str_swap(str1, str2):
    str1_swapped = str2[:2] + str1[2:]
    str2_swapped = str1[:2] + str2[2:]
    return str1_swapped + " " + str2_swapped
    pass

print(str_swap('abcui', 'xyzsfji'))
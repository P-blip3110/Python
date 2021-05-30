def count_char(str):
    chr_dict = {}
    for i in str:
        chr_dict[i] = chr_dict.get(i,0) + 1
    return chr_dict
    pass

print(count_char("google.com"))
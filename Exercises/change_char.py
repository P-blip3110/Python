def change_char(str):
    first_chr = str[0]
    str_rest = str[1:]
    print(first_chr)
    if first_chr in str_rest:
        return first_chr + str_rest.replace(first_chr, '$')
    pass

print (change_char('restart'))
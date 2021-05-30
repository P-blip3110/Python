def count_letters(word):
    dict_count = {}
	#li = []
    for i in word:
    	dict_count[i] = dict_count.get(i,0) + 1
    for k in dict_count:
        dict_count[k] = str(dict_count[k])
    dict_count = sorted(dict_count.items())
	#for key, value in dict_count.items():
    	#output_li.append((key,value))
    dict_count = [k+v for k,v in dict_count]
    return "".join(dict_count)
    


print(count_letters('abbcccddfffiiiiaaapppppppppiiiiiiadjcjjjjjjjjjjddddddlllllllllpppppppppdddddmmmmmmmmmmsssssssssssssssssssssooooooooooooooooooooooootttttttttttttttttttttttttttttttttttttt'))
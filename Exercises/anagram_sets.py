#1. take input: 
ang_list = ['cat', 'dog', 'god', 'bat', 'tab']
dict = {}
same_keys = []
rev_dict = {}
anagram_list = []

#2. covert to dictionary based on position and value:
#3. Sort the key values:
for key, value in enumerate(ang_list):
    dict[key] = "".join(sorted(value))

print(dict)

#4. Find out keys with similar values and group them together:
for key, value in dict.items():
    rev_dict.setdefault(value, set()).add(key)

print(rev_dict)

for key, value in rev_dict.items():
    same_keys.append(value)

print(same_keys)

#5 Convert same_key list element to list index values
for x in same_keys:
    temp_lst = []
    if type(x) in [set, list]:
        new_set = set()
        for y in x:
            new_set.add(ang_list[y])
        temp_lst.append(new_set)
    else:
        temp_lst.append(ang_list[x])
    
    anagram_list.extend(temp_lst)

print(anagram_list)





    
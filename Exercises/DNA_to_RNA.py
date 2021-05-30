seq = input().strip()
output_seq = ''
for i in seq:
    if i == 'G':
        output_seq += 'C'
    elif i == 'C':
        output_seq += 'G'
    elif i == 'T':
        output_seq += 'A'
    elif i == 'A':
        output_seq += 'U'
    else:
        output_seq = 'Invalid Input'
        break
print (output_seq)

#def DNA_to_RNA(seq, RNA_map):
    #transformed_seq = []
    #for i in seq:
        #if i in RNA_map:
            #transformed_seq.append(RNA_map[i])
        #else:
            #return ("Invalid Input")
    #return ("".join(transformed_seq))

#seq = list(input().strip())
#RNA_map = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
#print (DNA_to_RNA(seq, RNA_map))
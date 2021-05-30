def print_third(list):
    p = 2
    idx = 0
    lenli = len(list)
    while len(list):
        idx = (p+idx) % lenli
        print (list.pop(idx))
        lenli -= 1
    return 'executed'
    pass

print (print_third([10,20,30,40,50,60,70,80,90]))
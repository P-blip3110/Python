def list_elements_swap(li):
    temp = None
    for i in range(0,(len(li) - 1),2):
        temp = li[i]
        li[i] = li[i+1]
        li[i+1] = temp
    return li

print(list_elements_swap([0,1,2,3,4,5]))

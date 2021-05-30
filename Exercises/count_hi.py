def count_hi(str):
  count = 0
  li_str = list(str)
  for i in range(len(li_str)):
    if 'h' in li_str[i]:
        if 'i' in li_str[i+1:i+2]:
            count += 1
  
  return count
  

print (count_hi('hiHihi'))
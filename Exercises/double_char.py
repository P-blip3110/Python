def double_char(str):
  li_str = list(str)
  #print (li_str)
  return "".join([i*2 for i in li_str]) 

print(double_char('The'))
def make_chocolate(small, big, goal):
  if small + (big * 5) < goal:
    return -1
  elif big * 5 > goal:
    if goal % 5 <= small:
      return goal % 5
    return -1
  else:
    return goal - (big * 5)
  
print (make_chocolate(1, 2, 7))
print (make_chocolate(6, 1, 11))
print (make_chocolate(1000, 1000000, 5000006))
print (make_chocolate(7, 2, 13))
print (make_chocolate(4, 1, 10))
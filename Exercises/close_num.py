def close_far(a, b, c):
    #print (abs(b - a))
    #print (abs(c - a))
    return (abs(b - a) != abs(c - a) and abs(b - c) >= 2)

print (close_far(34,35,36))
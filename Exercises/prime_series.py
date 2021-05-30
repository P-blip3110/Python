def prime_series(n):
    for i in range(1,n+1):
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            print(i)
    return ('executed')


print (prime_series(10))

import time

start = time.time()

def findPair(A, sum):
    for i in A:
        for j in A[A.index(i):]:
            if i+j == sum:
                print (i,j)
            

end = time.time()

if __name__ == '__main__':
    A = [8, 7, 2, 5, 3, 1]
    sum = 10
    findPair(A, sum)
    print("time taken: ", end-start)
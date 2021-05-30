import time

start = time.time()

def findPair(A, sum):
    dict = {}
    for i, e in enumerate(A):
        if sum - e in dict:
            print("Pair found", (A[dict.get(sum - e)], A[i]))
            return
        dict[e] = i
    print("Pair not found")

end = time.time()

if __name__ == '__main__':
    A = [8, 7, 2, 5, 3, 1]
    sum = 10
    findPair(A, sum)
    print("time taken: ", end-start)


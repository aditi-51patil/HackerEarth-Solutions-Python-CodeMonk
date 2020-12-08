import random
import time
def partition(A,p,r):
    i=p-1
    x=A[r]
    for j in range(p,r):
        if(A[j]<x):
            i=i+1;
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def randomized_partition(A, p, r):
    q = random.randrange(p, r)
    A[q],A[r] = A[r],A[q]
    return partition(A,p,r)

def randomized_quicksort(A, p, r):
    # if len(A) == 1:
    #     return A
    if (p < r):
        q=partition(A, p, r)
        randomized_quicksort(A,p,q-1)
        randomized_quicksort(A,q+1,r)
def main():
    # arr = [int(x) for x in input().split()]
    A  = [random.randint(100, 10000) for iter in range(5000)]
    print(A)
    t0 = time.time()
    randomized_quicksort(A,0,len(A)-1)
    t1 = time.time()
    print(A)
    print(t1-t0)

if __name__ == "__main__":
    main()


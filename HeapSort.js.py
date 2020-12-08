import time
import random
def heapify(A,n,i):
    left=2*i+1
    right=2*i+2
    largest=i
    if(left<n and A[left]>A[largest]):
        largest=left;
    if(right<n and A[right]>A[largest]):
        largest=right;
    if(largest!=i):
        A[largest],A[i]=A[i],A[largest]
        heapify(A,n,largest)

def build_max_heap(A):
    n=int(len(A)/2)
    for i in range(n-1,-1,-1):
        heapify(A,len(A),i)

def heapsort(A):
    build_max_heap(A)
    for i in range(len(A)-1,0,-1):
        A[i],A[0]=A[0],A[i]
        heapify(A,i,0)

if __name__ == "__main__":
    A = [random.randint(100, 10000) for iter in range(5000)]
    print(A)
    t0 = time.time()
    heapsort(A)
    t1 = time.time()
    print(A)
    print(t1-t0)
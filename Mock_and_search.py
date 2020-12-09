'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
def lowerBound(A,num,start,end):
    while(start<end):
        mid=int((start+end)/2)
        if(A[mid]>=num):
            end=mid
        else:
            start= mid+1
    if(A[start]<num):
        return start+1
    return start
def upperBound(A,num,start,end):
    while(start<end):
        mid=int((start+end)/2)
        if(A[mid]<=num):
            start=mid+1
        else:
            end=mid
    if(A[start]>num):
        return start
    return start+1
if __name__ == "__main__":
    N=int(input())
    A=[int(x) for x in input().split()]
    A=sorted(A)
    Q=int(input())
    for i in range(0,Q):
        typ,x=[int(j) for j in input().split()]
        if(typ==0):
            ans = lowerBound(A,x,0,len(A)-1)
            print(N-ans)
        else:
            print(len(A)-upperBound(A,x,0,len(A)-1))
# for ln in range(Q):
#     print(ans[ln])
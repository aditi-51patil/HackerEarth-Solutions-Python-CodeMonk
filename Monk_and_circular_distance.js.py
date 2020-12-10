'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import math
def lowerBound(A,num,start,end):
    while(start<end):
        mid=int((start+end+1)/2)
        # print("start: ",start,"end: ",end,"mid: ",mid)
        if(A[mid]>num):
            end=mid-1
        else:
            start=mid
    if(A[start]>num):
        return start-1
    else:
        return start
# Write your code here
N=int(input())
p=[]
for i in range(N):
    x1,y1=[int(x) for x in input().split()]
    p.append(math.sqrt(x1**2 + y1**2))
q=int(input())
p=sorted(p)
for i in range(q):
    r=int(input())
    ans=lowerBound(p,r,0,N-1)+1
    print(ans)
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''
import math

# Write your code here
for _ in range(int(input())):
    N, l = input().split()
    A = [int(x) for x in input().split()]
    arr = [0] * 32;
    c = [0] * 32
    count = 0
    for i in range(32):
        for j in range(int(N)):
            if (1 << i & A[j]):
                arr[i] += 1;
        if (arr[i] != 0):
            count += 1
        c[i] = (1 << i) * arr[i]
    c = sorted(c, reverse=True)
    if (int(l) > count):
        print(-1)
    # elif(int(l)==0):
    #     print(1)
    else:
        l = int(l)
        j = l - 1, ans = 1, r = 0, k = 0;
        while (j >= 0 and c[j] == c[l - 1]):
            r + +1;
            j -= 1;
        j = l;
        while (j < 31 and c[j] == c[l - 1]):
            k += 1;
            j += 1;
        for i in range(k + 1, r + k + 1):
            ans *= i;
        for i in range(1, r + 1):
            ans /= i
        print(ans)
        # print("X")



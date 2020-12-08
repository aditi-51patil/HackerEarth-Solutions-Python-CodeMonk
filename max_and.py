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
    max_len = len(str(bin(max(A)))) - 2
    arr = []
    for i in range(max_len):
        count = 0
        for j in range(int(N)):
            temp = str(bin(A[j]))[2:][::-1]
            if (len(temp) > i):
                count += int(temp[i])
        arr.append(count * (2 ** i))
    arr = sorted(arr, reverse=True)
    if (int(l) > max_len):
        print(-1)
    elif (int(l) == 0):
        print(1)
    else:
        el = arr[int(l) - 1]
        el_ocr = arr.count(el)
        el_ind = arr.index(el)
        # if(el_ocr==1):
        #     print(1)
        # else:
        n = math.factorial(el_ocr)
        r = math.factorial(int(l) - el_ind)
        n_r = math.factorial(n - r)
        print(int(n / (n_r * r)))
        # print("X")



# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

T=int(input())
for pl in range(T):
    N,K = [int(x) for x in  input().split()]
    res = list(input().split())
    A=res[0]
    B=0
    C=0
    A=list(map(int,res[0]))
    itr=0
    occ=0
    f_ocr=0
    orig=0
    for i in range(0, N):
        face_value1 = (N - 1 - i);
        face_value_iterations1 = face_value1% N
        jh1 = 2 ** face_value_iterations1
        orig = orig + (A[i] * jh1)
    while(itr<N+1):
        itr += 1
        b=0;
        for i in range(0,N):
            face_value =(N-1-i);
            face_value_iterations = (face_value+itr)%N
            jh=2**face_value_iterations
            b=b+(A[i]*jh)
        print(b,"b")
        if(b>B):
            B=b
            C=0
            occ=itr
            f_ocr=itr
            print("f_ocr",f_ocr,"B",B)
        elif(B==b):
            print("f_ocr", f_ocr, "B", B,"C",C)
            C+=1
            if(C==1):
                occ=(itr-occ)
                print(C,"C",occ,"occ",B,"B")
    print(orig,"orig")
    if(C==0 and orig!=B):
        print(f_ocr+(K-1)*N)
    elif(C==0 and orig==B):
        print((K-1)*f_ocr)
    else:
        print(f_ocr+(K-1)*occ)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

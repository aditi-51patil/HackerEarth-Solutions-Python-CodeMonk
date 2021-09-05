def detectPattern(s1,s2):
    A=[]
    A1=""
    B=[]
    B1=""
    for i in s1:
        if(i not in A):
            A.append(i)
    for i in s1:
        A1=A1+str(A.index(i))
    for i in s2:
        if(i not in B):
            B.append(i)
    for i in s2:
        B1 = B1 + str(B.index(i))
    if(A1==B1):
        print("True")
        return True
    else:
        print("False")
        return False
detectPattern("xyy","abb")
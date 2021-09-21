n = int (input())
numList=list(map(int, input().split()))
def mergeSort(A):
    if len(A)<=1:
        return A
    else:
        mid=len(A)//2
        B=mergeSort(A[:mid])
        C=mergeSort(A[mid:])
        X=merge(B,C)
        # print(X)
        return X
def merge(B,C):
    D=[]
    while len(B)!=0 and len(C)!=0:
        a=B[0]
        b=C[0]
        if a<=b:
            D.append(a)
            B.remove(a)
        else:
            D.append(b)
            C.remove(b)
    if len(B)==0:
        for x in C:
            D.append(x)
    else:
        for z in B:
            D.append(z)
    # print(D)
    return D
j=1  
x=0
numList=mergeSort(numList)
for i in range(1,len(numList)):
    if numList[i-1] == numList[i]:
        j+=1
        if j>(len(numList)/2):
            x=1
            break
    else:
        j=1
print(x)

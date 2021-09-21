import random

def partition(a,l,r):
    m1=l
    m2=l
    pivot=a[l]
    for i in range(l+1,r+1):
        if a[i]<=pivot:
            a[i],a[m1]=a[m1],a[i]
            m1+=1
        elif a[i]==pivot:
            a[i],a[m2+1]=a[m2+1],a[i]
            m2+=1     
    return m1,m2

def randomizedQuickSort(a,l,r):
    if l>=r:
        return 
    k= random.randint(l,r)
    a[l],a[k]=a[k],a[l]
    m1,m2=partition(a,l,r)
    randomizedQuickSort(a,l,m1-1)
    randomizedQuickSort(a,m2+1,r)
n=int(input())
A=list(map(int, input().split()))
randomizedQuickSort(A,0,(len(A)-1))
for i in A:
    print(i,end=' ')

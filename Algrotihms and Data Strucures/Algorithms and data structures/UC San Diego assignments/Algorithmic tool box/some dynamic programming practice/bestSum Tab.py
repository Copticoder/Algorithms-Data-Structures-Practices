n=int(input())
x=[1,3,4]
def sumTab(n,numArray):
    newArr=[[0]]*(n+1)
    newArr[0]=[]
    for i in range(0,n):
        for j in range(len(numArray)):
                if newArr[i] !=[0]:
                    if i+numArray[j] < len(newArr):
                        temp=[*newArr[i], numArray[j]]
                        if len(temp)<len(newArr[i+numArray[j]]) or newArr[i+numArray[j]]==[0]:
                            newArr[i+numArray[j]]=temp
                else:
                    continue                        
    return newArr[-1]
print(len(sumTab(n,x)))

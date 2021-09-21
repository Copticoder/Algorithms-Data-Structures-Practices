n=8
x=[2,3,5]
def sunTab(n,numArray):
    newArr=[[0]]*(n+1)
    newArr[0]=[]
    for i in range(n):
        for j in range(len(numArray)):
            if newArr[i] !=[0]:
                if i+numArray[j] < len(newArr):
                    newArr[i+numArray[j]]=[*newArr[i], numArray[j]]
            else:
                continue
    return newArr[-1]
print(sunTab(n,x))
n=7
x=[5,3,4]
def sunTab(n,numArray):
    newArr=[False]*(n+1)
    newArr[0]=True
    for i in range(n):
        for j in range(len(numArray)):
            if newArr[i] != False:
                if i+numArray[j] < len(newArr):
                    newArr[i+numArray[j]]=True
            else:
                continue
    return newArr
print(sunTab(n,x))
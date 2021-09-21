n=int(input())
numbersList=[[] for _ in range(n + 1)]
numbersList[0],numbersList[1]=[0],[1]
numMulti=[2,3,1]
def addOrMultiply(temp,n):
    if len(temp)<len(numbersList[(n)]) or len(numbersList[(n)])==0:
        numbersList[(n)]=temp 
def dynamicCalculator(n,numMultiply):
    numOperations = [0]*(n+1)
    numOperations[0]=0
    numOperations[1]=1
    for i in range(1,n):
        for j in numMultiply:
            if j * i >= len(numOperations):
                continue

            if j !=1:
                numOperations[(j*i)]+=1
                temp=[*numbersList[i],(j*i)]
                addOrMultiply(temp,(j*i)) 
            else:
                numOperations[(i+j)]+=1
                temp=[*numbersList[i],(i+j)]
                addOrMultiply(temp,(j+i))
    return numOperations
dynamicCalculator(n,numMulti)
print(len(numbersList[-1])-1)
for z in numbersList[-1]:
    print(z,end=' ')
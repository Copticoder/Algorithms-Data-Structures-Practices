d=int(input())
m=int(input())
stopFill=int(input())
stopList=list(map(int, input().split()))
stopList.append(d)
stopList.insert(0,0)
lastRefill=0
currentRefill=0
numRefills=0
# print(stopList)
while currentRefill<=len(stopList)-2:
    lastRefill=currentRefill
    while currentRefill<=len(stopList)-2 and (stopList[currentRefill+1]-stopList[lastRefill])<=m:
        currentRefill=currentRefill+1
    if currentRefill==lastRefill:
        numRefills=-1
        break
    if currentRefill<=len(stopList)-2:
        numRefills+=1
    # print(currentRefill)
print(numRefills)
n=int(input())
windowNums=list(map(int,input().split(' ')))
m=int(input())
windowStack=[]
right=left=0
output=[]
while right < n:
    while windowStack and windowNums[windowStack[-1]]< windowNums[right]:
        windowStack.pop()
    windowStack.append(right)
    if left>windowStack[0]:
        windowStack.pop(0)
    if right+1 >=m:
        output.append(windowNums[windowStack[0]])
        left+=1
    right+=1
for j in output:
    print(j,end=' ')
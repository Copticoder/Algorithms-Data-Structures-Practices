n=int(input())
array=list(map(int,input().split(' ')))
swapList=[]
def swim(array,i):
    left=2*i +1
    right=2*i+2
    smallest=i
    if left < len(array) and array[left]<array[smallest]:
        smallest=left
    if right<len(array) and array[right]<array[smallest]:
        smallest=right
    if i != smallest:
        array[i],array[smallest]=array[smallest],array[i]
        swapList.append([i,smallest])
        swim(array,2*i +1)
for i in range(n-1//2 ,-1,-1):
    swim(array,i)
print(len(swapList))
for j in range(len(swapList)):
    print(swapList[j][0],swapList[j][1])

        
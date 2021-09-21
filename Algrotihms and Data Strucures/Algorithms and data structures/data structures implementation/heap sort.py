n=int(input())
array=list(map(int,input().split(' ')))
swapList=[]
def sink(size,wantedArray,i):
    largest =i
    left=2 * i
    right= 2* i +1
    if left <= size and wantedArray[left] > wantedArray[largest]:
        largest=left
    if right<=size and wantedArray[right] > wantedArray[largest]:
        largest=right
    if largest!=i:
        wantedArray[largest],wantedArray[i]= wantedArray[i],wantedArray[largest]
        sink(size,wantedArray,largest)

def heapSort(wantedArray):
    size=len(wantedArray)
    wantedArray.append(size)
    wantedArray[0],wantedArray[size]=wantedArray[size],wantedArray[0]
    for i in range(size//2,0,-1):
        sink(size,wantedArray,i)
    j=size
    while j:
        wantedArray[1],wantedArray[size]=wantedArray[size],wantedArray[1]
        size-=1
        sink(size,wantedArray,1)
        j-=1
    return wantedArray
print(heapSort(array))

#       10
#    9     3
# 2    8 1   5
# THE FUNNIEST SORTING ALGORITHM TILL NOW :DD <3 

# [19,14,28,15,16,7,27,15,21,21,5,2].
#              19
#         14       28
#      15    16  7    27
#   15  21 21 5 2
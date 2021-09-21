def countingSort(array):
    
    countingArray=[0]*5
    sortedArray=[0]*4
    j=len(array)-1

    for i in range(0,len(array)):
        countingArray[array[i]]+=1
    for z in range (1,len(countingArray)):
        countingArray[z]+=countingArray[z-1]
    while j>=0:
        sortedArray[countingArray[array[j]]-1]=array[j]
        countingArray[array[j]]-=1
        j-=1
    return sortedArray
listNums=[0,1,4,1]
print(countingSort(listNums))

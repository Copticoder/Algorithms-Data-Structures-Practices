numList = list(map(int, input().split()))
numList.remove(numList[0])
reqList = list(map(int, input().split()))
reqList.remove(reqList[0])


def binarySearch(num, low, high, array):
    if low <= high:
        mid = (low + high)//2
        if num == numList[mid]:
            return mid
        elif num > numList[mid]:
            return binarySearch(num, mid+1, high, array)
        elif num < numList[mid]:
            return binarySearch(num, low, mid-1, array)
    else:
        return -1


for i in reqList:
    print(binarySearch(i, 0, (len(numList)-1), numList), end=' ')

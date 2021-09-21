# numList=list(map(int, input().split()))
# numList.remove(numList[0])
# reqList=list(map(int, input().split()))
# reqList.remove(reqList[0])
# nums=[]
# i=0
# while i<len(reqList):
#     low=0
#     high=len(numList)-1
#     while low<high:
#         mid=((low+high)//2)
#         if numList[mid] > reqList[i]:
#             high=mid
#         elif numList[mid]<reqList[i]:
#             low = mid+1
#         else:
#             nums.append(mid)
#             break
#     if low == high:
#         nums.append(-1)
#     i+=1
#     low=0
#     high=len(numList)-1
# for i in nums:
#     print(i,end=' ')
# numList=list(map(int, input().split()))
numList=list(map(int, input().split()))
numList.remove(numList[0])
reqList=list(map(int, input().split()))
reqList.remove(reqList[0])
def binarySearch(num,low,high,array):
 if low <= high:
    mid = (low + high)//2
    if num==numList[mid]:
        return mid
    elif num > numList[mid]:
        return binarySearch(num,mid+1,high,array)
    elif num < numList[mid]:
        return binarySearch(num,low,mid-1,array)
 else:
    return -1
for i in reqList:
    print(binarySearch(i,0,(len(numList)-1),numList), end=' ')
        
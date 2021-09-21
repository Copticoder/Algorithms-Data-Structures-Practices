import numpy
def partitions(W, n, items):
    """ Finds if number of partitions having capacity W is >=3
    (int, int, list) -> (int) """
    count = 0 
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1

    if count < 3: print('0')
    else: print('1')

if __name__ == '__main__':
    n = int(input())
    item_weights = [int(i) for i in input().split()]
    total_weight = sum(item_weights)
    if n<3: 
        print('0')
    elif total_weight%3 != 0: 
        print('0')
    else:
        partitions(total_weight//3, n, item_weights)

























# n=int(input())
# sovs=list(map(int, input().split()))
# def partSov(dividand,sovs):
#     sovList=[[0]]*(dividand+1)
#     sovList[0]=[]
#     emptyList=sovList
#     finalList=[]
#     for l in range(0,2):  
#         for i in range (dividand):
#             for j in sovs:
#                     if sovList[i] !=[0]:
#                         if i+j <= dividand:
#                             if l!=2:
#                                 if j not in sovList[i+j] and j not in sovList[i]:
#                                     sovList[i+j]=[*sovList[i],j]
#                             else:
#                                 sovList[i+j]=[*sovList[i],j]
#         finalList.append(sovList[-1])
#         for x in sovList[-1]:
#             if x in sovs:
#                 sovs.remove(x)
#         sovList=[[0]]*(dividand+1)
#         sovList[0]=[]
#         # print(emptyList)
#         # print(finalsList)
#     return finalList
 
# dividandSovs=sum(sovs)%3
# if dividandSovs==0:
#     dividandSovs=sum(sovs)//3
#     counter=0
#     for z in partSov(dividandSovs,sovs):
#         if sum(z) == dividandSovs:
#             counter+=1
#     if counter ==2:
#         print(1)
#     else:
#         print(0)
# else:
#     print(0)
# print(partSov(dividandSovs,sovs))        







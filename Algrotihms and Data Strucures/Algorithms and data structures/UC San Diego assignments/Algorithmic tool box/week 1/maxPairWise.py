n=int(input())
numArray=list(map(int, input().split()))
numArray=sorted(numArray, reverse=True)
print(numArray[0]*numArray[1])
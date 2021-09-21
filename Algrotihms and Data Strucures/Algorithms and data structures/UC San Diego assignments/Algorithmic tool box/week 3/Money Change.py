x= int(input())
def getGreedy(x):
    i=0
    while x>0:
        if x>=10:
            x-=10
        elif x>=5 and x<10:
            x-=5
        elif x<5:
            x-=1
        i+=1
    return i
print(getGreedy(x)) 

            
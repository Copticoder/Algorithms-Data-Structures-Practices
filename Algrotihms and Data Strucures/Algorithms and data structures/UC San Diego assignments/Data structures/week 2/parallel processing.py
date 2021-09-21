class Thread:
    def __init__(self,index,time):
        self.index=index
        self.time=time
        
def compareThreads(first,scnd):
    if first.time != scnd.time:
        return first.time < scnd.time
    else:
        return first.index<scnd.index

def sink(i,threads):
    smallest=i
    left=2*i+1
    right=2*i +2
    if left <len(threads) and compareThreads(threads[left],threads[smallest]):
        smallest=left

    if right<len(threads) and compareThreads(threads[right],threads[smallest]):
        smallest=right

    if i!=smallest:

        threads[smallest],threads[i]=threads[i],threads[smallest]
        sink(smallest,threads)

m,*n=input().split(' ')
jobs=list(map(int,input().split(' ')))
m,n=int(m),int(*n)
threads = [0 for _ in range(m)]
result=[]

for i in range(m):
    threads[i]=Thread(i,0)

for job in jobs:
    threadIndex=threads[0].index
    threadTime=threads[0].time
    result.append([threadIndex,threadTime])
    threads[0].time += job
    sink(0,threads)
for x in result:
    print(x[0], x[1])
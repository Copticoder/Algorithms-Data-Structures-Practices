class ChainsHashing:
    def __init__(self,m):
        self.m=m
        self.hashList=[[]]
        for _ in range(m):
            self.hashList.append([])
        self.p=1000000007
        self.x=263

    def add(self,string):
        hashIndex=self.hashFunction(string)
        for i in self.hashList[hashIndex]:
            if i==string:
                return
        self.hashList[hashIndex].insert(0,string)

    def hashFunction(self,string):
        hash = sum((ord(string[j])*(self.x**j)) for j in range(len(string)))
        return (hash%self.p)%self.m


    def delete(self,string):
        hashIndex=self.hashFunction(string)
        if len(self.hashList[hashIndex]) <= 0:
            return 

        for i,text in enumerate(self.hashList[hashIndex]):
            if text == string:
                self.hashList[hashIndex].pop(i)
                return 

    def find(self,string):
        hashIndex=self.hashFunction(string)
        for i in self.hashList[hashIndex]:
            if i == string:
                return 'yes'
        return 'no'

    def check(self,stringIndex):
        return [j for j in self.hashList[stringIndex]]

mInput=int(input())
hashChain=ChainsHashing(mInput)
queryNum=int(input())
queryAns=[]

while queryNum:
    queryList=input().split(' ')
    if queryList[0] =='add':
        hashChain.add(queryList[1])
    elif queryList[0]=='find':
        queryAns.append(hashChain.find(queryList[1]))
    elif queryList[0]=='check':
        queryAns.append(hashChain.check(int(queryList[1])))
    else:
        hashChain.delete(queryList[1])
    queryNum-=1

for i in queryAns:
    if isinstance(i,list):
        for j in i:
            print(j,end=' ')
        print('')
    else:
        print(i)

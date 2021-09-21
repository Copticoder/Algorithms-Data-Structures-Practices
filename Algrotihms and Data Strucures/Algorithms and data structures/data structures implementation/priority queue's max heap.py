class MaxHeap:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = maxsize
        self.front=1 #first element is the size of heap while index 1 is the first heap element 
        
    def remove (self,i):
        self.swap(i,self.size)
        self.heap[self.size]=0
        self.size-=1
        if self.heap[i]>self.heap[self.parent(i)]:
            self.swim(i)
        else:
            self.sink(i)
    def swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    def parent(self,i):
        return i//2
    def leftChild(self,i):
        return 2*i 
    def rightChild(self,i):
        return 2*i +1

    def insert(self,i):
        if self.size >= self.maxsize:
            return 'reached max size of heap'
        self.size += 1
        
        self.heap[self.size] = i
        current = self.size
  
        while (self.heap[current] > 
               self.heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def sink(self,i):
        if i <= self.size and (
            self.heap[i] < self.heap[self.leftChild(i)]
            or self.heap[i] < self.heap[self.rightChild(i)]
        ):
            if self.heap[self.leftChild(i)]>self.heap[self.rightChild(i)]:
                self.swap(i,self.leftChild(i))
                self.sink(self.leftChild(i))
            else:
                self.swap(i,self.rightChild(i))
                self.sink(self.rightChild(i))
    def extractMax(self):
        self.swap(1,self.size)
        max= self.heap.pop(self.size)
        self.size-=1
        self.sink(1)
        return max 
    
    def swim(self,i):
        while i>1 and self.heap[i]>self.heap[self.parent(i)]:
            self.swap(self.heap[i],self.heap[self.parent(i)])
            i=self.parent(i)
    def changePriority(self,i,p):
        i+=1
        self.heap[i]=p
        if p>self.heap[self.parent(i)]:
            self.swim(i)
        else:
            self.sink(i)

firstHeap=MaxHeap(15)
firstHeap.insert(3)
firstHeap.insert(5)
firstHeap.insert(6)
firstHeap.insert(7)
firstHeap.insert(8)
firstHeap.insert(6)
print(firstHeap.heap)
print(firstHeap.extractMax())
print(firstHeap.heap)
firstHeap.remove(2)
print(firstHeap.heap)
firstHeap.changePriority(1,2)
print(firstHeap.heap)
#         8
#     7       3
#   6   2      
#       15
#   8        7
# 5   3   6




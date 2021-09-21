import ctypes
class DynamicArray(object):
    def __init__(self):
        self.n=0
        self.capacity=1
        self.A=self.make_array(self.capacity)
    def __len__(self):
        return self.n
    def __getitem__(self,k):
        if not 0 <= k < self.n:
            return IndexError('k out of bound')
        return self.A[k]
    def append(self,ele):
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n]=ele
        self.n+=1
    def insertAt(self,item,index):
        if not 0<= index<self.n:
            return IndexError('Index out of range')
        if self.n == self.capacity:
            self._resize(self.capacity*2)
        for i in range(self.n-1,index-1,-1):
            self.A[self.n+1]=self.A[self.n]
        self.A[index]=item
        self.n+=1    
    def delete(self):
        if self.n==0:
            print('array is empty deletion not possible')
            return 
        self.A[self.n-1]=0
        self.n-=1
    def removeAt(self,index):
        if self.n==0:
            print('array is empty deletion not possible')
            return        
        if not 0<= index<self.n:
            return IndexError('Index out of bounds')
        if self.index==self.n-1:
            self.A[self.n-1]=0
            self.n-=1
            return 
        for j in range(index,self.n-1):
            self.A[j]=self.A[j+1]
        self.A[self.n-1]=0
        self.n-=1
    def _resize(self,new_cap):
        B=self.make_array(new_cap)
        for z in range(self.n):
            B[z]=self.A[z]
        self.A=B
        self.capacity=new_cap
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()

newList=DynamicArray()
newList.append(2)
newList.insertAt(1,3)
print(newList.__getitem__(1))
class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        if len(self.storage)==0:
            self.storage.append(new_element)
        else:
            self.storage.append(0)
            for i in range(len(self.storage)-1,-1,-1):
                self.storage[i]=self.storage[i-1]
                if i==0:
                    self.storage[i]=new_element
        

    def peek(self):
        return self.storage[-1]
         

    def dequeue(self):
        if len(self.storage)==1:
            temp=self.storage[0]
            self.storage=[]
            return temp
        else:
            temp=self.storage[-1]
            self.storage=self.storage[:-1]
            return temp
        
    

q = Queue(1)
q.enqueue(2)
q.enqueue(3)

print (q.peek())


print (q.dequeue())


q.enqueue(4)

print (q.dequeue())

print (q.dequeue())

print (q.dequeue())

q.enqueue(5)

print (q.peek())

"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as 
few lines as possible.
Make sure you pass the test cases too!"""

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
        pass

    def peek(self):
        return self.storage[-1]
        pass 

    def dequeue(self):
        if len(self.storage)==1:
            temp=self.storage[0]
            self.storage=[]
            return temp
        else:
            temp=self.storage[-1]
            self.storage=self.storage[:-1]
            return temp
        pass
    
# Setup
# class Queue(object):
#     def __init__(self, head=None):
#         self.storage = [head]

#     def enqueue(self, new_element):
#         self.storage.append(new_element)

#     def peek(self):
#         return self.storage[0]

#     def dequeue(self):
#         return self.storage.pop(0)
q = Queue(1)
q.enqueue(2)
q.enqueue(3)
# print(q.storage)
# Test peek
# Should be 1
print (q.peek())

# Test dequeue
# Should be 1
print (q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
# print(q.storage)
print (q.dequeue())
# print(q.storage)
# Should be 3
print (q.dequeue())
# Should be 4   
# print(q.storage)
print (q.dequeue())
# print(q.storage)
q.enqueue(5)
# print(q.storage)
# Should be 5
print (q.peek())
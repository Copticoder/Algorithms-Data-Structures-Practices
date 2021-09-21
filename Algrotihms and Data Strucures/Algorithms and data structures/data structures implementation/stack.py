
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        new_element.next=self.head
        self.head=new_element
     

    def delete_first(self):
        if self.head:
            if self.head.next:
                current=self.head
                self.head=self.head.next
                return current.value
            else:
                current=self.head
                self.head=None
                return current.value
        else:
            return 'None'
        
      

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

  

    def pop(self):
        return self.ll.delete_first()
            
   
    

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)


stack = Stack(e1)

stack.push(e2)
stack.push(e3)
print (stack.pop())
print (stack.pop())
print (stack.pop())
print (stack.pop())
stack.push(e4)
print (stack.pop())

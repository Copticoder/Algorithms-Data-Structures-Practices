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
            
    def get_position(self, position):
        current=self.head
        counter =1 
        if self.head:
            while current.next and counter <position:
                current=current.next
                counter+=1
            
            return current.value 

    
    def insert(self, new_element, position):
        current=self.head
        counter=1
        if self.head:
                while counter<position and current.next:
                    if counter==position-1:
                        new_element.next=current.next
                        current.next=new_element
                
                    current=current.next
                    counter+=1

    
    
    def delete(self, value):
        current=self.head
        if self.head:
            if value == self.head.value:
                self.head = self.head.next
            else:
                while current.next.value != value:
                    current=current.next
                current.next=current.next.next




e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


print (ll.head.next.next.value)

print (ll.get_position(3))


ll.insert(e4,3)

print (ll.get_position(3))

ll.delete(1)

print (ll.get_position(1))

print (ll.get_position(2))

print (ll.get_position(3))

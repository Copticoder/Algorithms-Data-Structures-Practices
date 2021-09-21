"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev=None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            new_element.prev=current
        else:
            self.head = new_element
            
    def get_position(self, position):
        current=self.head
        counter =1 
        if self.head:
            while current.next and counter <position:
                current=current.next
                counter+=1
            
            return current 
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
    
    def insert(self, new_element, position):
        current=self.head
        counter=1
        if self.head:
                while counter<position and current.next:
                    if counter==position-1:
                        new_element.next=current.next
                        new_element.prev=current
                        current.next.prev=new_element
                        current.next=new_element
                
                    current=current.next
                    counter+=1
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        pass
    
    
    def delete(self, value):
        current=self.head
        if self.head:
            if value == self.head.value:
                self.head = self.head.next

            else:
                while current.next.value != value:
                    current=current.next
                current.next=current.next.next
                current.next.next.prev=current

        """Delete the first node with a given value."""
        pass

# Test cases
# Set up some Elements
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print (ll.head.next.value)
print(ll.head.next.prev.value)
print(ll.head.next.next.value)
print(ll.head.next.next.prev.prev.value)
# # Should also print 3
print (ll.get_position(3).value)

# # Test insert
ll.insert(e4,3)
# # Should print 4 now
print (ll.get_position(2).value)

# # Test delete
ll.delete(1)
# # Should print 2 now
print (ll.get_position(1).next.value)
# # Should print 4 now
print (ll.get_position(2).prev.value)
# # Should print 3 now
print (ll.get_position(3).prev.value)
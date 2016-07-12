# Write a LinkedList class. (Draw it out first, with empty list, and full list.)
# 1. Make a node class
# 2. Make a linkedlist class with head and tail
# 3. Make an add_node function
# 3a. Instantiate new node
# 3b. Point head to new_node if there is no head. 
# 3c. If there's a tail, point tail.next to new node.
# 3d. Then point tail to new node. 

class Node(object):

    def __init__(self, data):
        self.next = None
        self.data = data
    

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        # make node
        new_node = Node(data)

        # head points to node
        if self.head is None:
            self.head = new_node

        
        # tail points to node
        if self.tail is not None:
            self.tail.next = new_node

        self.tail = new_node


    def remove_node(self, data):

        #if head node has data, reassign head.
        if self.head is not None and self.head.data == data:
            self.head = self.head.next

        #If not, make current = self.head
        current = self.head

        #Look at current.next. If it has data, reassign current.next! 
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
            else:
                current = current.next


    def print_list(self):

        current = self.head
        while current is not None:
            print current.data
            current = current.next


    def find_node(self, data):
        """Return True if node in list."""

        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next

        return False

    def 



        

        




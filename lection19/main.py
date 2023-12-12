class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_el(self, data):  # sourcery skip: none-compare
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            
            while current_node.next is not None:
                current_node = current_node.next
                
            current_node.next = newNode
            
    def __str__(self):
        current_node = self.head
        tmp_list = []
        
        while current_node.next is not None:
            tmp_list.append(current_node.next)
            current_node = current_node.next
        
        tmp_list.append(current_node.next)
        
        return str(tmp_list)
    
    def find_el(self, data):
        current_node = self.head
        
        while current_node.next is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
            
    
    def remove(self, data):  # !!!NEED TO BE FIXED
        current_node = self.head
        previous_node = None
            
        while current_node.next is not None:
            if current_node.data == data:
                if previous_node is None:
                    self.head = current_node.next
                else:
                    previous_node = current_node
            current_node = current_node.next
    
    
linked_list = LinkedList()
    
class Node(): 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
# ...

from collections import deque 

linked_list = deque([1, "vdfvdv", 60])

print(linked_list)
print(linked_list[0])

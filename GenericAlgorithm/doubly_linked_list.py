from typing import Optional

class Node:
    def __inti__(self, data):
        self.data:Optional[Node] = data
        self.prev:Optional[Node] = None
        self.next:Optional[Node] = None


class DoublyLinkedList:
    
    def __init__(self):
        self.head:Node = None
        self.tail:Node = None
        
    def append(self, node:Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            
    def prepend(self, node:Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
    
    def delete(self, node:Node):
        if node.prev is None:
            self.head = node.next
            node.next.prev = None
            node.next = None
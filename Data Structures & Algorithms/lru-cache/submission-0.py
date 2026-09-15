class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.previous = None
        self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyMap = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.previous = self.head
        
    def remove(self, node):
        node.previous.next = node.next
        node.next.previous = node.previous

    
    def insert(self, node):
        self.tail.previous.next = node
        node.previous = self.tail.previous
        self.tail.previous = node
        node.next = self.tail
        

    def get(self, key: int) -> int:
        if key in self.keyMap:
            self.remove(self.keyMap[key])
            self.insert(self.keyMap[key])
            return self.keyMap[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyMap:
            self.remove(self.keyMap[key])
        self.keyMap[key] = Node(key, value)
        self.insert(self.keyMap[key])

        if len(self.keyMap) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.keyMap[lru.key]
        


class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.head
            while node:
                if node.val == key:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node.prev = self.tail
                    self.tail.next = node
                    self.tail = node
                    break
                node = node.next
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        
        new_node = Node(key, prev=self.tail)
        self.tail.next = new_node

        if len(self.cache) > self.capacity:
            self.head.next.prev = None
            self.head = self.head.next
            # leave old head to be GC? or remove it myself?
            del self.cache[key]
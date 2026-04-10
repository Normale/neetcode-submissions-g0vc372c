class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):
        node.prev = self.tail.prev
        node.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # refresh
            node = self.cache[key]
            self._remove(key)
            self._insert(key)
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # update
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert(node)
            return
        
        new_node = Node(value, prev=self.tail)
        self.cache[key] = new_node
        self._insert(new_node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]
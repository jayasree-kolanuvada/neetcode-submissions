# for this problem we use a dict to store key : node pairs and a dll to track the order of nodes. we need to make sure that each key has only one node and we use a dll over sll becasue when we remove nodes from the middle to add to the end we need access to the prev node in O(1) time which is only possible with a dll. we also make sure that the lru key is always at the front of the dll

class ListNode:

    def __init__(self, key, val, prev = None, nxt = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head, self.tail = ListNode(0,0), ListNode(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.capacity = capacity

    def insert(self, node):
        prev = self.tail.prev
        self.tail.prev, node.next = node, self.tail
        prev.next, node.prev = node, prev
    
    def remove(self, node):
        prev = node.prev
        prev.next, node.next.prev = node.next, prev
        
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = ListNode(key,value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.head.next
            del self.cache[lru.key]
            self.remove(lru)
        
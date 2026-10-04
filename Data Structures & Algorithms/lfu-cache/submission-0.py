# dict -> to store key : node pairs
# dict -> to store freq : list (dll) pairs
# keep track of current min freq in the cache

#keeps track of how our nodes are formed
class ListNode:
    def __init__(self,key,val,freq = 0):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

#this is to keep track of the lists in our freq : list map. we need a separate class for this becuase me need to keep track of many lists so it makes it easier to create and update different instances of linked lists
class LinkedList:
    def __init__(self):
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left
        self.size = 0

    def length(self):
        return self.size
    
    def insert(self,node):
        temp = self.right.prev
        self.right.prev, node.next = node, self.right
        node.prev, temp.next = temp, node
        self.size += 1
    
    def remove(self,node):
        prev, curr = node.prev, node.next
        prev.next, curr.prev = curr, prev
        node.prev = node.next = None
        self.size -= 1
    
    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.remove(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.order = collections.defaultdict(LinkedList)
        self.cap = capacity
        self.minFreq = 0
        
    
    # if key exists, update frequnecy, move node to next frequency
    # list, adjudt min freq if needed 
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            freq = node.freq
            self.order[freq].remove(node)
            if freq == self.minFreq and self.order[freq].length() == 0:
                self.minFreq += 1
            node.freq += 1
            self.order[freq+1].insert(node)
            return node.val
        return -1
            
        
    #if key exists, update value and treat like get op, else on 
    #adding new key, if capacity of cache exceeds pop leftmost 
    #element, insert new key into freq1 list and set min freq to 1
    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.order[node.freq].remove(node)
            if node.freq == self.minFreq and self.order[node.freq].length() == 0:
                self.minFreq += 1
            node.freq += 1
            self.order[node.freq].insert(node)
            return
        node = ListNode(key, value)
        self.cache[key] = node
        node.freq += 1
        if len(self.cache) > self.cap:
            node1 = self.order[self.minFreq].popLeft()
            del self.cache[node1.key]
        self.order[node.freq].insert(node)
        self.minFreq = 1

        

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


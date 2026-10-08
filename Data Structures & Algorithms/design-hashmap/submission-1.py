class ListNode:

    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.Map = [ListNode(0,0) for _ in range (10000)]
    
    def put(self, key: int, value: int) -> None:
        index = key%10000
        curr = self.Map[index]
        while curr.next:
            curr = curr.next
            if curr.key == key:
                curr.val = value
                return 
        curr.next = ListNode(key,value)
        return
        
    def get(self, key: int) -> int:
        index = key%10000
        curr = self.Map[index].next
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
        
    def remove(self, key: int) -> None:
        index = key%10000
        curr = self.Map[index]
        while curr.next and curr.next.key != key:
            curr = curr.next
        if not curr.next:
            return
        curr.next = curr.next.next
        return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
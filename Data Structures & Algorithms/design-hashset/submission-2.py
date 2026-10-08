class ListNode:

    def __init__(self, key=0):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.HashSet = [ListNode() for _ in range (10000)]
    
    def contains(self, key: int) -> bool:
        head = self.HashSet[key%10000].next
        while head:
            if head.key == key:
                return True
            head = head.next
        return False

    def add(self, key: int) -> None:
        index = key%10000
        curr = self.HashSet[index]
        while curr.next:
            curr = curr.next
            if curr.key == key:
                return 
        curr.next = ListNode(key)
        return

    def remove(self, key: int) -> None:
        index = key%len(self.HashSet)
        curr = self.HashSet[index]
        while curr.next and curr.next.key != key:
            curr = curr.next
        if not curr.next:
            return
        curr.next = curr.next.next 
        return
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
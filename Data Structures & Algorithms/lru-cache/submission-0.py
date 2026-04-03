class Node:
    def __init__(self, key, val):
        self.key,self.val=key,val
        self.pre=self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.m = {}
        self.right,self.left=Node(0, 0),Node(0, 0)
        self.right.pre=self.left
        self.left.next=self.right

    def remove(self, node: Node):
        node.pre.next=node.next
        node.next.pre=node.pre

    def insert(self, node: Node):
        node.next = self.right
        node.pre = self.right.pre
        self.right.pre.next = node
        self.right.pre = node

    def get(self, key: int) -> int:
        if not key in self.m:
            return -1
        self.remove(self.m[key])
        self.insert(self.m[key])
        return self.m[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.remove(self.m[key])
        self.m[key] = Node(key,value)
        self.insert(self.m[key])

        if len(self.m) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.m[lru.key]

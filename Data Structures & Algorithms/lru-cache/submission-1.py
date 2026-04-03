class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity
        self.m = OrderedDict()

    def get(self, key: int) -> int:
        if not key in self.m:
            return -1
        self.m.move_to_end(key)
        return self.m[key]

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m.move_to_end(key)
        self.m[key] = value

        if len(self.m) > self.capacity:
            self.m.popitem(last=False)
class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = {}
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self.hmap:
            val = self.hmap[key]
            del self.hmap[key]
            self.hmap[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap.keys():
            del self.hmap[key]
        
        self.hmap[key] = value
        if len(self.hmap) > self.capacity:
            del self.hmap[next(iter(self.hmap.keys()))]

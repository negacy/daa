class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.bucket_array = [None] * capacity
        self.num_of_elements = 0
        self.queue = []
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key > len(self.bucket_array):
            return -1
        if self.bucket_array[key%len(self.bucket_array)] != None:
            self.num_of_elements -=1 
            if self.queue[0] == key: 
                self.queue.append(self.queue.pop(0))
            return self.bucket_array[key%len(self.bucket_array)]
        else:#collision
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.bucket_array[key%len(self.bucket_array)] == None:
            self.bucket_array[key%len(self.bucket_array)] = value
            self.num_of_elements += 1
            self.queue.append(key)
        else:#cache full
            oldest = self.queue.pop(0)
            self.bucket_array[oldest%len(self.bucket_array)] = None
cache = LRU_Cache(5)

cache.set(1, 1);
cache.set(2, 2);
cache.set(3, 3);
cache.set(4, 4);

print(cache.get(1))       # returns 1
print(cache.get(2))       # returns 2
print(cache.get(9))     # returns -1 because 9 is not present in the cache
cache.set(5, 5)
cache.set(6, 6)
print(cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


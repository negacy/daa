import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(self.data)
        self.next = None
        self.prev = None

    def calc_hash(self, hash_str):
        sha = hashlib.sha256()

        hash_str = hash_str.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, timestamp, data):
        if self.head is None:
            self.head = Block(timestamp, data, 0)
            self.tail = self.head
            return

        self.tail.next = Block(timestamp, data, self.tail.hash)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += '|'+cur_head.timestamp + ',' + str(cur_head.data) + ',' +cur_head.hash +',' + str(cur_head.previous_hash) + '|'+  " <- "
            cur_head = cur_head.next
        return out_string
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        
        return size




b1 = DoublyLinkedList() 
b1.append(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()), 'my irst blockchain')
b1.append(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()), 'second blockchain')
b1.append(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()), 'third blockchain')
b1.append(time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()), 'forth blockchain')
print(b1)
print('size: ', b1.size())

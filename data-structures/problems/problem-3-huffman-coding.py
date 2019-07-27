import sys
import operator
from collections import deque

class Node(object):
    
    def __init__(self, freq = None, char = None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def set_value(self, freq, char):
        self.char = char
        self.freq = freq
    
    def get_char(self):
        return self.char

    def get_freq(self):
        return self.freq
         
    def set_left_child(self,left):
        self.left = left
    
    def set_right_child(self, right):
        self.right = right
    
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    

class Stack:
    
    def __init__(self, initial_size = 100):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0
    
    def push(self, data):
        if self.next_index == len(self.arr):
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()
        
        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1
    def top(self):
        return self.arr[self.num_elements-1] 
    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
    
    def _handle_stack_capacity_full(self):
        old_arr = self.arr
        
        self.arr = [0 for _ in range( 2* len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element
    def __repr__(self):
        if not self.is_empty():
            s = "<bottom here>\n_________________\n"
            for item in self.arr:
                if type(item).__name__ == 'Tree':
                    s += "\n_________________\n" + 'root: ' + str(item.get_root().get_freq()) + "\n"
                else:
                    s += "\n_________________\n" + item.get_char() + str(item.get_freq()) + "\n"
                s += "\n_________________\n<top here>"
                return s
        else:
            return "<queue is empty>"


class Queue():
    def __init__(self):
        self.q = deque()
    
    def enq(self,value):
        self.q.appendleft(value)
    
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n"
            for item in self.q:
                if type(item).__name__ == 'Tree':
                    s += "\n_________________\n" + 'root: ' + str(item.get_root().get_freq()) + "\n"
                else:
                    s += "\n_________________\n" + item.get_char() + str(item.get_freq()) + "\n"
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"
def _node_specific_has_left_child(node):
    if type(node).__name__ == 'Node':
        return node.has_left_child()
    elif type(node).__name__ == 'Tree':
        return node.get_root().has_left_child()
        
def _node_specific_has_right_child(node):
    if type(node).__name__ == 'Node':
        return node.has_right_child()
    elif type(node).__name__ == 'Tree':
        return node.get_root().has_right_child()
def _node_specific_get_left_child(node):
    if type(node).__name__ == 'Node':
        return node.get_left_child()
    elif type(node).__name__ == 'Tree':
        return node.get_root().get_left_child()

def _node_specific_get_right_child(node):
    if type(node).__name__ == 'Node':
        return node.get_right_child()
    elif type(node).__name__ == 'Tree':
        return node.get_root().get_right_child()
class Tree():
    def __init__(self):
        self.root = None
    
    def set_root(self,freq, char=None):
        self.root = Node(freq, char=None)
    
    def get_root(self):
        return self.root
    
    def compare(self,node, new_node):
        """
            0 means new_node equals node
            -1 means new node less than existing node
            1 means new node greater than existing node
            """
        if _node_specific_freq(new_node) == None:
            return -1
        if _node_specific_freq(new_node) == _node_specific_freq(node):
            return 0
        elif _node_specific_freq(new_node) < _node_specific_freq(node):
            return -1
        else:
            return 1
    
    def insert(self,new_node):
        #new_node = Node(new_value)
        node = self.get_root()
        if node == None:
            self.root = new_node
            return
        
        while(True):
            comparison = self.compare(node, new_node)
            if comparison == 0:
                # override with new node
                node = new_node
                break # override node, and stop looping
            elif comparison == -1:
                # go left
                if node.has_left_child():
                    node = node.get_left_child()
                else:
                    node.set_left_child(new_node)
                    break #inserted node, so stop looping
            else: #comparison == 1
                # go right
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    node.set_right_child(new_node)
                    break # inserted node, so stop looping
    
    
    def search(self,value):
        node = self.get_root()
        s_node = Node(freq=None, char=value)
        while(True):
            comparison = self.compare(node,s_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if _node_specific_has_left_child(node): 
                    node = _node_specific_get_left_child(node)
                else:
                    return False
            else:
                if node.has_right_child():
                    node = node.get_right_child()
                else:
                    return False
    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.get_root()
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
            
            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )
    
        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                s += "\n" + str(node)
                previous_level = level


        return s
def pre_order(tree):
    
    visit_order = list()
    
    def traverse(node):
        if node:
            # visit the node
            if _node_specific_char(node) == None:
                visit_order.append('None' + ':' + str(_node_specific_freq(node)))
            else:
                visit_order.append(_node_specific_char(node) + ':' + str(_node_specific_freq(node)))
            
            # traverse left subtree
            if type(node).__name__ == 'Node':
                traverse(node.get_left_child())
            else:
                traverse(node.get_root().get_left_child())
            
            # traverse right subtree
            if type(node).__name__ == 'Node':
                traverse(node.get_right_child())
            else:
                traverse(node.get_root().get_right_child())
    
    traverse(tree.get_root())
    
    return visit_order

def _node_specific_freq(node):
    if type(node).__name__ == 'Tree':
        return node.get_root().get_freq()
    elif type(node).__name__ == 'Node':
        return node.get_freq()
def _node_specific_char(node):
    if type(node).__name__ == 'Tree':
        return node.get_root().get_char()
    elif type(node).__name__ == 'Node':
        return node.get_char()
def encode_data(string, tree):
    '''
    tree: str to encode, uffman built tree
    return: encoded data, and tree
    '''
    for char in list(string):
        print(char, tree.search(char))
    root = tree.get_root()

def huffman_encoding(data):
    #replace white space by `|` separator
    data = data.replace(' ', '|')
    print(data)
    #frequency of characters
    freq = {}
    for char in list(data):
        if char in freq.keys():
            freq[char] += 1
        else:
            freq[char] = 1 
    #sort in descending order
    sorted_freq = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
    cnt = 0
    #build a tree
    s = Stack()
    for tpl in sorted_freq:
        node = Node(tpl[-1], tpl[0])
        s.push(node)
    for item in s.arr:
        if type(item).__name__ == 'Node':
            print(item.get_char(), item.get_freq())
    while s.num_elements > 1:
        print('TOP: ', _node_specific_char(s.top()))
        a = s.pop() 
        b = s.pop()
        #create a tree
        t = Tree()
        t.set_root(_node_specific_freq(a) + _node_specific_freq(b)) 
        #print('root: ', a.get_freq() + b.get_freq(), t.get_root().get_freq())
        if _node_specific_freq(a) < t.get_root().get_freq():
            t.get_root().set_left_child(a)
            t.get_root().set_right_child(b)
        else:
            t.get_root().set_left_child(a)
            t.get_root().set_right_child(b)
        #add to stack
        top = s.top()
        #node
        #if type(top).__name__ == 'Node':
        if _node_specific_freq(top) != None and _node_specific_freq(top) >= t.get_root().get_freq():
            s.push(t)
            print('pushing on top')
        else:#pop lighter nodes
            tmp_stack = []
            while _node_specific_freq(top) != None and  _node_specific_freq(top) < t.get_root().get_freq():
                tmp_stack.append(s.pop())
                top = s.top()
                #print('val: ', _node_specific_freq(top), t.get_root().get_freq())
                if _node_specific_freq(top) == None:
                    break
            s.push(t)
            print('size of lighter nodes: ', len(tmp_stack))
            for tt in list(reversed(tmp_stack)): 
                s.push(tt)
        ######################print
        print('-'*50)
        print('TOP: ', _node_specific_char(s.top()), _node_specific_freq(s.top()) )
        num = 0
        for item in s.arr:
            if type(item).__name__ == 'Node':
                print('n: ', item.get_char(), item.get_freq())
            elif type(item).__name__ == 'Tree':
                print('tree: ', pre_order(item))
                #print(item.get_root().get_char(), item.get_root().get_freq(), item.get_root().get_left_child().get_char(), item.get_root().get_right_child().get_char()) 
            num += 1
            if num == s.num_elements:
                break
        cnt += 1
        print('size of stack: ', s.num_elements)
    encode_data(data, s.top())
def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))
    
    huffman_encoding(a_great_sentence)
    '''encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))'''

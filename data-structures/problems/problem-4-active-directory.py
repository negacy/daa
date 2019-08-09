class Node(object):
    
    def __init__(self,value = None):
        self.value = value
        self.left = None
        self.right = None
    
    def set_value(self,value):
        self.value = value
    
    def get_value(self):
        return self.value
    
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
    

class Tree():
    def __init__(self):
        self.root = None
    
    def set_root(self,value):
        self.root = Node(value)
    
    def get_root(self):
        return self.root
    
    def compare(self,node, new_node):
        """
            0 means new_node equals node
            -1 means new node less than existing node
            1 means new node greater than existing node
            """
        if new_node.get_value() == node.get_value():
            return 0
        elif new_node.get_value() < node.get_value():
            return -1
        else:
            return 1
    
    def insert(self,new_value):
        new_node = Node(new_value)
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
        s_node = Node(value)
        while(True):
            comparison = self.compare(node,s_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.has_left_child():
                    node = node.get_left_child()
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

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)
        
    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
sub_child.add_user('Noah')
sub_child.add_user('Savanna')

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
    user(str): user name/id
    group(class:Group): group to check user membership against
    """
    users = group.get_users()

#build bst
    bstree = Tree()
    for i in group.get_users():
        bstree.insert(i) 
    return bstree.search(user)
if __name__ == '__main__':
    print(is_user_in_group("Noah", sub_child))
    print(is_user_in_group("Savanna", sub_child))
    print(is_user_in_group("Negacy", sub_child))

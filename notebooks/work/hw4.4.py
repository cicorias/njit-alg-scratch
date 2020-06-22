import random
import heapq

random.seed(42)

class Node:
    def __init__(self, key):
        self.key = key
        self.lchild = None
        self.rchild = None

inbound_list = [6, 7, 12, 10, 15, 17]

heapq.heapify(inbound_list)
# Now we have a min Heap --- 
print(inbound_list)


def insert_node(r, node):
    if r is None:
        r = node
    else:
        if r.key > node.key:
            if r.rchild is None:
                r.rchild = node
            else:
                insert_node(r.rchild, node)
        else:
            if r.lchild is None:
                r.lchild = node
            else:
                insert_node(r.lchild, node)


#         6
#        /  \
#       7    12
#      /  \   /
#    10  15  17
#  [6, 7, 12, 10, 15, 17

def insert(node, key):
    if node is None:
        node = Node(key)
    else:
        if key >= node.key:
            node.lchild = insert(node.lchild, key)
        else:
            node.rchild = insert(node.rchild, key)

    return node


#root = Node(heapq.heappop(inbound_list))

root = None  # insert(None, inbound_list[0])
for i in inbound_list:
    root = insert(root, i)


print('done..')


def print_nodes(n):
    print('Node: {}  lchild: {}   rchild: {}'.format(n.key, 
                            n.lchild.key if n.lchild is not None else '-',
                            n.rchild.key if n.rchild is not None else '-'))
    if n.lchild is not None:
        print_nodes(n.lchild)
    if n.rchild is not None:
        print_nodes(n.rchild)



print_nodes(root)












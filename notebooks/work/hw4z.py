class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# Function to insert nodes in level order

def print_nodes(n):
    print('Node: {}  lchild: {}   rchild: {}'.format(n.data, 
                            n.left.data if n.left is not None else '-',
                            n.right.data if n.right is not None else '-'))
    if n.left is not None:
        print_nodes(n.left)
    if n.left is not None:
        print_nodes(n.right)

def insertLevelOrder(arr, root, i, n):

    # Base case for recursion
    if i < n:
        temp = newNode(arr[i])
        root = temp

        # insert left child
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n)

        # insert right child
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root

# Function to print tree nodes in
# InOrder fashion


def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


# Driver Code
if __name__ == '__main__':
    arr = [6, 7, 12, 10, 15, 17] # [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    inOrder(root)
    #print_nodes(root)


#         6
#        /  \
#       7    12
#      /  \   /
#    10  15  17
#  [6, 7, 12, 10, 15, 17

# https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/
# https://www.geeksforgeeks.org/construct-a-binary-in-level-order-using-recursion/?ref=rp






class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.val = data

def inOrder(root):
    if root:
        inOrder(root.right)
        print(root.val)
        inOrder(root.left)

def preOrder(root):
    if root:
        print(root.val)
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data)


def BFS(root):
    h = height(root)
    print(h)
    for i in range(1, h+1):
        printLevel(root, i)


def printLevel(root, level):
    if root is None:
        return
    if level == 1:
        print("root data " ,root.val)
    elif level > 1:
        printLevel(root.left, level-1)
        printLevel(root.right, level-1)


def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if(lheight > rheight):
            return lheight+1
        else:
            return  rheight+1


def BFS_Queue(root):
    if root is None:
        return False
    queue = []
    queue.append(root)
    while(len(queue) >0):
        print(queue[0].val)
        node = queue.pop(0)

        if(node.left is not None):
            queue.append(node.left)
        if(node.right is not None):
            queue.append(node.right)

node = Node(5)
node.left = Node(10)
node.right = Node(15)
node.left.left = Node(20)
node.left.right = Node(30)
print(node.left.val)


inOrder(node)
BFS(node)

print("BFS using Queue")
BFS_Queue(node)

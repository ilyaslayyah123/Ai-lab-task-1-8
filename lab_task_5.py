#Task 1 
class Node:
    def __init__(self,value):
        self.value=value
        self.neighbor=[]
    def add_neighbor(self,neighbor):
        self.neighbor.append(neighbor)
def dfs_stack(start_node):
    visited=set()
    stack=[start_node]
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current.value)
            visited.add(current)
            for neighbor in current.neighbor:
                if neighbor not in visited:
                    stack.append(neighbor)
nodea=Node('a')
nodeb=Node('b')
nodec=Node('c')
noded=Node('d')

nodea.add_neighbor(nodeb)
nodea.add_neighbor(nodec)
nodeb.add_neighbor(noded)
nodec.add_neighbor(noded)

dfs_stack(nodea)

################################################33
#Task 2
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value,end=" ")
        inorder(node.right)
        
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.value,end=" ")

def preorder(node):
    if node is not None:
        print(node.value,end=" ")
        preorder(node.left)
        preorder(node.right)

class treenode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

root=treenode(1)
root.left=treenode(2)
root.right=treenode(3)
root.left.left=treenode(4)
root.left.right=treenode(5)

print("inorder traversal")
inorder(root)
print()
print("postorder traversal")
postorder(root)
print()
print("preorder traversal")
preorder(root)


class Node():
    def __init__(self,data,name=None) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.name = self.data if name is None else name

class Binarytree():
    def __init__(self,root=None,**kwargs):
        self.start = Node("start")
        self.end = Node("end")
        self.root = root if root is not None else self.start



    def height(self,node=None):

        if node is None:
            return 0
        else:
            l_height = self.height(node.left)
            r_height = self.height(node.right)
            if l_height>r_height:
                return l_height+1
            else:
                return r_height+1

    def add_node(self,node):

        return True

    def printLevelOrder(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while q:
            # nodeCount (queue size) indicates number
            # of nodes at current level.
            count = len(q)
            # Dequeue all nodes of current level and
            # Enqueue all nodes of next level
            while count > 0:
                temp = q.pop(0)
                print(temp.data, end=' ')
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                count -= 1
            print(' ')

    def printall(self,root):
        if root is None:
            return None
        if root is not None:
            print(root.data)
            self.printall(root.left)
            self.printall(root.right)





root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
print(Binarytree(root=root).printLevelOrder(root))
print(Binarytree(root=root).printall(root))


def test(*args,**kwargs):
    print("test")
    return "tested"
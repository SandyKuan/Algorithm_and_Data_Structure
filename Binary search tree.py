class Node(object):
    """docstring for Node"""
    def __init__(self, data):
        self.data = data
        self.rightchild = None
        self.leftchild = None

class BinarySearchTree(object):
    """docstring for BinarySearchTree"""
    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)

    # time complexity O(logN)
    def insertNode(self, data, node):
        if data < node.data:
            if node.leftchild:
                self.insertNode(data, node.leftchild)
            else:
                node.leftchild = Node(data)
        else:
            if node.rightchild:
                self.insertNode(data, node.rightchild)
            else:
                node.rightchild = Node(data)

    def remove(self,data):
        if self.root:
            self.root = self.removeNode(data, self.root)

    # time complexity O(logN)
    def removeNode(self,data,node):
        if not node:
            return node

        if data < node.data:
            node.leftchild = self.removeNode(data, node.leftchild)
        elif data > node.data:
            node.rightchild = self.removeNode(data, node.rightchild)
        else:
            if not node.leftchild and not node.rightchild:
                print("removing a leaf node...")
                del node
                return None
            if not node.leftchild:
                print("removing a node with single right child...")
                tempNode = node.rightchild
                del node
                return tempNode
            elif not node.rightchild:
                print("removing a node with single left child...")
                tempNode = node.leftchild
                del node
                return tempNode
            print("removing node with two children...")
            tempNode = self.getPredecessor(node.leftchild)
            node.data = tempNode.data
            node.leftchild = self.removeNode(tempNode.data,node.leftchild)
        return node

    def getPredecessor(self,node):
        if node.rightchild:
            return self.getPredecessor(node.rightchild)

    # O(logN)
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):
        if node.leftchild:
            return self.getMin(node.leftchild)
        return node.data

    # time complexity O(logN)
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self,node):
        if node.rightchild:
            return self.getMax(node.rightchild)
        return node.data

    def traverse(self):
        if self.root:
            return self.traveseInOrder(self.root)

    # O(N) 
    def traveseInOrder(self,node):
        if node.leftchild:
            self.traveseInOrder(node.leftchild)
        print(node.data)

        if node.rightchild:
            self.traveseInOrder(node.rightchild)
        # print(node.data)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(6)

print(bst.getMinValue())
print(bst.getMaxValue())

bst.traverse()
bst.remove(5)
                       
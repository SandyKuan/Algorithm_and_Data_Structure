class Node(object):
    """docstring for Node"""
    def __init__(self, data):
        self.data = data
        self.nextNode = None

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    #  time complexity is O(1) since it always inserts the new node in the 'head'
    def insertSatrt(self,data):
        self.size += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def remove(self,data):
        if self.head is None:
            return
        self.size -= 1
        currentNode = self.head
        previousNode = None

        # find the node we want to remove
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode

        # this means currentNode(target) is head, so the previousNode is None, 
        # after we remove the currentNode = target = head, then the head will become the currentNode.next 
        if previousNode is None: 
            self.head = currentNode.nextNode
        # the other case is we move the node in the list, so the previousNode.nextNode will point to currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    def size1(self):
        return self.size

    # we have to iterate the list and find the last node, so the complexity is O(N)
    def insertEnd(self,data):
        self.size += 1
        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode

        actualNode.nextNode = newNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode

linkedList = LinkedList()
linkedList.insertSatrt(12)
linkedList.insertSatrt(122)
linkedList.insertSatrt(133)
linkedList.insertEnd(2)

linkedList.traverseList()
print(linkedList.size1())

linkedList.remove(133)
linkedList.remove(12)
linkedList.remove(122)
linkedList.remove(2)

print(linkedList.size1())



            

          
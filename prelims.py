count = 0;
class Node(object):

    def __init__(self,data):
        self.data = data;
        self.nextNode = None;


class LinkedList(object):

    def __init__(self):
        self.head = None;
        self.size = 0;
        self.lastNode = None;

    def inserData(self, data):
        if self.lastNode is None:
            self.head = Node(data)
            self.lastNode = self.head
        else:
            self.lastNode.nextNode = Node(data)
            self.lastNode = self.lastNode.nextNode

    def displayLinkedList(self):
        current = self.head
        while current is not None:
            print(current.data, end = '')
            current = current.nextNode
    
a_list = LinkedList()
noi = int(input('Enter the number of elements you wish to enter: '))
while count != noi:
    data = int(input('Enter your desired data: '))
    a_list.inserData(data)
    count += 1
print('The items you Entered: ', end = '')
a_list.displayLinkedList()

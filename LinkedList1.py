class Node(object):

    def _init_(self,data):
        self.data = data;
        self.nextNode = None;


class LinkedList(object):

    def _init_(self):
        self.head = None;
        self.size = 0;

    def insertStart(self, data):

        self.size = self.size + 1;
        newNode = Node(data);

        if not self.head:
            self.head = newNode;
        else:
            newNode.nextNode = self.head;
            self.head = newNode;
            
    def size(self):
        return self.size;

    def size2(self):
        actualNode = self.head;
        size = 0;


        while actualNode is not None:
            size +=1 ;
            actualNode = actualNode.nextNode;
        return size;

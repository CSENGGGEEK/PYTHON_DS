class Node:
    def __init__(self,data,link):
        self.data = data
        self.link = link


class Circular_Linked_List:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append_cll(self,data):
        new_node = Node(data,None)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.link = self.head
        else :
            temp = self.head
            while temp.link!=self.head:
                temp = temp.link

            temp.link = new_node
            self.tail = new_node
            new_node.link = self.head  
    
    def addbtw_cll(self,data,loc):
        new_node = Node(data,None)
        temp = self.head
        for i in range(loc):
            if temp.link == self.head:
                print("There are less number of nodes !!")
                return
            temp = temp.link
        new_node.link = temp.link 
        temp.link = new_node

    def addbeg_cll(self,data):
        new_node = Node(data,None)
        self.tail.link = new_node 
        new_node.link = self.head
        self.head = new_node

    def display_cll(self):
        if self.head is None and self.tail is None:
            print("Queue is Empty !!")
        else:
            temp = self.head
            while temp.link!=self.head:
                print(temp.data,end=" ")
                temp = temp.link

            if temp.link == self.head:
                print(temp.data,end="\n")         

cll = Circular_Linked_List()
cll.append_cll(1)
cll.append_cll(2)
cll.addbtw_cll(3,1)
cll.addbtw_cll(4,2)
cll.addbeg_cll(0)
cll.display_cll()
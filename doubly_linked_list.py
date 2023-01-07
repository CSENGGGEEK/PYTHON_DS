# Structure of node of doubly linked list
class Node:
    def __init__(self,data,next,prev):
        self.data = data 
        self.next = next 
        self.prev = prev 

# Structure of a doubly linked list
class Doubly_Linked_List:
    def __init__(self):
        self.head = None
    
    # Adding a new node at the end of linked list 
    def append_dll(self,data):
        temp = self.head
        new_node = Node(data,None,None)
        if self.head == None:
            self.head = new_node
            new_node.prev = None
        else:
            while temp.next!= None:
                temp = temp.next            
            temp.next = new_node
            new_node.prev = temp
    
    # Adding a node an a specified location 
    def addaft_dll(self,data,loc):
        temp = self.head
        for i in range(loc):
            if temp.next == None:
                print("There are less than {} nodes !!".format(loc))
            temp = temp.next
        new_node = Node(data,None,None)
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp

    # Addition of new node at the beginning of linked list 
    def addbeg_dll(self,data):
        new_node = Node(data,None,None)
        new_node.next = self.head 
        self.head = new_node
        new_node.prev = self.head

    # Deleting the data from  the linked list 
    def deleteelm_dll(self,data):
        temp = self.head
        old = self.head 
        while temp.next != None:
            if temp.data == data:
                if old == self.head:
                    self.head = temp.next
                    temp.next.prev = self.head
                    return
                else:
                    old.next = temp.next
                    temp.prev = old            
            old = temp
            temp = temp.next
        if temp.link == None:
            old.next = temp.next

    # Printing the linked list
    def display_dll(self):
        temp = self.head
        if self.head == None:
            print("There is noting to display here !!")
        else :
            while temp.next != None:
                print(temp.data,end=" ")
                temp = temp.next
            if temp.next == None:
                print(temp.data,end="\n")

dll = Doubly_Linked_List()
dll.addbeg_dll(1)
dll.append_dll(10)
dll.append_dll(20)
dll.addaft_dll(20,1)
dll.addaft_dll(30,0)
dll.deleteelm_dll(1)
dll.display_dll()
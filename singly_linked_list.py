import sys 
# Creating the structure of single node
class Node:
    # This will initialize an object (Node) with parrameters as data and link
    def __init__(self,data,link):
        self.data = data  # Data 
        self.link = link # Link to next node
        
# Creating linked list Structure 
class Singly_Linked_List:
    # This will initialize an empty object (Singly Linked List) 
    def __init__(self):
        self.head = None # Head of linked list 

    # Adding a node at beginning of linked list 
    def addbeg_sll(self,data):
        new_node = Node(data,None) 
        new_node.link = self.head
        self.head = new_node

    # Inserting a node after a specifieid location 
    def addaft_sll(self,data,loc):
        new_node = Node(data,None)
        temp = self.head
        for i in range(loc): 
            if temp.link == None:
                print("There are less than {} node !!".format(loc))
                return
            temp = temp.link
        new_node.link = temp.link
        temp.link = new_node

    # Appending a linked list at the end
    def append_sll(self,data):
        new_node = Node(data,None)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.link!=None:
                temp = temp.link
            temp.link = new_node

    # Deleting the data from  the linked list 
    def deleteelm_sll(self,data):
        temp = self.head
        old = self.head 
        while temp.link != None:
            if temp.data == data:
                if old == self.head:
                    self.head = temp.link
                    return
                else:
                    old.link = temp.link            
            old = temp
            temp = temp.link
        if temp.link == None:
            old.link = temp.link
        
    # Printing the linked list 
    def display_sll(self):
        temp = self.head
        while temp.link != None:
            print(temp.data,end=" ")
            temp = temp.link

        if temp.link == None :
            print(temp.data,end="\n")


# Driver Code 
counter = 0
sll = None
msg = '''
    1. Create a new linked list 
    2. Append (Add a new node at the end of the linked list)
    3. Insert (Add a new node at a specific index in the linked list)
    4. Add at beginning (Add a new node at the beginning of linked list)
    5. Delete (A specified node will be deleted from the linked list)
    6. Display (Print the singly linked list)
    0. Exit the program 
    9. Show this message again
    '''
print(msg)

while True:
    choice = int(input("Enter your choice : "))
    if choice == 1:
        if counter == 0:
            sll = Singly_Linked_List()
            counter+=1
        else:
            print("There is already a linked list !!")
    elif choice == 2:
        data = int(input("Enter the data : "))
        sll.append_sll(data)
    elif choice == 3:
        data = int(input("Enter the data : "))
        loc = int(input("Enter the location : "))
        sll.addaft_sll(data,loc)
    elif choice == 4:
        data = int(input("Enter the data : "))
        sll.addbeg_sll(data)
    elif choice == 5:
        data = int(input("Enter the data you want to delete : "))
        sll.deleteelm_sll(data)
    elif choice == 6:
        sll.display_sll()
    elif choice == 9:
        print(msg)
    else:
        sys.exit()
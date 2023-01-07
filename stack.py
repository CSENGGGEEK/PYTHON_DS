# Node of a stack
class Node:
    def __init__(self,data,link) -> None:
        self.data = data
        self.link = link 

# Stack and Stack operations
class Stack:
    def __init__(self) -> None:
        self.top = None

    def push_stack(self,data):
        new_node = Node(data,None)
        if self.top == None:
            self.top = new_node
        else :
            new_node.link  = self.top
            self.top = new_node
    
    def pop_stack(self):
        if self.top == None:
            print("There is no element to delete !!")
        else:
            print(self.top.data)
            self.top = self.top.link

    def peep_stack(self):
        print(self.top.data)

    def isEmpty(self):
        if self.top == None:
            print('Stack is Empty')
        else:
            print('Stack is not empty')

    def display_stack(self):
        if self.top == None:
            print("There is nothing to print ")
        else :
            temp = self.top 
            while temp.link != None:
                print(temp.data,end=" ")
                temp = temp.link 
            
            if temp.link == None:
                print(temp.data,end="\n")

stack = Stack()
stack.push_stack(1)
stack.push_stack(2)
stack.push_stack(3)
stack.push_stack(4)
stack.push_stack(5)
stack.push_stack(6)
stack.push_stack(7)
stack.push_stack(8)
stack.display_stack()
stack.pop_stack()
stack.isEmpty()
stack.display_stack()
            
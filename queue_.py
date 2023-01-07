class Node:
    def __init__(self,data,link):
        self.data = data
        self.link = link

class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def push_queue(self,data):
        new_node = Node(data,None) 
        if self.front is None and self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            new_node.link =  self.rear
            self.rear = new_node
    
    def pop_queue(self):
        if self.front is None and self.rear is None:
            print("Queue is empty !!")
        else:
            old = self.rear
            temp = self.rear
            while temp.link!=None:
                old = temp
                temp = temp.link
            print(temp.data)
            old.link = temp.link 
            self.front = old
        
    def isEmpty(self):
        if self.front is None and self.rear is None:
            print("Yes")
        else:
            print("No!!")

    def display_queue(self):
        temp = self.rear 
        if self.front is None and self.rear is None:
            print("The queue is empty !!")
        else:
            while temp.link!=None:
                print(temp.data,end=" ")
                temp = temp.link

            if temp.link == None:
                print(temp.data,end="\n")
q = Queue()
q.push_queue(1)
q.push_queue(2)
q.push_queue(3)
q.pop_queue()
q.pop_queue()
q.pop_queue()
q.display_queue()
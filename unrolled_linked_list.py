class Block:
    def __init__(self) -> None:
        self.node_count = 0
        self.head = None
        self.tail = None
        self.next_block = None

class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.link = None

class Unrolled_Linked_List:
    def __init__(self) -> None:
        self.max_count = 10
        self.block_count = 0
        self.head_block = None

    def append(self,data):
        if self.head_block == None:
            new_block  = Block()
            self.head_block = new_block
            new_block.link = None
            new_node = Node(data)
            new_block.tail = new_node
            new_block.head = new_node
            new_node.data = data
            new_node.link = new_node
            new_block.node_count+=1
            self.block_count+=1
        else:
            block_temp = self.head_block

            while block_temp.next_block!=None:
                block_temp = block_temp.next_block 
                if block_temp.next_block == None:
                    break

            if block_temp.node_count == self.max_count:
                new_block = Block() # Creating a new block 
                block_temp.next_block = new_block
                new_node = Node(data)
                new_block.head = new_node
                new_node.link = new_node
                new_block.tail = new_node
                new_block.node_count = 1
                self.block_count+=1
            else:
                new_node = Node(data)
                new_node.link = block_temp.head
                block_temp.tail.link = new_node
                block_temp.tail = new_node
                block_temp.node_count+=1

    def display(self):
        block_temp = self.head_block
        for i in range(self.block_count):
            temp = block_temp.head
            for j in range(block_temp.node_count):
                print(temp.data,end=" ")
                temp = temp.link 
            block_temp = block_temp.next_block

ull = Unrolled_Linked_List()
ull.append(1)
ull.append(2)
ull.append(3)
ull.append(4)
ull.append(5)
ull.append(6)
ull.append(7)
ull.append(8)
ull.append(9)
ull.append(10)
ull.append(11)
ull.display()

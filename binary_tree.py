class Node:
    def __init__(self,data,leftchild,rightchild):
        self.data = data
        self.leftchild = leftchild
        self.rightchild = rightchild

class Binary_Tree:
    def __init__(self):
        self.rootnode = None

    def node_creator(self):
        data = int(input("Enter the data : "))
        left = int(input("Left Child : "))
        right = int(input("Right Child : "))
        return Node(data,left,right)

    def tree_creation(self):
        if self.rootnode == None:
            temp = self.root_node = self.node_creator()
            self.tree_creation()
        else:
            if self.root_node.leftchild == 1:
                self.root_node.leftchild = self.node_creator()
            else:
                return 
            if self.root_node.rightchild == 1:
                self.root_node.rightchild = self.node_creator()
            else:
                return
            self.tree_creation()
            print("There is already a tree !!")


tree = Binary_Tree()

tree.tree_creation()
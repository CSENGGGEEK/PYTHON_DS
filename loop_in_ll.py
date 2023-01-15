def detect_loop(self):
    visited_nodes = {
        # data : true | false
    }
    temp = self.head
    while temp.link != None:
        if visited_nodes[hash(temp.data)] == True:
             return 1
        else:
            visited_nodes[hash(temp.data)] = True

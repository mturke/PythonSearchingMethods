class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


class BinaryTreeStringList:
    def __init__(self):
        self.root = None

    def get(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self.adding(val, self.root)

    def adding(self, val, node):
        if(val < node.value):
            if(node.left != None):
                self.adding(val, node.left)
            else:
                node.left = Node(val)
        else:
            if(node.right != None):
                self.adding(val, node.right)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self.finding(val, self.root)
        else:
            return False

    def finding(self, val, node):
        if node is None:
            return False
        if(val == node.value):
            return True
        elif(val < node.value and node.left):
            return self.finding(val, node.left)
        elif(val > node.value and node.right):
            return self.finding(val, node.right)  



class Node:
    def __init__(self, value):
        self.r = None
        self.l = None
        self.v = value

class Tree:
    def __init__(self):
        self.root = None

    def GetRoot(self):
        return self.root

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(value, self.root)

    def _add(self, value, node):
        if (value < node.v):
            if node.l is None:
                node.l = Node(value)
            else:
                self._add(value, node.l)
        if (value > node.v):
            if node.r is None:
                node.r = Node(value)
            else:
                self._add(value, node.r)

    def find(self, value):
        if self.root is None:
            return None
        else:
            self._find(value, self.root)

    def _find(self, value, node):
        if (value == node.v):
            return node
        elif (value < node.v and node.l != None):
            self._find(value, node.l)
        elif (value > node.v and node.r != None):
            self._find(value, node.r)
class Node(object):
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.next = None

    def GetKey(self):
        return self.key

    def SetKey(self, value):
        self.key = value

    def GetData(self):
        return self.data

    def SetData(self, value):
        self.data = value

    def GetNext(self):
        return self.next

    def SetNext(self, value):
        self.next = value

class LinkedList(object):
    def __init__(self):
        self.head = None

    def Insert(self, key, data):
        newNode = Node(key, data)
        newNode.SetNext(self.head)
        self.head = newNode

    def Size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.GetNext()
        return count

    def Search(self, key):
        current = self.head
        found = False
        while not found and current:
            if current.GetKey() == key:
                found = True
            else:
                current = current.GetNext()
        if current == None:
           return "Not in list"
        else:
            return current.GetData()

    def Delete(self, key):
        current = self.head
        previous = None
        found = False
        while not found and current:
            if current.GetKey() == key:
                previous.SetNext(current.GetNext())
                found = True
            else:
                previous = current
                current = current.GetNext()



x = LinkedList()
x.Insert("flerp", "derp")
x.Insert("fizz", "buzz")
x.Insert("one", "two")
print(x.Size())
print(x.Search("fizz"))
x.Delete("fizz")
print(x.Size())
print(x.Search("fizz"))
print(x.Search("one"))
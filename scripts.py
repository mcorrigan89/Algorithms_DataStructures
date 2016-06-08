from Sort import QuickSort, SimpleSort
from TreeList import LinkedList

list = [6,4,3,4,5,7,8,7,6,4,54,6,3,26,357,64,35,13,346,647,467,23,134,24,64,57,546,36,23,235,36,5868,9]

print(QuickSort.Sort(list))
print(SimpleSort.Sort(list))

x = LinkedList.LinkedList()
x.Insert("flerp", "derp")
x.Insert("fizz", "buzz")
x.Insert("one", "two")
print(x.Size())
print(x.Search("fizz"))
x.Delete("fizz")
print(x.Size())
print(x.Search("fizz"))
print(x.Search("one"))
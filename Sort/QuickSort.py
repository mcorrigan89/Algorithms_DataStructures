def QuickSort(array):
    less = []
    equal = []
    greater =[]

    if (len(array) > 1):
        pivot = array[0]
        for i in array:
            if i < pivot:
                less.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                greater.append(i)
        return QuickSort(less) + equal + QuickSort(greater)
    else:
        return array



list = [6,7,8,75,52,4,2,3,4,5,7,4622,235,254,235,235235,674,5678,5785678,563,254,235,254,56,6,89,67,6,345,3354,546,567]

print(QuickSort(list))
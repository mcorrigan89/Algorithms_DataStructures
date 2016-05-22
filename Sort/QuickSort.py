def Sort(array):
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
        return Sort(less) + equal + Sort(greater)
    else:
        return array

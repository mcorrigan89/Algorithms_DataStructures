def Search(array, value):
    found = False
    while not found:
        index = len(array) / 2
        if value < array[int(index)]:
            return Search(array[:int(index)], value)
        elif value > array[int(index)]:
            return Search(array[int(index - 1):], value)
        else:
            return int(index)




list = [1,4,6,7,8,9]

print(Search(list, 6))
def Sort(array):
    for i in range(0, len(array)):
        currentValue = array[i]
        currentIndex = i
        while currentIndex>0 and array[currentIndex-1] > currentValue:
            array[currentIndex] = array[currentIndex - 1]
            currentIndex = currentIndex - 1
        array[currentIndex] = currentValue
    return array

def quicksort (array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)


def partition (array, low, high):
    pivot = high # Use last element as pivot
    pivot_position = low; # Track index of pivot

    for i in range(low, high):
        # If the current element is less than the last element, we swap it with the element at pivot_position and increment pivot_position
        if array[i] < array[pivot]:
            array[i], array[pivot_position] = array[pivot_position], array[i] # Swap
            pivot_position += 1 # Increment the firstHighIndex

    array[pivot], array[pivot_position] = array[pivot_position], array[pivot] # Swap the pivot from the end into the right position
    return pivot_position


testArray = [2,5,6,7,9,3,10,1,8,4]

quicksort(testArray, 0, 9)
print(testArray)
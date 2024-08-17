def partition (array, low, high):
    pivot = high; # Use last element as pivot value
    pivot_position = low; # Track index of pivot

    # print("Pivot number: ", array[pivot])
    for i in range(low, high):

        # print("Index: ", i, ", Value: ", array[i])

        # If the current element is less than the pivot, we swap it with the element at pivot_position and increment pivot_position
        if array[i] < array[pivot]:
            # print("Swap!")
            array[i], array[pivot_position] = array[pivot_position], array[i] # Swap
            pivot_position += 1 # Increment the firstHighIndex

        # print(array)
        # print(pivot_position)
        # print()

    # print("Swapping pivot to correct position")
    array[pivot], array[pivot_position] = array[pivot_position], array[pivot]
    return pivot_position

def quicksort (array, low, high):

    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)

testArray = [9,4,1,3,5,8,6,2,7]
quicksort(testArray, 0, 8)

print(testArray)
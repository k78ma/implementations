def mergesort(array, low, high):
    if low < high:
        middle = (low + high) // 2
        mergesort(array, low, middle)
        mergesort(array, middle + 1, high)
        merge(array, low, middle, high)

def merge(array, low, middle, high):

    # Create temporary arrays to hold the two subarrays
    left_subarray = array[low:middle + 1]
    right_subarray = array[middle + 1:high + 1]

    # Initial indexes for the subarrays and the main array
    left_idx = 0  # Initial index for left subarray
    right_idx = 0  # Initial index for right subarray
    merged_idx = low  # Initial index for merged array

    # Merge the temporary arrays back into the original array
    while left_idx < len(left_subarray) and right_idx < len(right_subarray):
        if left_subarray[left_idx] <= right_subarray[right_idx]:
            array[merged_idx] = left_subarray[left_idx]
            left_idx += 1
        else:
            array[merged_idx] = right_subarray[right_idx]
            right_idx += 1
        merged_idx += 1

    # Copy any remaining elements of left_subarray, if any
    while left_idx < len(left_subarray):
        array[merged_idx] = left_subarray[left_idx]
        left_idx += 1
        merged_idx += 1

    # Copy any remaining elements of right_subarray, if any
    while right_idx < len(right_subarray):
        array[merged_idx] = right_subarray[right_idx]
        right_idx += 1
        merged_idx += 1

testArray = [2,5,6,7,9,3,10,1,8,4]

mergesort(testArray, 0, 9)
print(testArray)
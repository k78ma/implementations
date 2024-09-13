def largest_subrange(array, left, right):
    """
    Given an array, return the index pair (i, j) that maximizes 
    the sum of elements from index i to index j, along with the maximum sum.
    """
    # Base case: Only one element
    if left == right:
        return array[left], left, right
    else:
        mid = (left + right) // 2

        # Find maximum subarray sum in left half
        left_max_sum, left_start, left_end = largest_subrange(array, left, mid)

        # Find maximum subarray sum in right half
        right_max_sum, right_start, right_end = largest_subrange(array, mid + 1, right)

        # Find maximum subarray sum crossing the midpoint
        cross_max_sum, cross_start, cross_end = max_crossing_subarray(array, left, mid, right)

        # Return the maximum of the three
        return max(
            (left_max_sum, left_start, left_end),
            (right_max_sum, right_start, right_end),
            (cross_max_sum, cross_start, cross_end),
            key=lambda x: x[0]
        )

def max_crossing_subarray(array, left, mid, right):
    """
    Finds the maximum subarray sum that crosses the midpoint.
    """
    # Find max subarray sum starting from mid and moving left
    left_sum = float('-inf')
    sum = 0
    max_left = mid
    for i in range(mid, left - 1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    # Find max subarray sum starting from mid+1 and moving right
    right_sum = float('-inf')
    sum = 0
    max_right = mid + 1
    for i in range(mid + 1, right + 1):
        sum += array[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    # Combine the two
    return left_sum + right_sum, max_left, max_right

# Test array
testArray = [-17, 5, 3, -10, 6, 1, 4, -3, 8, 1, -13, 4]

# Find the largest subrange
max_sum, start_index, end_index = largest_subrange(testArray, 0, len(testArray) - 1)

print(f"Maximum sum: {max_sum}, Start index: {start_index}, End index: {end_index}")
print(f"Subarray with maximum sum: {testArray[start_index:end_index+1]}")

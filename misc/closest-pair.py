def closestPair(array, left, right):
    # Base case: If the array has only one element, return infinity (no valid pair)
    if left >= right:
        return float('inf')

    # Base case: If there are only two elements, return their difference
    if right - left == 1:
        return abs(array[right] - array[left])

    # Find the middle index
    mid = (left + right) // 2

    # Recursively find the minimum difference in the left and right halves
    left_min = closestPair(array, left, mid)
    right_min = closestPair(array, mid + 1, right)

    # Check the difference between the middle pair
    cross_min = abs(array[mid + 1] - array[mid])

    # Return the smallest of the three minimums
    return min(left_min, right_min, cross_min)


# Test array
testArray = [-17, 5, 3, -10, 6, 1, 4, -3, 8, 1, -13, 4]

# Find the closest pair (minimum difference between any two adjacent elements)
result = closestPair(testArray, 0, len(testArray) - 1)

print(f"The smallest difference between any two adjacent elements is: {result}")

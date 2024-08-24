def binary_search_1(array, target):
	
	low, high = 0, len(array) - 1
	
	while low <= high:
		
		m = low + ((high-low) // 2) # Prevent overflow
		
		if array[m] > target:
			high = m - 1
		elif array[m] < target:
			low = m + 1
		elif array[m] == target:
			return m
			
	return -1

def binary_search_2(array, target, low, high):
	
    if low > high:
        return -1
	
    m = low + ((high-low) // 2)
	
    if array[m] == target:
        return m
    elif array[m] > target:
        return(binary_search_2(array, target, low, m - 1))
    elif array[m] < target:
        return(binary_search_2(array, target, m+1, high))

# Test code for binary search functions

# Test array (must be sorted for binary search)
test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Test cases
test_cases = [
    (1, 0),    # Existing element at the beginning
    (19, 9),   # Existing element at the end
    (11, 5),   # Existing element in the middle
    (4, -1),   # Non-existing element
    (0, -1),   # Non-existing element smaller than all
    (20, -1)   # Non-existing element larger than all
]

print("Testing binary_search_1:")
for target, expected in test_cases:
    result = binary_search_1(test_array, target)
    print(f"Target: {target}, Expected: {expected}, Result: {result}")
    assert result == expected, f"Test failed for target {target}"

print("\nTesting binary_search_2:")
for target, expected in test_cases:
    result = binary_search_2(test_array, target, 0, len(test_array) - 1)
    print(f"Target: {target}, Expected: {expected}, Result: {result}")
    assert result == expected, f"Test failed for target {target}"

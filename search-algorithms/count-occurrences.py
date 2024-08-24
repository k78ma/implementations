def count_occurrences(array, target):
    array = sorted(array)
    low_boundary = boundary_search_low(array, target)
    high_boundary = boundary_search_high(array, target)
    
    if low_boundary == -1:  # Target not found
        return 0
    
    occurrences = high_boundary - low_boundary + 1
    return occurrences

def boundary_search_high(array, target):

    low, high = 0, len(array) - 1
    boundary = -1

    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] == target:
            boundary = mid
            low = mid + 1
    return boundary

def boundary_search_low(array, target):

    low, high = 0, len(array) - 1
    boundary = -1

    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        elif array[mid] == target:
            boundary = mid
            high = mid - 1
    return boundary


test_array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Test cases
test_cases = [
    (1, 1),    # Element appears once
    (2, 2),    # Element appears twice
    (3, 3),    # Element appears three times
    (4, 4),    # Element appears four times
    (5, 5),    # Element appears five times
    (6, 0),    # Element does not appear
    (0, 0)     # Element smaller than all in array
]

print("Testing count_occurrences function:")
for target, expected in test_cases:
    result = count_occurrences(test_array, target)
    print(f"Target: {target}, Expected: {expected}, Result: {result}")
    assert result == expected, f"Test failed for target {target}"

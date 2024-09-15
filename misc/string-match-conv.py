# String matching with sliding window dot product or convolution

import numpy as np

# Define the binary strings
S = np.array([1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0])  # Encoded text S
P = np.array([1, 0, 0, 1, 1, 0])                   # Encoded pattern P

# Flip the pattern P so that convolution doesn't flip it implicitly
P_flipped = P[::-1]

# Perform convolution with 'valid' mode to prevent zero-padding
convolution_result = np.convolve(S, P_flipped, mode='valid')

# Sliding dot product function for comparison
def sliding_dot_product(S, P):
    m = len(P)
    n = len(S)
    
    dot_products = []
    # Slide the pattern over the string and calculate the dot product for each window
    for i in range(n - m + 1):
        window = S[i:i + m]  # Select window of size m from S
        dot_product = np.dot(window, P)  # Compute dot product with pattern P
        dot_products.append(dot_product)
    
    return dot_products

# Sliding dot product results
dot_product_result = sliding_dot_product(S, P)

# Display both results
print("Sliding Dot Product Results:", dot_product_result)
print("Convolution (with flipped pattern) Results:", convolution_result)

# Sliding Dot Product Results: [np.int64(3), np.int64(1), np.int64(1), np.int64(2), np.int64(1), np.int64(1), np.int64(3), np.int64(1), np.int64(1), np.int64(2), np.int64(1), np.int64(1), np.int64(3)]
# Convolution (with flipped pattern) Results: [3 1 1 2 1 1 3 1 1 2 1 1 3]
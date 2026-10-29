
# Experiment No. 10
# NumPy Array Operations

import numpy as np

# 1. Create a one-dimensional array from 1 to 10
arr = np.arange(1, 11)
print("Original Array:", arr)

# 2. Perform slicing operations
print("\nFirst five elements:", arr[:5])
print("Elements from index 3 to 7:", arr[3:8])
print("Alternate elements:", arr[::2])
print("Array in reverse order:", arr[::-1])

# 3. Compute statistical measures
print("\nSum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 4. Apply broadcasting

# Add 5 to every element
add_arr = arr + 5
print("\nArray after adding 5:", add_arr)

# Multiply every element by 2
mul_arr = arr * 2
print("Array after multiplying by 2:", mul_arr)

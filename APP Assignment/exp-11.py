
# Experiment No. 11
# Pandas Series Operations

import pandas as pd
import numpy as np

# 1. Generate 10 random numbers
np.random.seed(42)
numbers = np.random.randint(1, 100, 10)

# 2. Create a Pandas Series
s = pd.Series(numbers)

print("Original Series:")
print(s)

# 3. Perform indexing
print("\nElement at index 3:", s[3])

print("First five elements:")
print(s[:5])

# 4. Perform filtering
print("\nNumbers greater than 50:")
print(s[s > 50])

# 5. Perform statistical operations
print("\nMean:", s.mean())
print("Median:", s.median())
print("Minimum:", s.min())
print("Maximum:", s.max())

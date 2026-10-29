
# Experiment 4
# Calculate the nth Fibonacci number efficiently

def fibonacci_iterative(n):

    # Handle the base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Calculate Fibonacci number from 2 to n
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


# Take input from the user
n = int(input("Enter the value of n: "))

# Validate input
if n < 0:
    print("Please enter a non-negative integer.")
else:
    result = fibonacci_iterative(n)
    print("Fibonacci number is:", result)


# Experiment 6
# 0/1 Knapsack Problem using Dynamic Programming

def knapsack(weights, profits, capacity):
    n = len(weights)

    # Create the DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):

            if weights[i - 1] > w:
                # Exclude the item if it is too heavy
                dp[i][w] = dp[i - 1][w]

            else:
                # Choose the option with maximum profit
                dp[i][w] = max(
                    dp[i - 1][w],
                    profits[i - 1]
                    + dp[i - 1][w - weights[i - 1]]
                )

    # Find the selected items using backtracking
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    # Arrange selected indexes in original order
    selected_items.reverse()

    return dp[n][capacity], selected_items


# Main Program
weights = [3, 2, 4, 5, 1]
profits = [50, 40, 70, 80, 10]
capacity = 7

max_profit, items = knapsack(weights, profits, capacity)

print("Maximum Profit:", max_profit)
print("Items in Knapsack:", items)

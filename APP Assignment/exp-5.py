
# Experiment 5
# Longest Common Subsequence (LCS)
# Using Dynamic Programming

def lcs(X, Y):

    # Find the length of both strings
    m = len(X)
    n = len(Y)

    # Create a DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if X[i - 1] == Y[j - 1]:
                # Characters match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # Characters do not match
                dp[i][j] = max(dp[i - 1][j],
                               dp[i][j - 1])

    # Backtracking to find the actual LCS
    i = m
    j = n
    result = []

    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            result.append(X[i - 1])
            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Reverse the result
    result.reverse()

    # Convert list into a string
    lcs_string = ''.join(result)

    return dp[m][n], lcs_string


# Main Program
X = input("Enter first string: ")
Y = input("Enter second string: ")

length, sequence = lcs(X, Y)

print("\nLength of LCS:", length)
print("Longest Common Subsequence:", sequence)

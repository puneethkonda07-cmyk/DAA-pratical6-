
def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices

    # dp[i][j] stores the minimum multiplication cost
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # L is the chain length
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            dp[i][j] = float('inf')

            # Try all possible split points
            for k in range(i, j):
                q = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if q < dp[i][j]:
                    dp[i][j] = q

    return dp[1][n]


# Dimensions of matrices
# A1: 10 x 20, A2: 20 x 30
# A3: 30 x 40, A4: 40 x 30
dimensions = [10, 20, 30, 40, 30]

min_ops = matrix_chain_order(dimensions)

print("Minimum number of multiplications is:", min_ops)

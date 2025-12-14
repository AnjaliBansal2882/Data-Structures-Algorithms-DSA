class GridUniquePathsMemoization:

    def uniquePaths(self, m, n):
        # Initialize dp with -1
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.helper(m, n, 0, 0, dp)

    def helper(self, m, n, row, col, dp):

        # Reached destination
        if row == m - 1 and col == n - 1:
            return 1

        # Out of bounds
        if row >= m or col >= n:
            return 0

        # Memoized result
        if dp[row][col] != -1:
            return dp[row][col]

        # Move Down
        down = self.helper(m, n, row + 1, col, dp)

        # Move Right
        right = self.helper(m, n, row, col + 1, dp)

        dp[row][col] = down + right
        return dp[row][col]


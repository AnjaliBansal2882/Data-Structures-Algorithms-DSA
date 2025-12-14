class UniquePathsWithObstacleMemoization:

    def uniquePathsWithObstacles(self, matrix):
        m, n = len(matrix), len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.helper(matrix, m - 1, n - 1, dp)

    def helper(self, matrix, row, col, dp):

        # Reached first cell
        if row == 0 and col == 0 and matrix[row][col] == 0:
            return 1

        # Invalid index
        if row < 0 or col < 0:
            return 0

        # Blocked cell
        if matrix[row][col] == 1:
            return 0

        # Memoized result
        if dp[row][col] != -1:
            return dp[row][col]

        # Move left and up
        left = self.helper(matrix, row, col - 1, dp)
        up = self.helper(matrix, row - 1, col, dp)

        dp[row][col] = left + up
        return dp[row][col]


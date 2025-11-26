class RatInAMaze:
    def findPath(self, grid):
        n = len(grid) - 1
        ans = []
        curr = []

        if grid[0][0] == 0:
            return ans

        self.helper(grid, 0, 0, n, ans, curr)
        return ans

    def helper(self, grid, i, j, n, ans, curr):
        # Reached destination
        if i == n and j == n:
            ans.append("".join(curr))
            return

        # Out of bounds condition (your Java had i>n && j>n but that's unreachable)
        if i > n or j > n:
            return

        isCurrZero = (grid[i][j] == 0)

        # Mark visited
        grid[i][j] = 0

        # Move Up
        if i > 0 and grid[i - 1][j] != 0:
            curr.append('U')
            self.helper(grid, i - 1, j, n, ans, curr)
            curr.pop()

        # Move Right
        if j < n and grid[i][j + 1] != 0:
            curr.append('R')
            self.helper(grid, i, j + 1, n, ans, curr)
            curr.pop()

        # Move Down
        if i < n and grid[i + 1][j] != 0:
            curr.append('D')
            self.helper(grid, i + 1, j, n, ans, curr)
            curr.pop()

        # Move Left
        if j > 0 and grid[i][j - 1] != 0:
            curr.append('L')
            self.helper(grid, i, j - 1, n, ans, curr)
            curr.pop()

        # Restore original value
        grid[i][j] = 0 if isCurrZero else 1

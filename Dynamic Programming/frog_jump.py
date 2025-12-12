class FrogJumpMemoization:

    def frogJump(self, heights):
        memo = [-1] * len(heights)
        return self.helper(heights, len(heights) - 1, memo)

    def helper(self, heights, index, memo):

        if index <= 0:
            return 0

        if memo[index] != -1:
            return memo[index]

        left = abs(heights[index] - heights[index - 1]) + self.helper(heights, index - 1, memo)
        right = float('inf')

        if index >= 2:
            right = abs(heights[index] - heights[index - 2]) + self.helper(heights, index - 2, memo)

        memo[index] = min(left, right)
        return memo[index]

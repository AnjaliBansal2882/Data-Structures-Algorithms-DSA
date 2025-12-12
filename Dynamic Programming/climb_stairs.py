class ClimbingStairsMemoization:
    def climbStairs(self, n):
        dp = [-1] * (n + 1)
        return self.helper(n, dp)

    def helper(self, n, dp):
        if n == 0:
            return 1

        if n < 0:
            return 0

        # One step
        if dp[n - 1] != -1:
            oneStep = dp[n - 1]
        else:
            oneStep = self.helper(n - 1, dp)

        # Two steps
        if n >= 2:
            if dp[n - 2] != -1:
                twoStep = dp[n - 2]
            else:
                twoStep = self.helper(n - 2, dp)
        else:
            twoStep = 0

        dp[n] = oneStep + twoStep
        return dp[n]

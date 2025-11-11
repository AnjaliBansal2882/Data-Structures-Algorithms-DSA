"""
Time Complexity: O(2^n * k) where n is the number of candidates and k is the average length of each combination
Space Complexity: O(k) for recursive stack space
"""

class CombinationSum:
    def combination_sum(self, candidates, target):
        ans = []
        self._solve(candidates, target, ans, [], 0)
        return ans

    def _solve(self, candidates, target, ans, curr, index):
        # Found valid combination
        if target == 0:
            ans.append(list(curr))
            return

        # Target exceeded
        if target < 0:
            return

        # Ran out of candidates
        if index >= len(candidates):
            return

        # No selection
        self._solve(candidates, target, ans, curr, index + 1)

        # Select current element
        curr.append(candidates[index])
        self._solve(candidates, target - candidates[index], ans, curr, index)
        curr.pop()  # backtrack


# Example usage
if __name__ == "__main__":
    solver = CombinationSum()
    candidates = [2, 3, 6, 7]
    target = 7
    print(solver.combination_sum(candidates, target))  
    # Output: [[7], [2, 2, 3]]

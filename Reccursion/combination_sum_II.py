"""
Time Complexity: O(2^n) where n is the number of candidates
Space Complexity: O(n) for recursive stack space
"""

class CombinationSumII:
    def combination_sum2(self, candidates, target):
        candidates.sort()
        ans = []
        self._combination(candidates, target, ans, [], 0)
        return ans

    def _combination(self, candidates, target, ans, curr, index):
        if target == 0:
            ans.append(list(curr))
            return

        if target < 0 or index >= len(candidates):
            return

        # Skip duplicates — move temp_index forward
        temp_index = index
        while (
            temp_index < len(candidates) - 1
            and candidates[temp_index] == candidates[temp_index + 1]
        ):
            temp_index += 1

        # Without selection (skip duplicates)
        self._combination(candidates, target, ans, curr, temp_index + 1)

        # With selection
        curr.append(candidates[index])
        self._combination(candidates, target - candidates[index], ans, curr, index + 1)
        curr.pop()


# Example usage
if __name__ == "__main__":
    solver = CombinationSumII()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(solver.combination_sum2(candidates, target))
    # Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]

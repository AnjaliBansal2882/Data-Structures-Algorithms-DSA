"""
Time Complexity: O(2^n) where n is the number of elements in the input array
Space Complexity: O(n) for recursive stack space
"""

class SubsetsI:
    def subset_sums(self, nums):
        ans = []
        self._subset(nums, 0, ans, 0)
        return ans

    def _subset(self, nums, curr_sum, ans, index):
        if index == len(nums):
            ans.append(curr_sum)
            return

        # Include current element
        self._subset(nums, curr_sum + nums[index], ans, index + 1)

        # Exclude current element
        self._subset(nums, curr_sum, ans, index + 1)


# Example usage
if __name__ == "__main__":
    solver = SubsetsI()
    nums = [5, 2, 1]
    print(solver.subset_sums(nums))
    # Output: [8, 7, 6, 5, 3, 2, 1, 0]

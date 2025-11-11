"""
Time Complexity: O(2^n) where n is the number of elements in the input array
Space Complexity: O(n) for recursive stack space
"""

class SubsetsII:
    def subsets_with_dup(self, nums):
        nums.sort()
        ans = []
        self._solve(nums, [], ans, 0)
        return ans

    def _solve(self, nums, curr, ans, index):
        if index == len(nums):
            ans.append(list(curr))
            return

        # Include current element
        curr.append(nums[index])
        self._solve(nums, curr, ans, index + 1)
        curr.pop()

        # Skip duplicates when excluding current element
        temp_index = index
        while temp_index + 1 < len(nums) and nums[temp_index] == nums[temp_index + 1]:
            temp_index += 1

        # Exclude current element and its duplicates
        self._solve(nums, curr, ans, temp_index + 1)


# Example usage
if __name__ == "__main__":
    solver = SubsetsII()
    nums = [1, 2, 2]
    print(solver.subsets_with_dup(nums))
    # Output:
    # [ [1, 2, 2], [1, 2], [1], [2, 2], [2], [] ]
